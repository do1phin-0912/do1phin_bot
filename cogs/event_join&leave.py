import discord
from discord.ext import commands
import datetime

class Member(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel#設定發送訊息頻道
        embed=discord.Embed(title="Welcome!", color=0x80b2c6, timestamp= datetime.datetime.now())
        embed.add_field(name=member.name + "!", value="Welcome to **" + member.guild.name + "**", inline=False)
        await channel.send(embed=embed)#發送嵌入文字

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = member.guild.system_channel#設定發送訊息頻道
        embed=discord.Embed(title="Good Bye!", color=0x80b2c6, timestamp= datetime.datetime.now())
        embed.add_field(name=member.name + "!", value="Leave the server, so sad!", inline=False)
        await channel.send(embed=embed)#發送嵌入文字

async def setup(bot):
    await bot.add_cog(Member(bot))
