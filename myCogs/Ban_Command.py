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

class Ban(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(ban_members=True)
    @commands.cooldown(5, 86400, commands.BucketType.user)
    async def ban(self, ctx, member: discord.Member,*,reason=None):
        if reason == None:
            await ctx.send(embed=discord.Embed(
                title = "You cannot ban anyone without a reason",
                color = embed_color
            ))
            return

        ban_embed = discord.Embed(
            title = "❗ Notifier",
            description = "You were banned from Nocturnal",
            color = embed_color
        )
        ban_embed.add_field(
            name = "Reason",
            value = f"- {reason}",
            inline = False
        )
        ban_embed.add_field(
            name = "Responsible moderator",
            value = f"- {ctx.author}",
            inline = False
        )
        ban_embed.add_field(
            name = "Your user ID",
            value = f"- {member.id}\n\nIf you wish to appeal, you can use the informations above and fill up this [appeal form](https://docs.google.com/forms/d/e/1FAIpQLSc5oYS2ZZi1ZwhyEVlAvidin_54gDvvWOUyj2CZqIYG1BHZkw/viewform).",
            inline = False
        )
        
        await member.send(embed=ban_embed)
        await member.ban(reason=reason)
        await ctx.send(embed=discord.Embed(
            title = f"{member} was banned from the server",
            color = embed_color
        ))

def setup(bot):
    bot.add_cog(Ban(bot))
