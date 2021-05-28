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


bot = commands.Bot(command_prefix='n!', intents=intents)

class Error_Handler(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MemberNotFound):
            await ctx.send("I could not find this user")
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send("You do not have the permission to use this command")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("There is something wrong with the argument(s) you passed in")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("There are missing argument(s)")
        elif isinstance(error, commands.CommandOnCooldown):
            time_remaining = datetime.timedelta(seconds=int(error.retry_after))
            await ctx.send(f"Chill! You are on cooldown: *{time_remaining}*")
        elif isinstance(error, commands.CommandNotFound):
            await ctx.send("This command is either disabled or does not exist. Type `n!help` to see my available commands")
        elif isinstance(error, commands.CommandInvokeError):
            await ctx.send("An error occured while executing this command")
        elif isinstance(error, commands.CommandError):
            await ctx.send("An error occured while executing this command")
        elif isinstance(error, commands.MissingRole):
            await ctx.send("You don't have the required role to execute this command")
        elif isinstance(error, commands.MissingAnyRole):
            await ctx.send("You don't have the required roles to execute this command")   

def setup(bot):
    bot.add_cog(Error_Handler(bot))
