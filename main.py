import discord
from discord.ext import tasks, commands
import os
from os.path import join, dirname
import webscraper
from dotenv import load_dotenv
import music
import gifsend

FILE_DIR = os.path.dirname(os.path.abspath(__file__))#gets the absolute directory of the environment (os)

def main():
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)

    cogs = [music, gifsend]

    bot = commands.Bot(command_prefix='!', intents = discord.Intents.all())

    for i in range(len(cogs)):
       cogs[i].setup(client=bot)
       print(str(cogs[i]) +" successfully set up")

    bot.run(os.environ.get("TOKEN"))

if __name__ == "__main__":
    main()