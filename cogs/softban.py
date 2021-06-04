import discord
from discord.ext import commands
import json

with open('config.json', 'r') as f:
    config = json.load(f)

class Softban(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='softban')
    @commands.has_permissions(kick_members=True)
    async def softban_cmd(self, ctx, member: discord.Member, *, reason=config['defaults']['softban_reason']):
        try:
            kick_embed = discord.Embed(
                title = "❗ User Notice",
                description = "You were softbanned from Nocturnal",
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
            await member.ban(reason=f"{ctx.author} (Softban) - {reason}")
            await member.unban(reason=f"{ctx.author} {Softban} - Softban")
            await ctx.send(embed=discord.Embed(
                title = f"{member} was kicked from the server",
                color = int(config['embed_color'], 16)
            ))
        except Exception as e:
            await ctx.reply(f"```{e}```")

def setup(bot):
    bot.add_cog(Softban(bot))
