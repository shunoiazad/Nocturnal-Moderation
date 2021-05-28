import discord
from discord.ext import commands

import random
import asyncio
import datetime
import pytz

import os

embed_color = 0x616060

intents = discord.Intents.default()
intents.members = True

class Unban(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, userid: int, moderator_note=None):
        banned_users = await ctx.guild.bans()

        for banned in banned_users:
            user = banned.user
            if user.id == userid:
                await ctx.guild.unban(user)

                await ctx.send(embed=discord.Embed(
                    title = f'{user} is now unbanned',
                    color = embed_color
                ))
                return
        
        await ctx.send(embed=discord.Embed(
            title = "User ID not found",
            color = embed_color
        ))

def setup(bot):
    bot.add_cog(Unban(bot))
