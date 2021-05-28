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

class Purge(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_messages=True, kick_members=True)
    @commands.cooldown(1, 7, commands.BucketType.user)
    async def purge(self, ctx, amount: int=5):
      amt = amount + 1
      await ctx.channel.purge(limit=amt)
      
      sent = await ctx.send(f"Deleted previous *{amount} messages*.")
      await asyncio.sleep(3.5)
      await sent.delete()
       

def setup(bot):
    bot.add_cog(Purge(bot))
