import discord
from discord.ext import commands

class Math(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def math(self, ctx, *, message):
        print(message)
        s = str(message)
        await ctx.channel.send(eval(s))

async def setup(bot):
    await bot.add_cog(Math(bot))
