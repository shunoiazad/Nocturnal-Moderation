import discord
from discord.ext import commands

import random
import asyncio
import datetime
import pytz

import os
from keep_alive import keep_alive

embed_color = 0x616060

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='n!', intents=intents, help_command=None)

#onready---
@bot.event
async def on_ready():
    print(f'Successfully logged in as: {bot.user.name}')


#LOAD COMMANDS
@bot.command()
@commands.is_owner()
async def enable(ctx, extension):
    if ctx.author.id == 386860764368994304:
        try:
            if extension == "all":
                for f in os.listdir('./myCogs'):
                    if f.endswith('.py'):
                        exempted_files = ["Snipe_Command.py"]
                        if f in exempted_files:
                            pass

                        else:
                            bot.load_extension(f'myCogs.{f[:-3]}')
                            await ctx.message.add_reaction("✅")
                            
                    else:
                        pass
            else:
                bot.load_extension(f'myCogs.{extension}')
                await ctx.message.add_reaction("✅")

        except Exception as error:
            await ctx.message.reply(
              content = '''An error occured: ```{}```'''.format(error)
          )
          
    else:
        await ctx.send(embed=discord.Embed(
            title = "You don't have the permission to use this command",
            color = embed_color
        ))

@bot.command()
@commands.is_owner()
async def refresh(ctx, extension):
    if ctx.author.id == 386860764368994304 or 657181824673513482:
        try:
            if extension == "all":
                for f in os.listdir('./myCogs'):
                    if f.endswith('.py'):
                        exempted_files = ["Snipe_Command.py"]
                        if f in exempted_files:
                            pass

                        else:
                            bot.unload_extension(f'myCogs.{f[:-3]}')
                            await asyncio.sleep(0.1)
                            bot.load_extension(f'myCogs.{f[:-3]}')
                            await ctx.message.add_reaction("✅")
                            

                    else:
                        pass
            else:
                bot.unload_extension(f'myCogs.{extension}')
                await asyncio.sleep(0.1)
                bot.load_extension(f'myCogs.{extension}')
                await ctx.message.add_reaction("✅")

        except Exception as error:
            await ctx.message.reply(
              content = '''An error occured: ```{}```'''.format(error)
          )
          
    else:
        await ctx.send(embed=discord.Embed(
            title = "You don't have the permission to use this command",
            color = embed_color
        ))

@bot.command()
@commands.is_owner()
async def disable(ctx, extension):
    if ctx.author.id == 386860764368994304:
        try:
            if extension == "all":
                for f in os.listdir('./myCogs'):
                    if f.endswith('.py'):
                        exempted_files = ["Snipe_Command.py"]
                        if f in exempted_files:
                            pass
                        else:
                            bot.unload_extension(f'myCogs.{f[:-3]}')
                            await ctx.message.add_reaction("✅")
                            
                    else:
                        pass
            else:
                bot.unload_extension(f'myCogs.{extension}')
                await ctx.message.add_reaction("✅")

        except Exception as error:
            await ctx.message.reply(
              content = '''An error occured: ```{}```'''.format(error)
          )
          
    else:
        await ctx.send(embed=discord.Embed(
            title = "You don't have the permission to use this command",
            color = embed_color
        ))







@bot.command(aliases=['cmds','help'])
async def commands(ctx):
    mod_embed = discord.Embed(
        title = "Commands list",
        color = embed_color
    )
    mod_embed.add_field(
        name = 'Tickets',
        value = "`n!close` - closes a ticket, minor purpose channels",
        inline = False
    )
    mod_embed.add_field(
        name = 'Miscellaneous',
        value = "`n!rule <rule number>` - displays the rule of its specified rule number",
        inline = False
    )
    mod_embed.add_field(
        name = "Channels",
        value = "`n!purge <optional amount>` - bulk deletes messages in a channel, default is 5\n`n!lockdown` - locks the channel the command is executed in\n`n!unlock` - unlocks the channel the command is executed in",
        inline = False
    )
    mod_embed.add_field(
        name = "Mutes",
        value = "`n!mute <user> <optional amount> <optional unit>` - mutes the specified user unconditionally or temporarily\n`n!unmute <user>` - unmuted the specified user",
        inline = False
    )
    mod_embed.add_field(
        name = "Warns",
        value = "`n!warn <user> <reason>` - warns the specified member\n`n!removewarn <user> <reference>` - removes the warn from the specific warn reference of the user\n`n!clearwarn <user>` - clears all the warn from the user",
        inline = False
    )
    mod_embed.add_field(
        name = "Advanced Moderation",
        value = "`n!kick <user> <optional reason>` - kicks the specified member\n`n!softban <user> <optional reason>` - kicks the user and deletes all of their message in the server\n`n!ban <user> <reason>` - bans the specified member\n`n!unban <userid> <optional moderator note>` - unbans the specified user ID holder",
        inline = False
    )
    await ctx.send(embed=mod_embed)











@bot.command()
async def perms(ctx, member: discord.Member):
    await ctx.send(member.permissions_in(ctx.channel))














for f in os.listdir("myCogs"):
    if f.endswith(".py"):
        excepted = []
        if f in excepted:
            pass

        else:
            bot.load_extension("myCogs.{}".format(f[:-3]))





keep_alive()
token = os.getenv("TOKEN")
bot.run(token)
