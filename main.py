import os
import discord
from discord.ext import commands
from discord import app_commands

intents = discord.Intents.all()
intents.members = True
intents.message_content = True

class abot(commands.Bot):
    def __init__(self):
        super().__init__(intents=discord.Intents.all(), command_prefix = "!", application = 1014824301586821140)
    
    async def setup_hook(self):
        for file in os.listdir('./cogs'):
            if file.endswith('.py'):
                await self.load_extension(f'cogs.{file[:-3]}')

        await bot.tree.sync(guild=discord.Object(id=1020285373596831764))

    async def on_ready(self):
        print(f"{self.user} has connected to discord")

bot = abot()
bot.run("TOKEN")
