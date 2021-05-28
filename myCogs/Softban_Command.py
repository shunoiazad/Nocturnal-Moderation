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

class Softban(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def softban(self, ctx, member: discord.Member,*,reason="Unspecified"):
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
        await member.ban(reason=reason)
        await asyncio.sleep(1)
        await member.unban()
        await ctx.send(embed=discord.Embed(
            title = f"{member} was kicked from the server",
            color = embed_color
        ))

def setup(bot):
    bot.add_cog(Softban(bot))
