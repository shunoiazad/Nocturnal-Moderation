import discord
from discord.ext import commands
import json

with open('config.json', 'r') as f:
    config = json.load(f)

class Purge(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='purge')
    @commands.has_permissions(manage_messages=True)
    async def purge_cmd(self, ctx, amount: int=config['defaults']['purge_amount'], channel: discord.TextChannel=config['defaults']['purge_channel']):
        try:
            if channel == None:
                channel = ctx.channel
                await channel.purge(limit=(amount + 1))
            else:
                await channel.purge(limit=amount)
                await ctx.message.add_reaction('✅')
        except Exception as e:
            await ctx.reply(f"```{e}```")

def setup(bot):
    bot.add_cog(Purge(bot))
