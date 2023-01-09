import discord
from discord.ext import commands
from discord import app_commands

class Clean(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def clean(self, ctx, num:int):
        await ctx.channel.purge(limit=num+1)

async def setup(bot):
    await bot.add_cog(Clean(bot))