from distutils import command
from http import client
import discord
from discord.ext import tasks
import os
from os.path import join, dirname
import webscraper
from dotenv import load_dotenv
import json

#sets up the server environment and allows the fetching of the ENVIRONMENT VARIABLES
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

client = discord.Client()

FILE_DIR = os.path.dirname(os.path.abspath(__file__)) #gets the absolute directory of the environment (os)

newestVersion = None
URL = "https://github.com/AllenNotAlan/LeetCodeSolutions/releases" #For future use -> will be the link for scraping a webpage

@client.event
async def on_ready():
    print('Bot: {0.user} ready'
        .format(client))
    await scrape.start()

@client.event
async def on_message(message):
    content = ""
    commandDict = loadJson(FILE_DIR+"/commandList.json")

    if message.author == client.user:
        return

    if message.content.startswith("!help"):
        msg = json.dumps(commandDict, indent=4, sort_keys=True)
        title = "List of commands \n"
        await message.channel.send(title + "```" + msg + "```")

    if message.content in commandDict:
        content = commandDict[message.content]["commandContent"]
        await message.channel.send(content)

@tasks.loop(seconds=60)
async def scrape():
    versionHeader = webscraper.sendMessage(URL)

    global newestVersion
    if newestVersion == None:
        newestVersion = versionHeader

    if versionHeader != newestVersion:
        newestVersion = versionHeader
        channel = client.get_channel(os.environ.get("CHANNEL_ID_1"))
        messageToSend = 'New version of ValheimPlus has been released {v}. See {url}.'.format(v=newestVersion, url=URL)
        await channel.send(messageToSend)

def loadJson(fileName):
    f = open(fileName, 'r')
    data = json.load(f)
    return data

def main():
    client.run(os.environ.get("TOKEN")) #MUST NOT BE PUBLIC

if __name__ == "__main__":
    main()