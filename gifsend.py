import os
import discord
from discord.ext import commands
import json

FILE_DIR = os.path.dirname(os.path.abspath(__file__))

class Gifsend(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.dict = loadJson(FILE_DIR+"/commandList.json")

    @commands.command()
    async def send(self, ctx, arg):

        if ctx.author == self.client.user:
            return

        if arg in self.dict:
            await ctx.send(self.dict[arg]['commandContent'])
        else:
            await ctx.send('Gif not found bitch')

    @commands.command()
    async def commands(self, ctx):
        msg = json.dumps(self.dict, indent=5, sort_keys=True)
        title = 'See list of commands below: \n\nNote that the bot currently only detects a command if it is the FIRST element of a message, ie: \n'\
             '```"!fu @user" will work \n'\
             '"@user is a !cuck" will NOT work```'
        await ctx.send(title + "```"+ msg + "```") 

def loadJson(fileName):
    f = open(fileName, 'r')
    data = json.load(f)
    return data

def setup(client):
    client.add_cog(Gifsend(client))