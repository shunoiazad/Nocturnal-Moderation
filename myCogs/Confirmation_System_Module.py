import discord
from discord.ext import commands

import asyncio
import random

embed_color = 0x616060

intents = discord.Intents.default()
intents.members = True
intents.reactions = True

class Confirmation_System(commands.Cog):

  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener()
  async def on_raw_reaction_add(self, payload):
    emoji1 = self.bot.get_emoji(846719237690884096)
    emoji2 = self.bot.get_emoji(846719362739732511)
    
    
    confirmationRole = discord.utils.find(lambda r: r.id == 827075812050206720, self.bot.get_guild(819194655999524914).roles)
    msg_id = payload.message_id
    guild = self.bot.get_guild(payload.guild_id)
    member = discord.utils.find(lambda m: m.id == payload.member.id, guild.members)
    reaction = payload.emoji
    channel = self.bot.get_channel(827075769833750579)
    msg = await channel.fetch_message(846720884576354314)
    await msg.remove_reaction(reaction, member)
    if confirmationRole in member.roles:
      if msg_id == 846720884576354314:
        if reaction == emoji1:
          sent = await self.bot.get_channel(827075769833750579).send(
              content = "{} You may now proceed".format(member.mention)
          )
          await asyncio.sleep(3)
          await sent.delete()
          await member.remove_roles(confirmationRole)
          embed = discord.Embed(
            title = f"{member} confirmed their age",
            color = embed_color
          )
          embed.set_footer(
            text = "Authorised by Age Confirmation"
          )
          await self.bot.get_channel(819462564500996116).send(embed=embed)
          

        elif reaction == emoji2:
          ban_embed = discord.Embed(
            title = "❗ Notifier",
            description = "You were banned from Nocturnal",
            color = embed_color
          )
          ban_embed.add_field(
            name = "Reason",
            value = "- Underage / Discord ToS Violation",
            inline = False
          )
          ban_embed.add_field(
            name = "Responsible moderator",
            value = "- Nocturnal Automated Moderation",
            inline = False
          )
          ban_embed.add_field(
            name = "Your user ID",
            value = f"- {msg.author.id}\n\nIf you wish to appeal, you can use the informations above and fill up this [appeal form](https://docs.google.com/forms/d/e/1FAIpQLSc5oYS2ZZi1ZwhyEVlAvidin_54gDvvWOUyj2CZqIYG1BHZkw/viewform).",
            inline = False
          )
            
          await member.send(embed=ban_embed)
          await member.ban(reason="Nocturnal Automated Moderation: Underage / Discord TOS Violation")
          embed = discord.Embed(
            title = f"{member} was banned from the server: Underage",
            color = embed_color
          )
          embed.set_footer(
            text = "Banned by Age Confirmation"
          )
          await self.bot.get_channel(819462564500996116).send(embed=embed)
      

def setup(bot):
  bot.add_cog(Confirmation_System(bot))
