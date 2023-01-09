import discord
from discord.ext import commands

class Kick(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True)#確認使用者有踢出成員的權限
    async def kick(self, ctx, member:discord.Member, *, reason=None):
        if reason == None:
            reason="no reason provided"
        await ctx.guild.kick(member)#對指定成員踢出伺服器
        await ctx.send(f"User {member.mention} has been kicked for {reason}")#發送訊息

    @commands.command()
    @commands.has_permissions(ban_members=True)#確認使用者有停權成員的權限
    async def ban(self, ctx, member:discord.Member, *, reason=None):
        if reason == None:
            reason="no reason provided"
        await ctx.guild.ban(member)#對指定成員停權
        await ctx.send(f"User {member.mention} has been banned for {reason}")#發送訊息

async def setup(bot):
    await bot.add_cog(Kick(bot))