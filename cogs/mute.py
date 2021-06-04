import discord
from discord.ext import commands
import json
import asyncio
import datetime
import pytz

with open('config.json', 'r') as f:
    config = json.load(f)

class Mute(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='mute')
    @commands.has_permissions(manage_roles=True)
    async def mute_cmd(self, ctx, member: discord.Member, args=config['defaults']['mute_limit']):
        try:
            muted_role = discord.utils.find(lambda r: r.id == config['muted_role'], ctx.guild.roles)
            
            if member == self.bot.user:
                await ctx.reply("I can't mute myself")

            else:
                if muted_role in member.roles:
                    await ctx.reply("{} is already muted".format(member))
                
                else:
                    if args:
                        if args.endswith("s"):
                            end_time = datetime.datetime.now(tz=pytz.UTC).astimezone(pytz.timezone('Asia/Manila')) + datetime.timedelta(seconds=int(args[0:-1]))
                            await member.add_roles(muted_role)
                            await ctx.send(embed=discord.Embed(
                                title = "{} will be muted until {}".format(member, end_time.strftime('%b %d, %Y %I:%M %p')),
                                color = int(config["embed_color"], 16)
                            ))
                            await asyncio.sleep(int(args[0:-1]))
                            await member.remove_roles(muted_role)
                            await ctx.send(embed=discord.Embed(
                                title = "{} is now unmuted".format(member),
                                color = int(config["embed_color"], 16)
                            ))

                        elif args.endswith("m"):
                            end_time = datetime.datetime.now(tz=pytz.UTC).astimezone(pytz.timezone('Asia/Manila')) + datetime.timedelta(minutes=int(args[0:-1]))
                            await member.add_roles(muted_role)
                            await ctx.send(embed=discord.Embed(
                                title = "{} will be muted until {}".format(member, end_time.strftime('%b %d, %Y %I:%M %p')),
                                color = int(config["embed_color"], 16)
                            ))
                            await asyncio.sleep(int(args[0:-1])*60)
                            await member.remove_roles(muted_role)
                            await ctx.send(embed=discord.Embed(
                                title = "{} is now unmuted".format(member),
                                color = int(config["embed_color"], 16)
                            ))

                        elif args.endswith("h"):
                            end_time = datetime.datetime.now(tz=pytz.UTC).astimezone(pytz.timezone('Asia/Manila')) + datetime.timedelta(hours=int(args[0:-1]))
                            await member.add_roles(muted_role)
                            await ctx.send(embed=discord.Embed(
                                title = "{} will be muted until {}".format(member, end_time.strftime('%b %d, %Y %I:%M %p')),
                                color = int(config["embed_color"], 16)
                            ))
                            await asyncio.sleep(int(args[0:-1])*3600)
                            await member.remove_roles(muted_role)
                            await ctx.send(embed=discord.Embed(
                                title = "{} is now unmuted".format(member),
                                color = int(config["embed_color"], 16)
                            ))

                        elif args.endswith("d"):
                            end_time = datetime.datetime.now(tz=pytz.UTC).astimezone(pytz.timezone('Asia/Manila')) + datetime.timedelta(days=int(args[0:-1]))
                            await member.add_roles(muted_role)
                            await ctx.send(embed=discord.Embed(
                                title = "{} will be muted until {}".format(member, end_time.strftime('%b %d, %Y %I:%M %p')),
                                color = int(config["embed_color"], 16)
                            ))
                            await asyncio.sleep(int(args[0:-1])*86400)
                            await member.remove_roles(muted_role)
                            await ctx.send(embed=discord.Embed(
                                title = "{} is now unmuted".format(member),
                                color = int(config["embed_color"], 16)
                            ))
                        
                        else:
                            await ctx.reply("Use `n!help mute` for the proper usage of the command.")
                    
                    else:
                        await member.add_roles(muted_role)
                        await ctx.send(embed=discord.Embed(
                            title = "{} has been muted".format(member),
                            color = int(config["embed_color"], 16)
                        ))
        except Exception as e:
            await ctx.reply(f"```{e}```")

def setup(bot):
    bot.add_cog(Mute(bot))
