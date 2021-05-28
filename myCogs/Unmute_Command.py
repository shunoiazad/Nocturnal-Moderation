import discord
from discord.ext import commands

import random
import asyncio
import datetime
import pytz

import os

embed_color = 0x616060

class Unmute(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True)
    @commands.cooldown(1, 8, commands.BucketType.user)
    async def unmute(self, ctx, member: discord.Member):
        muted = discord.utils.get(ctx.guild.roles, id=819449455019425822)
        if not muted in member.roles:
            await ctx.send(embed=discord.Embed(
                title = f"{member} is not even muted",
                color = embed_color
            ))
        else:
            await member.remove_roles(muted)
            await ctx.send(embed=discord.Embed(
                title = f"{member} is now unmuted",
                color = embed_color
            ))

def setup(bot):
    bot.add_cog(Unmute(bot))
