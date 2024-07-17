import discord
import json
from module.myconfig import myconfig

intents = discord.Intents.all()
intents.message_content = True
intents.members = True
client = discord.Client(intents=intents)













config = myconfig()
config.load("config.json")


@client.event
async def on_ready():
    print('====================================')
    print(f'We have logged in as {client.user}.')
    print('This bot is on ready.')
    print('====================================')
    return

@client.event
async def on_member_join(member):
    channel = client.get_channel(config.joinchannel)
    await channel.send(content=config.joinmessage["message"],embed=discord.Embed.from_dict(config.joinmessage["embed"]))
    return

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.channel.type == discord.ChannelType.private:
        guild = client.get_guild(config.serverid)
        channels = [str(guild.channels[i].name) for i in range(len(guild.channels))]
        if str(message.author.id) not in channels:
            print(message.author.id)
            print(channels)
            category = guild.get_channel(1238310718168629328)
            await category.create_text_channel(message.author.id)
        channel = 
        await 
        return
    if message.content.startswith(config.prefix):
        commands = message.content.split()
        if commands[0] == config.prefix + "help":
            if commands[1] == "send":
                await message.channel.send(content=config.helpmessage["message"],embed=discord.Embed.from_dict(config.helpmessage["embed"]))
            elif commands[1] == "edit":
                if commands[2] == "message":
                    config.helpmessage["message"] = commands[3]
                elif commands[2] == "embed":
                    config.helpmessage["embed"] = json.loads(message.content[(len(commands[0])+len(commands[1])+len(commands[2])+3):][3:-3])
                await message.channel.send("edit successed")
                await message.channel.send(config.helpmessage)
                config.save("config.json")
        elif commands[0] == config.prefix + "config":
            if commands[1] == "guidechannel":
                config.guidechannel = int(commands[2])
                config.save("config.json")
            elif commands[1] == "helpchannel":
                config.helpchannel = int(commands[2])
                config.save("config.json")
            elif commands[1] == "joinchannel":
                config.joinchannel = int(commands[2])
                config.save("config.json")
            elif commands[1] == "prefix":
                config.prefix = commands[2]
                config.save("config.json")
            elif commands[1] == "username":
                config.username = commands[2]
                config.save("config.json")
            elif commands[1] == "serverid":
                config.serverid = int(commands[2])
                config.save("config.json")
            await message.channel.send("edit successed")
        elif commands[0] == config.prefix + "guide":
            if commands[1] == "send":
                channel = client.get_channel(config.guidechannel)
                await channel.send(content=config.guidemessage["message"],embed=discord.Embed.from_dict(config.guidemessage["embed"]))
            elif commands[1] == "edit":
                if commands[2] == "message":
                    config.guidemessage["message"] = commands[3]
                elif commands[2] == "embed":
                    config.guidemessage["embed"] = json.loads(message.content[(len(commands[0])+len(commands[1])+len(commands[2])+3):][3:-3])
                config.save("config.json")
                await message.channel.send("edit successed")
        elif commands[0] == config.prefix + "join":
            if commands[1] == "send":
                channel = client.get_channel(config.joinchannel)
                await channel.send(content=config.guidemessage["message"],embed=discord.Embed.from_dict(config.joinmessage["embed"]))
            elif commands[1] == "edit":
                if commands[2] == "message":
                    config.joinmessage["message"] = commands[3]
                elif commands[2] == "embed":
                    config.joinmessage["embed"] = json.loads(message.content[(len(commands[0])+len(commands[1])+len(commands[2])+3):][3:-3])
                config.save("config.json")
                await message.channel.send("edit successed")
        elif commands[0] == config.prefix + "embed":
            if commands[1] == "temp":
                await message.channel.send(content="```"+config.embedtemp+"```")
                await message.channel.send(embed=discord.Embed.from_dict(json.loads(config.embedtemp)))
            elif commands[1] == "test":
                await message.channel.send(embed=discord.Embed.from_dict(json.loads(message.content[(len(commands[0])+len(commands[1])+2):][3:-3])))
            return
        elif commands[0] == config.prefix + "tools":
            await message.channel.send("GitHub : https://github.com/ak-2302/Atlasez \nEmbed Generater : https://message.style/app/editor")
        else:
            await message.channel.send("invalid command")
        return
    return

@client.event
async def on_voice_state_update(member, before, after):
            return


with open("token","r",encoding="utf-8") as f:
    token = f.read()
client.run(token)
