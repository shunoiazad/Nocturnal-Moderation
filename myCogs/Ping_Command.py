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

class Ping(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def ping(self, ctx):
        lines = [f"My latency: `{round(self.bot.latency*1000)}ms`", "Pong!"]
        await ctx.send(random.choice(lines))

def setup(bot):
  bot.add_cog(Ping(bot))
