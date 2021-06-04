import discord
from discord.ext import commands
import json

with open('config.json', 'r') as f:
    config = json.load(f)

class Kick(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='kick')
    @commands.has_permissions(kick_members=True)
    async def kick_cmd(self, ctx, member: discord.Member, *, reason=config['defaults']['kick_reason']):
        try:
            kick_embed = discord.Embed(
                title = "❗ User Notice",
                description = "You have been kicked from Nocturnal",
                color = int(config['embed_color'], 16)
            )
            kick_embed.add_field(
                name = "Reason",
                value = f"- {reason}",
                inline = False
            )
            kick_embed.add_field(
                name = "Responsible moderator",
                value = f"- {ctx.author}",
                inline = False
            )
            await member.send(embed=kick_embed)
            await member.kick(reason=reason)
            await ctx.send(embed=discord.Embed(
                title = f"{member} was kicked from the server",
                color = int(config['embed_color'], 16)
            ))
        except Exception as e:
            await ctx.reply(f"```{e}```")

def setup(bot):
    bot.add_cog(Kick(bot))
