# from os import listdir
# import re

# import discord
# from discord.ext import commands
# import unidecode


# class Commander(commands.Cog):
#     def __init__(self, bot):
#         self.bot = bot

#     @commands.command(aliases=['commander', 'talents', 'talent'])
#     async def commanders(self, ctx):
#         await ctx.send(f"{ctx.message.author.mention}\n{commanders}")

#     @commands.command()
#     async def commander(self, ctx, *args):
#         directory = f'images/{ctx.command}/'
#         try:
#             await ctx.send(file=discord.File(f'{directory}{args[0]}.jpg'))
#         except:
#             images = [img.split('.')[0] for img in listdir(f'{directory}')]
#             await ctx.send(f"```{ctx.prefix}{ctx.command}{ctx.command.aliases}{' '.join(images)}```")


# def setup(bot):
#     pattern = re.compile('[\W_]+')
#     for comm in commanderlist:
#         comm = unidecode.unidecode(comm).lower() # Transform text to ASCII
#         pattern.sub('', comm) # Remove non-alphanumeric characters
#         bot.add_command(commander)
#         commander.name = comm
