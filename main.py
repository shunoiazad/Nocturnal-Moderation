import discord
from discord.ext import commands
import os
import json
import asyncio


with open('config.json', 'r') as f:
    config = json.load(f)

bot = commands.Bot(command_prefix=config['bot_prefix'])

#remove default help
bot.remove_command('help')


#on ready
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")


#load
@bot.command(name='load')
@commands.has_permissions(administrator=True)
async def load_cog(ctx, extension):
    try:
        cog = f"cogs.{extension.lower()}"
        bot.load_extension(cog)
        await ctx.message.add_reaction('✅')
    except Exception as e:
        await ctx.reply(f'```{e}```')


#unload
@bot.command(name='unload')
@commands.has_permissions(administrator=True)
async def unload_cog(ctx, extension):
    try:
        cog = f"cogs.{extension.lower()}"
        bot.unload_extension(cog)
        await ctx.message.add_reaction('✅')
    except Exception as e:
        await ctx.reply(f'```{e}```')


#reload
@bot.command(name='reload')
@commands.has_permissions(administrator=True)
async def reload_cog(ctx, extension):
    try:
        cog = f"cogs.{extension.lower()}"
        bot.unload_extension(cog)
        bot.load_extension(cog)
        await ctx.message.add_reaction('✅')
    except Exception as e:
        await ctx.reply(f'```{e}```')


#refresh
@bot.command(name='refresh')
@commands.is_owner()
async def refresh(ctx):
    for f in os.listdir('./cogs'):
        if f.endswith('.py') and not f in config["exempted_cogs"]:
            try:
                cog = f'cogs.{f[0:-3]}'
                bot.load_extension(cog)
                bot.unload_extension(cog)
                bot.load_extension(cog)
            except:
                pass
    await ctx.message.add_reaction('✅')














#HELP_CMD
@bot.group(name="help", aliases=["cmds", "commands"], invoke_without_command=True)
async def help_command(ctx):
    mod_embed = discord.Embed(
        title = "Commands list",
        color = int(config["embed_color"], 16)
    )
    mod_embed.add_field(
        name = 'Tickets',
        value = "`close`",
        inline = False
    )
    mod_embed.add_field(
        name = "Channels",
        value = "`purge`, `lockdown`",
        inline = False
    )
    mod_embed.add_field(
        name = "Mutes",
        value = "`mute`, `unmute`",
        inline = False
    )
    mod_embed.add_field(
        name = "Warns",
        value = "`warn`, `removewarn`, `clearwarns`",
        inline = False
    )
    mod_embed.add_field(
        name = "Advanced Moderation",
        value = "`kick`, `softban`, `ban`, `unban`, `email`",
        inline = False
    )
    mod_embed.set_footer(
        text = "Use n!help <command>, to see the specified command's information and usage"
    )
    try:
        await ctx.send(embed=mod_embed)
    except Exception as e:
        await ctx.reply(f'```{e}```')



#HELP SUB CMDS
#CLOSE_CMD
@help_command.command(name="close")
async def close_command(ctx):
    embed = discord.Embed(
        title = "Close Command (UNAVAILABLE)",
        color = int(config["embed_color"], 16)
    )
    embed.add_field(
        name = "Description",
        value = "Closes minor purposed channels such as tickets.",
        inline = False
    )
    embed.add_field(
        name = "Usage",
        value = "`n!close`",
        inline = False
    )
    try:
        await ctx.send(embed=embed)
    except Exception as e:
        await ctx.reply(f'```{e}```')

#PURGE_CMD
@help_command.command(name="purge")
async def purge_command(ctx):
    embed = discord.Embed(
        title = "Purge Command",
        color = int(config["embed_color"], 16)
    )
    embed.add_field(
        name = "Description",
        value = "Purges channel, basically clearing previous messages with the specified amount.",
        inline = False
    )
    embed.add_field(
        name = "Usage",
        value = "`n!purge <amount / default=5>`",
        inline = False
    )
    try:
        await ctx.send(embed=embed)
    except Exception as e:
        await ctx.reply(f'```{e}```')

#LOCKDOWN_CMD
@help_command.command(name="lockdown")
async def lockdown_command(ctx):
    embed = discord.Embed(
        title = "Lockdown Command (UNAVAILABLE)",
        color = int(config["embed_color"], 16)
    )
    embed.add_field(
        name = "Description",
        value = "This command is used in urgent situations. It locks and override the channel permissions for `@everyone` to `view_channel=false`.",
        inline = False
    )
    embed.add_field(
        name = "Usage",
        value = "`n!lockdown`",
        inline = False
    )
    try:
        await ctx.send(embed=embed)
    except Exception as e:
        await ctx.reply(f'```{e}```')

#MUTE_CMD
@help_command.command(name="mute")
async def mute_command(ctx):
    embed = discord.Embed(
        title = "Mute Command",
        color = int(config["embed_color"], 16)
    )
    embed.add_field(
        name = "Description",
        value = "Mutes the specified user with the time given. It takes 2 arguments, which is the user and the time limit. `s` stands for second(s), `m` stands for minute(s), `h` stands for hour(s), and `d` stands for days(s). An example for time limits are `2m`, `12h` and `5d`.",
        inline = False
    )
    embed.add_field(
        name = "Usage",
        value = "`n!mute <@user> <time limit>`",
        inline = False
    )
    try:
        await ctx.send(embed=embed)
    except Exception as e:
        await ctx.reply(f'```{e}```')

#UNMUTE_CMD
@help_command.command(name="unmute")
async def unmute_command(ctx):
    embed = discord.Embed(
        title = "Unmute Command",
        color = int(config["embed_color"], 16)
    )
    embed.add_field(
        name = "Description",
        value = "Removes the mute from the specified user.",
        inline = False
    )
    embed.add_field(
        name = "Usage",
        value = "`n!unmute <@user>`",
        inline = False
    )
    try:
        await ctx.send(embed=embed)
    except Exception as e:
        await ctx.reply(f'```{e}```')

#WARN_CMD
@help_command.command(name="warn")
async def warn_command(ctx):
    embed = discord.Embed(
        title = "Warn Command",
        color = int(config["embed_color"], 16)
    )
    embed.add_field(
        name = "Description",
        value = "Warns the specified user and a reason must be provided.",
        inline = False
    )
    embed.add_field(
        name = "Usage",
        value = "`n!warn <@user> <reason>`",
        inline = False
    )
    try:
        await ctx.send(embed=embed)
    except Exception as e:
        await ctx.reply(f'```{e}```')

#WARNINGS_CMD
@help_command.command(name="warnings")
async def warnings_command(ctx):
    embed = discord.Embed(
        title = "Warnings Command",
        color = int(config["embed_color"], 16)
    )
    embed.add_field(
        name = "Description",
        value = "Shows every warnings of the user.",
        inline = False
    )
    embed.add_field(
        name = "Usage",
        value = "`n!warnings <@user>`",
        inline = False
    )
    try:
        await ctx.send(embed=embed)
    except Exception as e:
        await ctx.reply(f'```{e}```')

#REMOVEWARN_CMD
@help_command.command(name="removewarn", aliases=["delwarn"])
async def removewarn_command(ctx):
    embed = discord.Embed(
        title = "Removewarn Command",
        color = int(config["embed_color"], 16)
    )
    embed.add_field(
        name = "Description",
        value = "Removes the warning of a user with an specific warn reference.",
        inline = False
    )
    embed.add_field(
        name = "Usage",
        value = "`n!removewarn <@user> <warn reference>`",
        inline = False
    )
    try:
        await ctx.send(embed=embed)
    except Exception as e:
        await ctx.reply(f'```{e}```')

#CLEARWARNS_CMD
@help_command.command(name="clearwarns")
async def clearwarns_command(ctx):
    embed = discord.Embed(
        title = "Clearwarn Command",
        color = int(config["embed_color"], 16)
    )
    embed.add_field(
        name = "Description",
        value = "Clears all of the warning of the specified user.",
        inline = False
    )
    embed.add_field(
        name = "Usage",
        value = "`n!clearwarns <@user>`",
        inline = False
    )
    try:
        await ctx.send(embed=embed)
    except Exception as e:
        await ctx.reply(f'```{e}```')
        
#KICK_CMD
@help_command.command(name="kick")
async def kick_command(ctx):
    embed = discord.Embed(
        title = "Kick Command",
        color = int(config["embed_color"], 16)
    )
    embed.add_field(
        name = "Description",
        value = "Kicks the specified user out of the server.",
        inline = False
    )
    embed.add_field(
        name = "Usage",
        value = "`n!kick <@user> <optional reason>`",
        inline = False
    )
    try:
        await ctx.send(embed=embed)
    except Exception as e:
        await ctx.reply(f'```{e}```')

#SOFTBAN_CMD
@help_command.command(name="softban")
async def softban_command(ctx):
    embed = discord.Embed(
        title = "Softban Command",
        color = int(config["embed_color"], 16)
    )
    embed.add_field(
        name = "Description",
        value = "Kicks the specified user and deletes all of their messages on the server.",
        inline = False
    )
    embed.add_field(
        name = "Usage",
        value = "`n!softban <@user> <optional reason>`",
        inline = False
    )
    try:
        await ctx.send(embed=embed)
    except Exception as e:
        await ctx.reply(f'```{e}```')

#BAN_CMD
@help_command.command(name="ban")
async def ban_command(ctx):
    embed = discord.Embed(
        title = "Ban Command",
        color = int(config["embed_color"], 16)
    )
    embed.add_field(
        name = "Description",
        value = "Bans the specified user on the server.",
        inline = False
    )
    embed.add_field(
        name = "Usage",
        value = "`n!ban <@user> <reason>`",
        inline = False
    )
    try:
        await ctx.send(embed=embed)
    except Exception as e:
        await ctx.reply(f'```{e}```')

#UNBAN_CMD
@help_command.command(name="unban")
async def unban_command(ctx):
    embed = discord.Embed(
        title = "Unban Command",
        color = int(config["embed_color"], 16)
    )
    embed.add_field(
        name = "Description",
        value = "Unbans the specified user id on the server.",
        inline = False
    )
    embed.add_field(
        name = "Usage",
        value = "`n!unban <user id>`",
        inline = False
    )
    try:
        await ctx.send(embed=embed)
    except Exception as e:
        await ctx.reply(f'```{e}```')

#EMAIL_CMD
@help_command.command(name="email")
async def email_command(ctx):
    embed = discord.Embed(
        title = "Email Command (UNAVAILABLE)",
        color = int(config["embed_color"], 16)
    )
    embed.add_field(
        name = "Description",
        value = "This command is used when unbanning users to notify them. You will be asked with some questions which regards to the email.",
        inline = False
    )
    embed.add_field(
        name = "Usage",
        value = "`n!email`",
        inline = False
    )
    try:
        await ctx.send(embed=embed)
    except Exception as e:
        await ctx.reply(f'```{e}```')
















bot.run(os.environ.get('TOKEN'))
