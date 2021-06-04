import discord
from discord.ext import commands
import json
import datetime
import pytz
import asyncio
from RandomWordGenerator import RandomWord

with open('config.json', 'r') as f:
    config = json.load(f)

class Warn(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='warn')
    @commands.has_permissions(kick_members=True)
    async def warn_cmd(self, ctx, member: discord.Member, *, reason):
        try:
            await register_user(member)
            await add_warn(member, reason, str(ctx.author))
            await ctx.send(
                embed = discord.Embed(
                    title = "{} has been warned".format(member),
                    color = int(config["embed_color"], 16)
                )
            )
            
            warn_embed = discord.Embed(
                title = "❗ User Notice",
                description = "You have been warned in Nocturnal",
                color = int(config["embed_color"], 16)
            )
            warn_embed.add_field(
                name = "Reason",
                value = f"- {reason}",
                inline = False
            )
            warn_embed.add_field(
                name = "Responsible moderator",
                value = f"- {ctx.author}",
                inline = False
            )
            await member.send(embed=warn_embed)
        except Exception as e:
            await ctx.reply(f"```{e}```")





#generate warn reference
async def gen_warn_reference():
    warn_ref: str = RandomWord(max_word_size=30).generate()
    return warn_ref

#helper functions
#add warn
async def add_warn(user, reason, moderator):
    warnings = await get_data()
    warn_ref = await gen_warn_reference()

    set = {
        "Reason": reason,
        "Moderator": moderator,
        "Reference": warn_ref,
        "Time": datetime.datetime.now(tz=pytz.UTC).astimezone(pytz.timezone('Asia/Manila')).strftime("%B %d, %Y - %I:%M %p")
    }
    warnings[str(user.id)].append(set)

    await update_database(warnings, config['warn_database'])

#remove warn
async def remove_warn(user, warn_ref):
    warnings = await get_data()

    for i, warning in enumerate(warnings[str(user.id)]):
        if warning["Reference"] == warn_ref:
            warnings[str(user.id)].pop(i)

    await update_database(warnings, config['warn_database'])

#clear warn
async def clear_warn(user):
    warnings = await get_data()

    warnings[str(user.id)] = []

    await update_database(warnings, config['warn_database'])






#register
async def register_user(user):
    data = await get_data()
    
    if str(user.id) in data:
        return

    else:
        data[str(user.id)] = []
    
    await update_database(data, config['warn_database'])

#get data
async def get_data():
    with open(config['warn_database'], "r") as f:
        data = json.load(f)
    return data

#update database
async def update_database(object, database):
    with open(config['warn_database'], "w") as database:
        json.dump(object, database)

def setup(bot):
    bot.add_cog(Warn(bot))
