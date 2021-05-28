import discord
from discord.ext import commands
import asyncio
import smtplib
from email.message import EmailMessage
import os

class Email_Command(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 20, commands.BucketType.user)
    @commands.has_permissions(ban_members=True)
    async def email(self, ctx):
        recipient_email_address = None
        account_status = None
        receive_reply = None
        moderator_message = None

        def check(m):
            return m.author.id == ctx.author.id and m.channel.id == ctx.channel.id

        await ctx.message.reply("Please type the email you wanted to send email to.")
        try:
            response1 = await self.bot.wait_for("message", check=check, timeout=20)
            if response1.content.endswith("@gmail.com"):
                recipient_email_address = response1.content
                await response1.reply("What is the account's status? It can either be **Unbanned** or **Retained**.")
                try:
                    response2 = await self.bot.wait_for("message", check=check, timeout=20)
                    if response2.content.lower() == "unbanned":
                        account_status = "Unbanned"
                    elif response2.content.lower() == "retained":
                        account_status = "Retained"
                    else:
                        response2.reply("Your choices can only be either one of the two, **Unbanned** or **Retained**.")
                        return
                    await response2.reply("Should this email recieve a reply? **Yes** or **No**.")
                    try:
                        response3 = await self.bot.wait_for("message", check=check, timeout=20)
                        if response3.content.lower() == "yes":
                            receive_reply = True
                        elif response3.content.lower() == "no":
                            receive_reply = False
                        else:
                            response3.reply("Your choices can only be either one of the two, **Yes** or **No**.")
                            return
                        await response3.reply("What would be your message in this email?")
                        try:
                            response4 = await self.bot.wait_for("message", check=check, timeout=20)
                            moderator_message = response4.content

                            await ctx.send(f"**Email:** {recipient_email_address}\n**Status:** {account_status}\n**Receive Reply:** {receive_reply}\n**Moderator Message:** {moderator_message}")
                            await ctx.send("Type **send** to send the email and **cancel** to cancel.")
                            try:
                                response5 = await self.bot.wait_for("message", check=check, timeout=20)
                                if response5.content.lower() == "send":
                                    await ctx.send("The email is now being sent to the recipient...")

                                    if receive_reply == True:
                                        host = "smtp.gmail.com"
                                        port = 587
                                        my_email_address = os.getenv("EMAIL_USER")
                                        my_email_password = os.getenv("EMAIL_PASS")

                                        msg = EmailMessage()
                                        msg["Subject"] = "User Status"
                                        msg["From"] = my_email_address
                                        msg["To"] = recipient_email_address
                                        msg.add_alternative(f"""\
                                    <!DOCTYPE html>
                                    <html>
                                        <body>
                                            <p style="font-family:Times New Roman;">Hello there,</p>


                                            <p style="font-family:Times New Roman;">We thank you for responding or providing us information so that we can clarify if it is possible for us to help you, regarding your status in <a href='https://discord.gg/WJtxeARRrV'><b>Nocturnal</b></a>.</p>


                                            <p style="font-family:Times New Roman;"><b>Your status:</b> {account_status}<br>
                                            <b>Moderator message:</b> {moderator_message}</p>


                                            <p style="font-family:Times New Roman;"><b>We will be expecting for your reply in this email.</b></p><br>




                                            <p style="color:#3e006f; font-family:Times New Roman;">Sincerely,<br>
                                            {ctx.author.name}<br>
                                            Nocturnal Support & Moderation</p>
                                        </body>
                                    </html>
                                    """, subtype='html')

                                        with smtplib.SMTP(host, port) as smtp:
                                            smtp.ehlo()
                                            smtp.starttls()
                                            smtp.ehlo()
                                            smtp.login(my_email_address, my_email_password)
                                            smtp.send_message(msg)
                                            await ctx.send(f"Successfully sent email to **{recipient_email_address}**")
                                            return



                                    else:
                                        host = "smtp.gmail.com"
                                        port = 587
                                        my_email_address = os.getenv("EMAIL_USER")
                                        my_email_password = os.getenv("EMAIL_PASS")

                                        msg = EmailMessage()
                                        msg["Subject"] = "User Status"
                                        msg["From"] = my_email_address
                                        msg["To"] = recipient_email_address
                                        msg.add_alternative(f"""\
                                    <!DOCTYPE html>
                                    <html>
                                        <body>
                                            <p style="font-family:Times New Roman;">Hello there,</p>


                                            <p style="font-family:Times New Roman;">We thank you for responding or providing us information so that we can clarify if it is possible for us to help you, regarding your status in <a href='https://discord.gg/WJtxeARRrV'><b>Nocturnal</b></a>.</p>


                                            <p style="font-family:Times New Roman;"><b>Your status:</b> {account_status}<br>
                                            <b>Moderator message:</b> {moderator_message}</p>


                                            <p style="font-family:Times New Roman;"><b>If you will reply to this email, do not expect to receive or hear any further from us.</b></p><br>




                                            <p style="color:#3e006f; font-family:Times New Roman;">Sincerely,<br>
                                            {ctx.author.name}<br>
                                            Nocturnal Support & Moderation</p>
                                        </body>
                                    </html>
                                    """, subtype='html')

                                        with smtplib.SMTP(host, port) as smtp:
                                            smtp.ehlo()
                                            smtp.starttls()
                                            smtp.ehlo()
                                            smtp.login(my_email_address, my_email_password)
                                            smtp.send_message(msg)
                                            await ctx.send(f"Successfully sent email to **{recipient_email_address}**")
                                            return





                                elif response5.content.lower() == "cancel":
                                    await ctx.send("Email canceled.")
                                else:
                                    response3.reply("Your choices can only be either one of the two, **Send** or **Cancel**.")
                                    return

                            except asyncio.TimeoutError:
                                await ctx.send("Prompt ended for not responding in 20 seconds.")
                                
                        except asyncio.TimeoutError:
                            await ctx.send("Prompt ended for not responding in 20 seconds.")

                    except asyncio.TimeoutError:
                        await ctx.send("Prompt ended for not responding in 20 seconds.")

                except asyncio.TimeoutError:
                    await ctx.send("Prompt ended for not responding in 20 seconds.")

            else:
                response1.reply("You must provide an email address")
                return

        except asyncio.TimeoutError:
            await ctx.send("Prompt ended for not responding in 20 seconds.")





    @commands.command()
    @commands.cooldown(1, 20, commands.BucketType.user)
    @commands.has_permissions(ban_members=True)
    async def timeout(self, ctx, email_address):
        await ctx.send("The email is now being sent to the recipient...")
        
        host = "smtp.gmail.com"
        port = 587
        my_email_address = os.getenv("EMAIL_USER")
        my_email_password = os.getenv("EMAIL_PASS")

        msg = EmailMessage()
        msg["Subject"] = "User Status"
        msg["From"] = my_email_address
        msg["To"] = email_address
        msg.add_alternative(f"""\
    <!DOCTYPE html>
    <html>
        <body>
            <p style="font-family:Times New Roman;">Hello there,</p>


            <p style="font-family:Times New Roman;"><b>We have not received any reply from you, hence, I will be closing this email prompt now.</b></p>


            <p style="font-family:Times New Roman;"><b>If you will reply to this email, do not expect to receive or hear any further from us.</b></p><br>




            <p style="color:#3e006f; font-family:Times New Roman;">Sincerely,<br>
            {ctx.author.name}<br>
            Nocturnal Support & Moderation</p>
        </body>
    </html>
    """, subtype='html')

        with smtplib.SMTP(host, port) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
            smtp.login(my_email_address, my_email_password)
            smtp.send_message(msg)
            await ctx.send(f"Successfully sent email to **{email_address}**")


def setup(bot):
    bot.add_cog(Email_Command(bot))
