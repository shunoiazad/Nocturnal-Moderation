import discord
from discord.ext import commands

import random
import asyncio
import datetime
import pytz

import os

embed_color = 0x616060

class Mute(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True)
    @commands.cooldown(1, 8, commands.BucketType.user)
    async def mute(self, ctx, member: discord.Member, args=None):
        muted_role = discord.utils.find(lambda r: r.id == 819449455019425822, ctx.guild.roles)
        
        if member == self.bot.user:
            await ctx.send("I can't mute myself")

        else:
            if muted_role in member.roles:
                await ctx.send(embed=discord.Embed(
                    title = "{} is already muted".format(member),
                    color = embed_color
                ))
            
            else:
                if args:
                    if args.endswith("s"):
                        end_time = datetime.datetime.now(tz=pytz.UTC).astimezone(pytz.timezone('Asia/Manila')) + datetime.timedelta(seconds=int(args[0:-1]))
                        await member.add_roles(muted_role)
                        await ctx.send(embed=discord.Embed(
                            title = "{} will be muted until {}".format(member, end_time.strftime('%b %d, %Y %I:%M %p')),
                            color = embed_color
                        ))
                        await asyncio.sleep(int(args[0:-1]))
                        await member.remove_roles(muted_role)
                        await ctx.send(embed=discord.Embed(
                            title = "{} is now unmuted".format(member),
                            color = embed_color
                        ))

                    elif args.endswith("m"):
                        end_time = datetime.datetime.now(tz=pytz.UTC).astimezone(pytz.timezone('Asia/Manila')) + datetime.timedelta(minutes=int(args[0:-1]))
                        await member.add_roles(muted_role)
                        await ctx.send(embed=discord.Embed(
                            title = "{} will be muted until {}".format(member, end_time.strftime('%b %d, %Y %I:%M %p')),
                            color = embed_color
                        ))
                        await asyncio.sleep(int(args[0:-1])*60)
                        await member.remove_roles(muted_role)
                        await ctx.send(embed=discord.Embed(
                            title = "{} is now unmuted".format(member),
                            color = embed_color
                        ))

                    elif args.endswith("h"):
                        end_time = datetime.datetime.now(tz=pytz.UTC).astimezone(pytz.timezone('Asia/Manila')) + datetime.timedelta(hours=int(args[0:-1]))
                        await member.add_roles(muted_role)
                        await ctx.send(embed=discord.Embed(
                            title = "{} will be muted until {}".format(member, end_time.strftime('%b %d, %Y %I:%M %p')),
                            color = embed_color
                        ))
                        await asyncio.sleep(int(args[0:-1])*3600)
                        await member.remove_roles(muted_role)
                        await ctx.send(embed=discord.Embed(
                            title = "{} is now unmuted".format(member),
                            color = embed_color
                        ))

                    elif args.endswith("d"):
                        end_time = datetime.datetime.now(tz=pytz.UTC).astimezone(pytz.timezone('Asia/Manila')) + datetime.timedelta(days=int(args[0:-1]))
                        await member.add_roles(muted_role)
                        await ctx.send(embed=discord.Embed(
                            title = "{} will be muted until {}".format(member, end_time.strftime('%b %d, %Y %I:%M %p')),
                            color = embed_color
                        ))
                        await asyncio.sleep(int(args[0:-1])*86400)
                        await member.remove_roles(muted_role)
                        await ctx.send(embed=discord.Embed(
                            title = "{} is now unmuted".format(member),
                            color = embed_color
                        ))
                    
                    else:
                        await ctx.send("I don't understand what you mean")
                
                else:
                    await member.add_roles(muted_role)
                    await ctx.send(embed=discord.Embed(
                        title = "{} has been muted".format(member),
                        color = embed_color
                    ))


def setup(bot):
    bot.add_cog(Mute(bot))
