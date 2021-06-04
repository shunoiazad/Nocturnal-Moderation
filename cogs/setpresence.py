import discord
from discord.ext import commands
import json

with open('config.json', 'r') as f:
    config = json.load(f)

class Setpresence(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='setpresence')
    @commands.is_owner()
    async def setpresence_cmd(self, ctx, status: discord.Status=discord.Status.online, *, activity: discord.Game=None):
        try:
            await self.bot.change_presence(
                status = status,
                activity = activity
            )
            await ctx.reply('Presence successfully set.')
        except Exception as e:
            await ctx.reply(f"```{e}```")

def setup(bot):
    bot.add_cog(Setpresence(bot))
