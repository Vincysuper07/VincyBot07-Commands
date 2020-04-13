import discord
from discord.ext import commands

from core.paginator import EmbedPaginatorSession

class VincyBot07e(commands.Cog):
      def __init__(self, bot):
            self.bot = bot
            
      @commands.command(aliases=["argee","garee","agere","arege"])
      async def agree(self, ctx):
            """eh"""
            member = ctx.author
            role = discord.utils.find(lambda r: r.name == "Members",ctx.guild.roles)
            await member.add_roles(role)

      @commands.command(aliases=["status"])
      async def mcstatus(self, ctx):
            """Shows MC server's status."""
            response = await self.bot.session.get("http://vps.vincysuper07.cf/vincystatus/enapi.php")
            status = (await response.content.readline()).decode('UTF-8')
            embed = discord.Embed(title = "Minecraft Server: mc.Vincysuper07.cf", description = f"Right now the server is {status}")
            if status == "OFFLINE.":
                embed.color = discord.Color.red()
            else:
                embed.color = discord.Color.green()
            await ctx.send(embed=embed)
            
      @commands.command(aliases=["help"])
      async def commands(self,ctx):
            """Shows bot commands"""
            embed = discord.Embed(title="Tags", description=f"{ctx.prefix}tag <name> - With this command you can use a tag\n{ctx.prefix}tags add <name> <answer> - Adds a tag", color = discord.Color.green())
            embed1 = discord.Embed(title="Fun", description=f"{ctx.prefix}choose <first option> <second option> Choose between 2 options\n{ctx.prefix}roll - Roll a random number\n{ctx.prefix}flip - Flip a coin\n{ctx.prefix}rps - Play Rock, Paper, Scissors\n{ctx.prefix}8ball <question>? - Ask 8Ball a question\n{ctx.prefix}reverse <message> - !txeT ruoY esreveR\n{ctx.prefix}meme - Get a random meme\n{ctx.prefix}roast <someone> - Roast someone! If you suck at roasting them yourself\n{ctx.prefix}smallcaps <message> - ᴄᴏɴᴠᴇʀᴛ ʏᴏᴜʀ ᴛᴇxᴛ ᴛᴏ ꜱᴍᴀʟʟ ᴄᴀᴘꜱ!", color = discord.Color.green())
            embed2 = discord.Embed(title="Hastebin", description=f"{ctx.prefix}hastebin <message> - Makes a hastebin link with your message", color = discord.Color.green())
            embed3 = discord.Embed(title="Moderation", description=f"{ctx.prefix}purge <number> - Delete an amount of messages\n{ctx.prefix}kick <someone> - Kick someone\n{ctx.prefix}mute <someone> - Mute someone\n{ctx.prefix}unmute <someone> - Unmute someone\n{ctx.prefix}nuke - Delete **every** message in a channel\n{ctx.prefix}ban <someone> - Ban someone (this is permanent ban)\n{ctx.prefix}unban <someone> - Unban someone", color = discord.Color.green())
            embed4 = discord.Embed(title="Announcements", description=f"{ctx.prefix}announcement start - Make announcement\n{ctx.prefix}announcement quick <channel> [role] <message> - An old and faster way to make announcements", color = discord.Color.green())
            embed5 = discord.Embed(title="Music", description=f"{ctx.prefix}join - Joins a voice channel\n{ctx.prefix}leave - Leaves a voice channel\n{ctx.prefix}now - Shows the currently playing song\n{ctx.prefix}pause - Pauses a song\n{ctx.prefix}play <song> - Plays a song\n{ctx.prefix}queue - Shows the queue\n{ctx.prefix}remove - Removes a song from the queue\n{ctx.prefix}resume - Resumes a song currently paused\n{ctx.prefix}shuffle - Shuffles a song\n{ctx.prefix}skip - Skips a song\n{ctx.prefix}stop - Stops playing songs and clears the queue\n{ctx.prefix}summon - The same as v!play, enters in a voice channel\n{ctx.prefix}volume <volume> - Changes the player's volume", color=discord.Color.green())
            embed6 = discord.Embed(title="Other", description=f"{ctx.prefix}embed send <title> <Description> - Send an embed message\n{ctx.prefix}embed color <hexcode> - Change your embed message's color\n{ctx.prefix}reactionrole add <message_id> <role> <emoji> - Make a reaction role\n{ctx.prefix}status - Check Vincy's MC server's status\n{ctx.prefix}commands - Shows this message\n{ctx.prefix}help - Shows this message", color = discord.Color.green())
            embeds = []
            embed_list = [embed, embed1, embed2, embed3, embed4, embed5, embed6]
            for embed in embed_list:
                embed.set_footer(text=f"Use reaction to change page. • Prefix: {ctx.prefix}")
                embed.set_author(name="VincyBot07 1.1", icon_url="https://vincybot07.vincysuper07.cf/assets/images/immagine-VincyBot07-rotonda.png")
                embeds.append(embed)
            session = EmbedPaginatorSession(ctx, *embeds)
            await session.run()
            
def setup(bot):
      bot.add_cog(VincyBot07e(bot))
