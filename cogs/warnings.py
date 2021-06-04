import discord
from discord.ext import commands
import json
import datetime
import pytz
import asyncio
from RandomWordGenerator import RandomWord

with open('config.json', 'r') as f:
    config = json.load(f)

class Warnings(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='warnings')
    @commands.has_permissions(kick_members=True)
    async def warnings_cmd(self, ctx, member: discord.Member=None):
        try:
            if member == None:
                member = ctx.author
            
            await register_user(member)
            warns = await get_data()
            
            if warns[str(member.id)] == []:
                embed = discord.Embed(
                    title = "Warnings for {}".format(member),
                    description = "There are no warnings",
                    color = int(config["embed_color"], 16)
                )
                await ctx.send(embed=embed)
            
            else:
                embed = discord.Embed(
                    title = "Warnings for {}".format(member),
                    color = int(config["embed_color"], 16)
                )
                for warn in warns[str(member.id)]:
                    embed.add_field(
                        name = warn['Time'],
                        value = f"**Reason:** {warn['Reason']}\n**Moderator:** {warn['Moderator']}\n**Warn Reference:** {warn['Reference']}",
                        inline = False
                    )
                await ctx.send(embed=embed)
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
    bot.add_cog(Warnings(bot))
