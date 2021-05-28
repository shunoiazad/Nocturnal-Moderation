import discord
from discord.ext import commands

import asyncio


embed_color = 0x616060

class Confirmation_Response_Checker(commands.Cog):
  
  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener()
  async def on_member_join(self, member):
    await asyncio.sleep(300)
    confirmationRole = discord.utils.find(lambda r: r.id == 827075812050206720, self.bot.get_guild(819194655999524914).roles)
    if confirmationRole in member.roles:
      kick_embed = discord.Embed(
        title = "❗ Notifier",
        description = "You were kicked from Nocturnal",
        color = embed_color
      )
      kick_embed.add_field(         name = "Reason",
        value = "- Not responding in the confirmation",
        inline = False
      )
      kick_embed.add_field(
        name = "Responsible moderator",
        value = "- Nocturnal Automated Moderation",
        inline = False
      )
      await member.send(
        embed = kick_embed
      )
      await member.kick(reason="Nocturnal Automated Moderation: Not responding in the confirmation within 5 minutes")
        
      
def setup(bot):
  bot.add_cog(Confirmation_Response_Checker(bot))
