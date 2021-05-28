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

class Antiracism_Module(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, msg):
        guild = self.bot.get_guild(819194655999524914)
        staff_roles = [
            discord.utils.find(lambda r: r.id == 819195059505332255, guild.roles),
            discord.utils.find(lambda r: r.id == 819195142836846622, guild.roles),
            discord.utils.find(lambda r: r.id == 840473687105732608, guild.roles)
        ]
        
        
        n_words = ['nigga','negga','nigger','niggar','nieger','niegger','niegga','nigg@','n!gga@','ni66a','ni66@','neigga','neyga','niyga','neygga','niygga','nibba','neggro','negro']
        for word in n_words:
            if word.lower() in msg.content.lower():
                if msg.author.top_role in staff_roles:
                    await msg.delete()
                    return
                    
                ban_embed = discord.Embed(
                    title = "❗ Notifier",
                    description = f"You were banned from {msg.guild}",
                    color = embed_color
                )
                ban_embed.add_field(
                    name = "Reason",
                    value = "- Your message was found inappropriate to Nocturnal environment",
                    inline = False
                )
                ban_embed.add_field(
                    name = "Your message",
                    value = f"- {msg.content}",
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
                await msg.author.send(embed=ban_embed)
                await msg.author.ban(reason="Nocturnal Automated Moderation: Racism")
                await msg.channel.send(embed=discord.Embed(
                    title = f"{msg.author} was banned from the server",
                    color = embed_color
                ))

    

def setup(bot):
    bot.add_cog(Antiracism_Module(bot))
