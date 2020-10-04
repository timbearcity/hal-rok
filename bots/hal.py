import logging

import discord
from discord.ext import commands
import wikipedia

from secrets import TOKEN


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
        await message.add_reaction(u'\U0001F95B') # Glass of milk emoji

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

@bot.command()
async def roles(ctx):
    roles = [role.name for role in ctx.author.roles[1:]]
    roles = ', '.join(roles)
    await ctx.send(f"{ctx.message.author.mention} Your roles are: {roles}")


@bot.command()
@commands.has_role(703282083040198666) # R4
async def arkadd(ctx):
    aoo_role = discord.utils.get(ctx.guild.roles, id=762324577824669756)
    bot_role = discord.utils.get(ctx.guild.roles, id=756897839732490371)
    for mention in ctx.message.mentions:
        if aoo_role not in mention.roles and bot_role not in mention.roles:
            await mention.add_roles(aoo_role)


@bot.command()
@commands.has_role(703282083040198666) # R4
async def arkclear(ctx):
    aoo_role = discord.utils.get(ctx.guild.roles, id=762324577824669756)
    for member in aoo_role.members:
        await member.remove_roles(aoo_role)


@bot.command()
async def wiki(ctx, *args):
    await ctx.send(f"https://en.wikipedia.org/wiki/{'_'.join(args)}")


@bot.command()
async def wikiception(ctx, *args):
    args = list(args)
    depth = 0
    if args[-1].isdigit():
        depth = int(args.pop())
    article = wikipedia.page(' '.join(args))
    results = [article.title]
    if depth > 0:
        for _ in range(depth):
            article = wikipedia.page(article.links[0])
            results.append(article.title)
    await ctx.send(f"{' > '.join(results)}\n{article.url}")


bot.run(TOKEN)
