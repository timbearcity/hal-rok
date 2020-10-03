import logging

import discord

from secrets import TOKEN


logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='logs/discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s'))
logger.addHandler(handler)

client = discord.Client()

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if client.user in message.mentions:
        await message.add_reaction(u'\U0001F95B') # Glass of milk emoji
        #roles = [role.name for role in message.author.roles]
        #await message.channel.send(f"Your roles are {', '.join(roles)}")

    if message.author.id == 159985870458322944 and 'level' in message.content: #MEE6 bot ID
        member = message.mentions[1]
        level = int(message.content.split()[13][:-1])
        r2 = discord.utils.get(message.guild.roles, id=762010221669122048)
        r3 = discord.utils.get(message.guild.roles, id=762010219559518298)
        print(f"Message author: {message.author}")
        print(f"Target member: {member}")
        print(f"Target level: {level}")
        print(r2)
        print(r3)
        if 20 <= level < 30 and r2 not in member.roles:
            await member.add_roles(r2)

        if 30 <= level and r3 not in member.roles:
            await member.add_roles(r3)

client.run(TOKEN)
