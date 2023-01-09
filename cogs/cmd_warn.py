import discord
from discord.ext import commands
import sqlite3
import asyncio
from datetime import datetime
from discord import app_commands

async def addwarn(ctx, reason, user):
    db = sqlite3.connect("warning.sqlite")
    cursor = db.cursor()
    cursor.execute("INSERT INTO warns (user, reason, time, guild) VALUES (?, ?, ?, ?)", (user.id, reason, int(datetime.now().timestamp()),ctx.guild.id))
    db.commit()

class Warn(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @app_commands.command(name="warn")
    @commands.has_permissions(kick_members=True)
    async def warn(self, interation: discord.Interaction, member:discord.Member, *, reason:str = "No reason"):
        await addwarn(interation, reason, member)
        await interation.response.send_message(f"Warned {member.mention} for {reason}")

        db = sqlite3.connect("warning.sqlite")
        cursor = db.cursor()
        cursor.execute("SELECT * FROM warns WHERE user = ? AND guild = ?", (member.id, interation.guild.id))
        data = cursor.fetchall()
        if len(data) >= 3:
            muteRole = discord.utils.get(interation.guild.roles, name="Muted")
            await member.add_roles(muteRole)
            await interation.response.send_message(f"You have been warned {len(data)} times and your are now temp muted")
            await asyncio.sleep(10)
            await member.remove_roles(muteRole)
            await interation.response.send_message(f"{member.mention} You have been unmuted")

    @app_commands.command(name="removewarn")
    async def removewarn(self, interaction: discord.Interaction, member:discord.Member):
        db = sqlite3.connect("warning.sqlite")
        cursor = db.cursor()
        cursor.execute("SELECT reason FROM warns WHERE user = ? AND guild = ?", (member.id, interaction.guild.id))
        data = cursor.fetchone()
        if data:
            cursor.execute("DELETE FROM warns WHERE user = ? AND guild = ?", (member.id, interaction.guild.id))
            await interaction.response.send_message("Warns have been removed")
        else:
            await interaction.response.send_message("You dont have any warnings")
    
        db.commit()

async def setup(bot):
    await bot.add_cog(Warn(bot), guilds = [discord.Object(id=1020285373596831764)])