import discord
from discord.ext import commands
import json

with open('config.json', 'r') as f:
    config = json.load(f)

class Ban(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ban')
    @commands.has_permissions(ban_members=True)
    async def ban_cmd(self, ctx, member: discord.Member, *, reason=None):
        try:
            if reason == None:
                return await ctx.reply('You cannot ban anyone without a reason.')
            
            ban_embed = discord.Embed(
                title = "❗ User Notice",
                description = "You have been banned from Nocturnal",
                color = int(config['embed_color'], 16)
            )
            ban_embed.add_field(
                name = "Reason",
                value = f"- {reason}",
                inline = False
            )
            ban_embed.add_field(
                name = "Responsible moderator",
                value = f"- {ctx.author}",
                inline = False
            )
            ban_embed.add_field(
                name = "Your user ID",
                value = f"- {member.id}\n\nIf you wish to appeal, you can use the informations above and fill up this [appeal form](https://docs.google.com/forms/d/e/1FAIpQLSc5oYS2ZZi1ZwhyEVlAvidin_54gDvvWOUyj2CZqIYG1BHZkw/viewform).",
                inline = False
            )
            
            await member.send(embed=ban_embed)
            await member.ban(reason=f'{ctx.author} - {reason}')
            await ctx.send(embed=discord.Embed(
                title = f"{member} was banned from the server",
                color = int(config['embed_color'], 16)
            ))
        except Exception as e:
            await ctx.reply(f"```{e}```")

def setup(bot):
    bot.add_cog(Ban(bot))
