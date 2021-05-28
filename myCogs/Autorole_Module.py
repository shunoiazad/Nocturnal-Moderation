import discord
from discord.ext import commands
from random import choice

class Autorole_Module(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_member_join(self, member):
        guild = self.bot.get_guild(819194655999524914)
        team_roles = [discord.utils.find(lambda r: r.id == 819196301689225236, guild.roles), discord.utils.find(lambda r: r.id == 819196195666788363, guild.roles)]
        confirmationRole = discord.utils.find(lambda r: r.id == 827075812050206720, guild.roles)
        
        await member.add_roles(choice(team_roles))
        await member.add_roles(confirmationRole)
        
def setup(bot):
    bot.add_cog(Autorole_Module(bot))
