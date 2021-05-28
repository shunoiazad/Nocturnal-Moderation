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

class Lockdown(commands.Cog):
  
  def __init__(self, bot):
    self.bot = bot
  
  @commands.command()
  @commands.has_permissions(ban_members=True)
  async def lockdown(self, ctx):
      overwrites = {
        ctx.guild.default_role: discord.PermissionOverwrite(view_channel=False)
      }
      await ctx.channel.edit(overwrites=overwrites)
      await ctx.send("<#{}> was put to lockdown by {}".format(ctx.channel.id, ctx.author.mention))

  
  @commands.command()
  @commands.has_permissions(ban_members=True)
  async def unlock(self, ctx):
      overwrites = {
        ctx.guild.default_role: discord.PermissionOverwrite(send_messages=True, attach_files=True, add_reactions=True, read_messages=True)
      }
      await ctx.channel.edit(overwrites=overwrites)
      await ctx.send("{} removed the lockdown for <#{}>".format(ctx.author.mention, ctx.channel.id))
    
  
        
def setup(bot):
  bot.add_cog(Lockdown(bot))
