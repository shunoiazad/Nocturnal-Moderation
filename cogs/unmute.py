import discord
from discord.ext import commands
import json

with open('config.json', 'r') as f:
    config = json.load(f)

class Unmute(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='unmute')
    @commands.has_permissions(manage_roles=True)
    async def unmute_cmd(self, ctx, member: discord.Member):
        try:
            muted_role = discord.utils.find(lambda r: r.id == config['muted_role'], ctx.guild.roles)
            
            if not muted_role in member.roles:
                await ctx.reply(f'This user is not even muted.')
            else:
                await member.remove_roles(muted_role)
                await ctx.send(
                    embed = discord.Embed(
                        title = f'{member} is no longer muted',
                        color = int(config['embed_color'], 16)
                    )
                )
        except Exception as e:
            await ctx.reply(f"```{e}```")

def setup(bot):
    bot.add_cog(Unmute(bot))
