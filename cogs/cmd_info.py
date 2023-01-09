import discord 
from discord.ext import commands
from discord import app_commands
import json

class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        

    @commands.command()
    async def info(self, ctx):
        with open('levels.json', 'r') as f:
            data = json.load(f)
            if str(ctx.author.id) in data:
                lvl = data[str(ctx.author.id)]["level"]
                xp = data[str(ctx.author.id)]["xp"]
                embed=discord.Embed(title=f"This is your profile!! <a:gifundefinedImgur7:1061592610847854674>", color=0x80b2c6, description="Your level : " + str(lvl) + f"\n    *exp : {xp} \/ {lvl*100}*")
                embed.set_author(name=str(ctx.author)[:-5])
                embed.set_thumbnail(url=ctx.author.avatar)
                await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Info(bot))
