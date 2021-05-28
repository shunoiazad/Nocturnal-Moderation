import discord
from discord.ext import commands
from RandomWordGenerator import RandomWord
import json
import datetime
import pytz
import asyncio

warn_database = "databases/warnings.json"
embed_color = 0x616060

class Warn(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def warnings(self, ctx, member: discord.Member = None):
        if member == None:
            member = ctx.author
        
        await register_user(member)
        warns = await get_data()
        
        if warns[str(member.id)] == []:
            embed = discord.Embed(
                title = "Warnings for {}".format(member),
                description = "There are no warnings",
                color = embed_color
            )
            await ctx.send(embed=embed)
        
        else:
            embed = discord.Embed(
                title = "Warnings for {}".format(member),
                color = embed_color
            )
            for warn in warns[str(member.id)]:
                embed.add_field(
                    name = warn['Time'],
                    value = f"**Reason:** {warn['Reason']}\n**Moderator:** {warn['Moderator']}\n**Warn Reference:** {warn['Reference']}",
                    inline = False
                )
            await ctx.send(embed=embed)



    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def warn(self, ctx, member: discord.Member, *, reason):
        await register_user(member)
        await add_warn(member, reason, str(ctx.author))
        await ctx.send(
            embed = discord.Embed(
                title = "{} has been warned".format(member),
                color = embed_color
            )
        )
        
        warn_embed = discord.Embed(
            title = "❗ Notifier",
            description = "You were warned in Nocturnal",
            color = embed_color
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

    

    @commands.command(aliases=['delwarn'])
    @commands.has_permissions(kick_members=True)
    async def removewarn(self, ctx, member: discord.Member, warn_ref: str):
        await register_user(member)
        data = await get_data()
        await remove_warn(member, warn_ref)
        available_references = []
        for warning in data[str(member.id)]:
            available_references.append(warning["Reference"])
        if warn_ref in available_references:
            return await ctx.send("{} Successfully removed a warn from **{}**".format(ctx.author.mention, member))
        else:
            await ctx.send("{} **{}** is not a valid reference!".format(ctx.author.mention, warn_ref))


    @commands.command(aliases=['clearwarns'])
    @commands.has_permissions(kick_members=True)
    async def clearwarn(self, ctx, member: discord.Member):
        await register_user(member)
        warns = await get_data()
        await clear_warn(member)
        if len(warns[str(member.id)]) == 0:
            return await ctx.send("{} **{}** doesn't even have a single warn lol".format(ctx.author.mention, member))

        if len(warns[str(member.id)]) == 1:
            await ctx.send("{} Successfully cleared **{}** warning from **{}**".format(ctx.author.mention, len(warns[str(member.id)]), member))

        else:
            await ctx.send("{} Successfully cleared **{}** warnings from **{}**".format(ctx.author.mention, len(warns[str(member.id)]), member))
































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

    await update_database(warnings, warn_database)

#remove warn
async def remove_warn(user, warn_ref):
    warnings = await get_data()

    for i, warning in enumerate(warnings[str(user.id)]):
        if warning["Reference"] == warn_ref:
            warnings[str(user.id)].pop(i)

    await update_database(warnings, warn_database)

#clear warn
async def clear_warn(user):
    warnings = await get_data()

    warnings[str(user.id)] = []

    await update_database(warnings, warn_database)






#register
async def register_user(user):
    data = await get_data()
    
    if str(user.id) in data:
        return

    else:
        data[str(user.id)] = []
    
    await update_database(data, warn_database)

#get data
async def get_data():
    with open(warn_database, "r") as f:
        data = json.load(f)
    return data

#update database
async def update_database(object, database):
    with open(warn_database, "w") as database:
        json.dump(object, database)


def setup(bot):
    bot.add_cog(Warn(bot))
