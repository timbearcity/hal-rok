#!/usr/bin/env python

from random import randint
import os
import logging
import json
import glob

import discord
from discord.ext import commands
import wikipedia


# Logging
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='logs/discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s'))
logger.addHandler(handler)

# Instantiation of the bot client
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print("Logged in as {0.user}".format(bot))


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if bot.user in message.mentions:
        await message.add_reaction(u'\U0001F95B') # If bot is mentioned, react with a glass of milk emoji

    # Bot gives members R2 if level 20 is reached and R3 is level 30 is reached
    if message.author.id == 159985870458322944 and 'level' in message.content: # MEE6 bot ID
        member = message.mentions[1]
        level = int(message.content.split()[13][:-1])
        r2 = discord.utils.get(message.guild.roles, id=762010221669122048)
        r3 = discord.utils.get(message.guild.roles, id=762010219559518298)
        if 20 <= level and r2 not in member.roles:
            await member.add_roles(r2)

        if 30 <= level and r3 not in member.roles:
            await member.add_roles(r3)

    await bot.process_commands(message)


# Commands
@bot.command(aliases=['role'], description="Returns all your roles.")
async def roles(ctx):
    roles = [role.name for role in ctx.author.roles[1:]]
    roles = ', '.join(roles)
    await ctx.send(f"{ctx.message.author.mention} Your roles are: {roles}")


@bot.command(category="R4", description="Gives all mentioned members the Osiris Combatant role.")
@commands.has_role(703282083040198666) # R4
async def arkadd(ctx):
    aoo_role = discord.utils.get(ctx.guild.roles, id=762324577824669756)
    bot_role = discord.utils.get(ctx.guild.roles, id=756897839732490371)
    for mention in ctx.message.mentions:
        if aoo_role not in mention.roles and bot_role not in mention.roles:
            await mention.add_roles(aoo_role)


@bot.command(category="R4", description="Removes the Osiris Combatant role from all members.")
@commands.has_role(703282083040198666) # R4
async def arkclear(ctx):
    aoo_role = discord.utils.get(ctx.guild.roles, id=762324577824669756)
    for member in aoo_role.members:
        await member.remove_roles(aoo_role)


@bot.command(description="Returns the requested Wikipedia article")
async def wiki(ctx, *args):
    await ctx.send(f"https://en.wikipedia.org/wiki/{'_'.join(args)}")


@bot.command(aliases=['wc'], description="Returns the requested Wikipedia article. If the keyword is followed by a number it will return a new article that many links deep from the origin article.")
async def wikiception(ctx, *args):
    args = list(args)
    depth = 0
    if args[-1].isdigit():
        depth = int(args.pop())
    article = wikipedia.page(' '.join(args))
    results = [article.title]
    if depth > 0:
        for _ in range(depth):
            article = wikipedia.page(article.links[randint(0, len(article.links)-1)])
            results.append(article.title)
    await ctx.send(f"{' > '.join(results)}\n{article.url}")


@bot.command(description="Who am I?")
async def whoami(ctx):
    await ctx.send(f"I know life can be tough and we all go through identity crises at times. However, you'll be pleased to know that you're {ctx.message.author.mention}.")


@bot.command(aliases=['leaderboards', 'top', 'toplist', 'leader', 'leaders'])
async def leaderboard(ctx):
    await ctx.send("https://mee6.xyz/leaderboard/703247278776778842")


# A command for each commander to return an image of possible talent builds
with open('files/commanders.json', 'r') as f:
    data = json.load(f)

for commander in data:
    @bot.command(name=commander, aliases=data[commander]['aliases'], description=data[commander]['name'])
    async def _commander(ctx, *args):
        directory = f'images/{ctx.command}/'
        try:
            await ctx.send(file=discord.File(glob.glob(os.path.join(directory, args[0] + '.*'))[0]))
        except:
            images = [img.split('.')[0] for img in os.listdir(directory)]
            await ctx.send(f"```python\n{ctx.command.description} - Available talent builds\n{ctx.prefix}{ctx.command}{ctx.command.aliases} {' '.join(images)}```")


bot.run(os.getenv("DISCORD_TOKEN"))
