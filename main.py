#importing modules yuh
import discord
from discord.ext import commands
import os
import random

#imports the TOKEN variable from apikeys python file.  
from apikeys import *

bot = commands.Bot(command_prefix = '!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print('The bot is ready to be used!')
    print('-----------------------------')

#command named "johny" to send a random picture from "johny" folder
@bot.command()
async def johny(ctx):
    #folder destination
    johny_folder = r"C:\Users\huade\Desktop\Johny Bot\johny"
    
    #turn folder destination into a list
    johny_files = os.listdir(johny_folder)
    
    if johny_files:
        #random module chooses random element in list (random photo in folder)
        random_johny = random.choice(johny_files)
      
        #turns the randomly selected image from above^^ to a path in the folder destination TO THAT image
        file_path = os.path.join(johny_folder, random_johny)

        #opens the path to the random picture (from variable above) and sends it
        with open(file_path, 'rb') as f:
            file = discord.File(f)
            await ctx.send(file=file)
            
#TOKEN variable from the OTHER python file (apikeys.py). 
bot.run(TOKEN)
