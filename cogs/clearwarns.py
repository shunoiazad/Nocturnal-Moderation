import discord
from discord.ext import commands
import json
import datetime
import pytz
import asyncio
from RandomWordGenerator import RandomWord

with open('config.json', 'r') as f:
    config = json.load(f)

class Clearwarns(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='clearwarns')
    @commands.has_permissions(kick_members=True)
    async def clearwarns_cmd(self, ctx, member: discord.Member):
        try:
            def check(m):
                return m.author.id == ctx.author.id and m.channel.id == ctx.channel.id
            await register_user(member)
            warns = await get_data()

            if discord.utils.find(lambda r: r.id == 819195059505332255, ctx.guild.roles) in ctx.author.roles:
                if len(warns[str(member.id)]) == 0:
                    return await ctx.send("{} **{}** doesn't even have a single warn.".format(ctx.author.mention, member))
                else:
                    await ctx.reply("Are you sure you want to clear all warnings from this user? Reply with **YES** if so and **NO** if not.")
                    try:
                        response = await self.bot.wait_for("message", check=check, timeout=20)
                        if response.content.lower() == "yes":
                            await clear_warn(member)
                    
                            if len(warns[str(member.id)]) == 1:
                                await ctx.send("{} Successfully cleared **{}** warning from **{}**.".format(ctx.author.mention, len(warns[str(member.id)]), member))
                    
                            else:
                                await ctx.send("{} Successfully cleared **{}** warnings from **{}**.".format(ctx.author.mention, len(warns[str(member.id)]), member))
                        elif response.content.lower() == "no":
                            await response.add_reaction("✅")
                            return
                        else:
                            await response.reply(f"**{response.content}** is not a valid option.")
                            return
                    except asyncio.TimeoutError:
                        await ctx.send("Prompt ended for not responding in 20 seconds.")
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
    bot.add_cog(Clearwarns(bot))
