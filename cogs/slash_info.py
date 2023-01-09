from email import message
import discord 
from discord.ext import commands
from discord import app_commands
import json

class Slash_info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="info")
    async def info(self, interation: discord.Interaction):
        with open('levels.json', 'r') as f:
            data = json.load(f)
            if str(interation.user.id) in data:
                lvl = data[str(interation.user.id)]["level"]
                xp = data[str(interation.user.id)]["xp"]
                embed=discord.Embed(title=f"This is your profile!! <a:gifundefinedImgur7:1061592610847854674>", color=0x80b2c6, description="Your level : " + str(lvl) + f"\n    *exp : {xp} \/ {lvl*100}*")
                embed.set_author(name=str(interation.user)[:-5])
                embed.set_thumbnail(url=interation.user.avatar)
                await interation.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(Slash_info(bot), guilds = [discord.Object(id=1020285373596831764)])