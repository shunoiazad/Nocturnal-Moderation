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

class Kick(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member,*,reason="Reason not specified"):
        kick_embed = discord.Embed(
            title = "❗ Notifier",
            description = "You were kicked from Nocturnal",
            color = embed_color
        )
        kick_embed.add_field(
            name = "Reason",
            value = f"- {reason}",
            inline = False
        )
        kick_embed.add_field(
            name = "Responsible moderator",
            value = f"- {ctx.author}",
            inline = False
        )
        await member.send(embed=kick_embed)
        await member.kick(reason=reason)
        await ctx.send(embed=discord.Embed(
            title = f"{member} has been kicked from the server",
            color = embed_color
        ))

def setup(bot):
    bot.add_cog(Kick(bot))
