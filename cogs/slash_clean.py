
import discord
from discord import app_commands
from discord.ext import commands

class Slash_clean(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="clean")
    @commands.has_permissions(manage_messages = True)
    async def clean(self, interaction:discord.Interaction, num:int):
        await interaction.response.send_message(f"<a:gifundefineImgur4:1061592625427255347> done.", ephemeral=True)
        await interaction.channel.purge(limit=num)
async def setup(bot):
    await bot.add_cog(Slash_clean(bot), guilds = [discord.Object(id=1020285373596831764)])
