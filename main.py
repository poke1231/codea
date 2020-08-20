
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.command()
async def claimer (ctx):
    await ctx.send('You have no gifts or rewards in here')

bot.run('NzQ1MTEwMTQxMjgzODYwNTM5.Xzs_5Q.kYfK8zIy18IgGlJo0ma09iCkoWI')
import discord
from discord.ext import commamands
import discord
from discord.ext import commands

embed = commands.Bot(command_prefix = "!")

class BotData:
    def __init__(self):
        self.welcome_channel = None
        self.goodbye_channel = None

        self.reaction_role = None
        self.reaction_message = None

botdata = BotData()
@bot.event
async def on_ready():
    print("Your bot is ready.")
@bot.command()
async def cool(embed):
   embedVar = discord.Embed(title="Commands",color=844532)
   embedVar.add_field(name="wfna;ng;nawg;kln", value="kawg;kwanbg;kwag")
   await ctx.channel.send(embed=embedVar)
