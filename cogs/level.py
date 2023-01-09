import profile
import discord
import json

from discord import File
from discord.ext import commands
from typing import Optional 

class Level(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if not message.author.bot:
            with open("levels.json", "r") as f:
                data = json.load(f)

            if str(message.author.id) in data:
                xp = data[str(message.author.id)]["xp"]
                lvl = data[str(message.author.id)]["level"]

                increased_xp = xp+25
                new_level = int(increased_xp/100)

                data[str(message.author.id)]["xp"] = increased_xp

                with open("levels.json", "w") as f:
                    json.dump(data, f)

                if new_level > lvl:
                    await message.channel.send(f"{message.author.mention} Just Leveled up to level {new_level}!")

                    data[str(message.author.id)]["level"] = new_level
                    data[str(message.author.id)]["xp"] = 0
                    
                    with open("levels.json", "w") as f:
                        json.dump(data, f)

            else:
                data[str(message.author.id)] = {}
                data[str(message.author.id)]["xp"] = 0
                data[str(message.author.id)]["level"] = 1

                with open("levels.json", "w") as f:
                    json.dump(data, f)
    
async def setup(bot):
    await bot.add_cog(Level(bot))
