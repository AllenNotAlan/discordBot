from http import client
import discord
from discord.ext import tasks
import os
from os.path import join, dirname
import webscraper
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
client = discord.Client()

newestVersion = None
URL = "https://github.com/AllenNotAlan/LeetCodeSolutions/releases"

@client.event
async def on_ready():
    print('Hello u cunt. Logged in as {0.user}'
        .format(client))
    await scrape.start()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Ur a cunt!')

    if message.content.startswith('!link'):
        await message.channel.send('https://static.wixstatic.com/media/c21d0e_9f0910faa19c49e6a70c4d5689e7ddd3~mv2.gif')

@tasks.loop(seconds=60)
async def scrape():
    versionHeader = webscraper.sendMessage("Webscraper started", URL)

    global newestVersion
    if newestVersion == None:
        newestVersion = versionHeader

    if versionHeader != newestVersion:
        print(versionHeader + " != " + newestVersion)
        newestVersion = versionHeader
        print(versionHeader + " == " + newestVersion)
        channel = client.get_channel(os.environ.get("CHANNEL_ID_1")) #must not be public!
        messageToSend = 'New version of ValheimPlus has been released {v}. See {url}.'.format(v=versionHeader, url=URL)
        await channel.send(messageToSend)
    print("Task ran")

def main():
    client.run(os.environ.get("TOKEN")) #MUST NOT BE PUBLIC

if __name__ == "__main__":
    main()