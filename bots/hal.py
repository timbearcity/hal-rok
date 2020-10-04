import logging

import discord
from discord.ext import commands

from secrets import TOKEN


# Logging
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='logs/discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s'))
logger.addHandler(handler)

# Instantiation of the bot client
bot = commands.Bot(command_prefix='!')

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


#@bot.command()
#async def 


bot.run(TOKEN)
