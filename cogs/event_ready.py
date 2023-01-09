import discord
from discord.ext import commands
import sqlite3

class Ready(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
           
    @commands.Cog.listener()
    async def on_ready(self):
        db = sqlite3.connect("warning.sqlite")
        cursor = db.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS warns(user INTERGER, reason TEXT, time INTERGER, guild INTERGER)")
        print("bot is online")


async def setup(bot):
    await bot.add_cog(Ready(bot))