import discord
from discord.ext import commands

import asyncio

class Close_Ticket(commands.Cog):
  
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  @commands.has_permissions(kick_members=True)
  async def close(self, ctx):
    def check(m):
      return m.author.id == ctx.author.id
      
    if "ticket" in ctx.channel.name:
      await ctx.send(
        content = "{} This action **CANNOT** be undone! Are you sure you want to close this ticket? Reply with **YES** if so, and **NO** if not".format(ctx.author.mention)
      )
      
      try:
        response = await self.bot.wait_for(
          "message",
          check = check,
          timeout = 20
        )
        
        if response.content.upper() == "YES":
          await response.add_reaction("✅")
          countdown = 5
          sent = await ctx.send("{} This channel will be deleted in {} seconds".format(ctx.author.mention, countdown))
          
          while countdown != 0:
            await asyncio.sleep(1)
            countdown = countdown - 1
            await sent.edit(
              content = "{} This channel will be deleted in **{}** seconds".format(ctx.author.mention, countdown)
            )
          await ctx.channel.delete(
            reason = "Closed ticket"
          )
          
        elif response.content.upper() == "NO":
          await response.add_reaction("✅")
          
        else:
          await ctx.send(
            content = "{} Your response is none of the two choices".format(ctx.author.mention)
          )
          
      except asyncio.TimeoutError:
        await ctx.send(
          content = "{} You did not respond within 20 seconds".format(ctx.author.mention)
        )

    else:
      await ctx.send(
        content = "{} This command can only be used in ticket channels".format(ctx.author.mention)
      )

def setup(bot):
  bot.add_cog(Close_Ticket(bot))
