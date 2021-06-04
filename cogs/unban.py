import discord
from discord.ext import commands
import json

with open('config.json', 'r') as f:
    config = json.load(f)

class Unban(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='unban')
    @commands.has_permissions(ban_members=True)
    async def unban_cmd(self, ctx, userid):
        try:
            banned_users = await ctx.guild.bans()

            for banned in banned_users:
                user = banned.user
                if user.id == int(userid):
                    await ctx.guild.unban(user)
                    await ctx.send(embed=discord.Embed(
                        title = f'{user} is no longer banned',
                        color = int(config['embed_color'], 16)
                    ))
                    return
            
            await ctx.reply('I can\'t find this user.')
        except Exception as e:
            await ctx.reply(f"```{e}```")

def setup(bot):
    bot.add_cog(Unban(bot))
