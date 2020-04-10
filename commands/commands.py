import discord
from discord.ext import commands

from core.paginator import EmbedPaginatorSession

class VincyBot07e(commands.Cog):
      def __init__(self, bot):
            self.bot = bot
            
      @commands.command(aliases=["accetot"])
      async def accetto(self, ctx):
            """<#595319716344758291>"""
            member = ctx.author
            role = discord.utils.find(lambda r: r.name == "Membri",ctx.guild.roles)
            await member.add_roles(role)

      @commands.command(aliases=["stato"])
      async def statomc(self, ctx):
            """Mostra lo stato del server Minecraft."""
            response = await self.bot.session.get("http://vps.vincysuper07.cf/vincystatus/api.php")
            status = (await response.content.readline()).decode('UTF-8')
            embed = discord.Embed(title = "Server Minecraft: mc.Vincysuper07.cf", description = f"Al momento il server è {status}")
            if status == "OFFLINE":
                embed.color = discord.Color.red()
            else:
                embed.color = discord.Color.green()
            await ctx.send(embed=embed)
            
      @commands.command(aliases=["help"])
      async def comandi(self,ctx):
            """Mostra i comandi del bot"""
            embed = discord.Embed(title="Tags", description=f"{ctx.prefix}tag <name> - With this command you can use a tag\n{ctx.prefix}tags add <name> <answer> - Adds a tag", color = discord.Color.green())
            embed1 = discord.Embed(title="Fun", description=f"{ctx.prefix}choose <primo oggetto> <secondo oggetto> Chooses between 2 options\n{ctx.prefix}roll - Roll a random number\n{ctx.prefix}flip - Lancia una moneta\n{ctx.prefix}rps - Sasso, Carta, o Forbici?\n{ctx.prefix}8ball <domanda>? - La 8Ball risponderà a ogni tua domanda!\n{ctx.prefix}reverse <messaggio> - !otseT out li etrevnI\n{ctx.prefix}meme - Ti da una meme a caso\n{ctx.prefix}roast <persona> - Insulta la persona menzionata\n{ctx.prefix}smallcaps <messaggio> - ᴄᴏɴᴠᴇʀᴛᴇ ɪʟ ᴛᴜᴏ ᴛᴇꜱᴛᴏ ᴀ ᴜɴ ᴍᴀɪᴜꜱᴄᴏʟᴏ ᴘɪᴄᴄᴏʟᴏ!", color = discord.Color.green())
            embed2 = discord.Embed(title="Hastebin", description=f"{ctx.prefix}hastebin <messaggio> - Makes a hastebin link with your message", color = discord.Color.green()
            embed3 = discord.Embed(title="Moderation", description=f"{ctx.prefix}purge <numero> - Elimina una quantità da 1 a 100 di messaggi\n{ctx.prefix}kick <persona> - Espelle un membro del server\n{ctx.prefix}mute <persona> - Muta una persona nel server\n{ctx.prefix}unmute <persona> - Smuta una persona nel server\n{ctx.prefix}nuke - Eimina tutti i messaggi di una chat\n{ctx.prefix}ban <persona> - Banna una persona dal server\n{ctx.prefix}unban <persona> - Revoca il ban a una persona del server", color = discord.Color.green())
            embed4 = discord.Embed(title="Announcements", description=f"{ctx.prefix}announcement start - crea un annuncio interattivo\n{ctx.prefix}announcement quick <canale> [ruolo] <messaggio> - Un vecchio modo per creare un'annuncio", color = discord.Color.green())
            embed5 = discord.Embed(title="Other", description=f"{ctx.prefix}embed send <titolo> <Descrizione> - Invia un messaggio incorporato\n{ctx.prefix}embed color <hexcode> - Cambia il colore del tuo messaggio incorporato\n{ctx.prefix}welcomer <chat> <messaggio> - Crea un messaggio di benvenuto!\n{ctx.prefix}reactionrole add <id_messaggio> <ruolo> <emoji> - Inserisce una reazione ad un messaggio, che servirà per ricevere un ruolo!\n{ctx.prefix}stato - Controlla se il server Minecraft di Vincy è online!\n{ctx.prefix}comandi - Mostra questo messaggio!\n{ctx.prefix}help - Mostra questo messaggio!", color = discord.Color.green())
            embeds = []
            embed_list = [embed, embed1, embed2, embed3, embed4, embed5]
            for embed in embed_list:
                embed.set_footer(text=f"Usa le frecce per cambiare pagina. • Prefix: {ctx.prefix}")
                embed.set_author(name="VincyBot07 1.1", icon_url="https://vincybot07.vincysuper07.cf/assets/images/immagine-VincyBot07-rotonda.png")
                embeds.append(embed)
            session = EmbedPaginatorSession(ctx, *embeds)
            await session.run()
            
def setup(bot):
      bot.add_cog(VincyBot07e(bot))
