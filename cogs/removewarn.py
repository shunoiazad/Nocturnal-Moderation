import discord
from discord.ext import commands
import json
import datetime
import pytz
import asyncio
from RandomWordGenerator import RandomWord

with open('config.json', 'r') as f:
    config = json.load(f)

class Removewarn(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='removewarn')
    @commands.has_permissions(kick_members=True)
    async def removewarn_cmd(self, ctx, member: discord.Member, warn_ref: str):
        try:
            if discord.utils.find(lambda r: r.id == 819195059505332255, ctx.guild.roles) in ctx.author.roles:
                await register_user(member)
                data = await get_data()
                await remove_warn(member, warn_ref)
                available_references = []
                for warning in data[str(member.id)]:
                    available_references.append(warning["Reference"])
                if warn_ref in available_references:
                    return await ctx.reply("Successfully removed a warn from **{}**".format(member))
                else:
                    await ctx.reply("**{}** is not a valid reference".format(warn_ref))
            else:
                await ctx.reply("You don't have permission to use this command.")
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
    bot.add_cog(Removewarn(bot))
