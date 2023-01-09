import discord
from discord import app_commands
from discord.ext import commands

class Slash_math(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="math")
    async def math(self, interaction: discord.Interaction, formula : str):
        await interaction.response.send_message(f"<a:gifudefinedImgur10:1061592595278614588> **| {str(interaction.user)[:-5]}**, the answeris: **{eval(str(formula))}**")
async def setup(bot):
    await bot.add_cog(Slash_math(bot), guilds = [discord.Object(id=1020285373596831764)])