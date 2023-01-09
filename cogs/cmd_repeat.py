import discord
from discord.ext import commands
from discord import app_commands

class Repeat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
  
    @commands.command()
    async def say(self, ctx, *, msg):
        await ctx.message.delete()#刪除指令訊息
        await ctx.send(msg)#覆誦指定訊息

async def setup(bot):
    await bot.add_cog(Repeat(bot))