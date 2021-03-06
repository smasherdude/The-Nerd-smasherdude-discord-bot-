import os
import discord
from discord.ext import commands
from fractions import Fraction
import math
from typing import Optional
from discord.ext import tasks
from webserver import keep_alive

bot = commands.Bot(command_prefix="=")
#removes the default help
bot.remove_command('help')


@bot.event
async def on_command_error(ctx, error):
    await ctx.send(f"An error occured: {str(error)}")
    print(f"An error occured: {str(error)}")


#bot is online
@bot.event
async def on_ready():
    print(f"Ready!\nUsername: {bot.user}")
    await bot.change_presence(activity=discord.Game(name="Minecraft"))


#lists all possible commands
@bot.command(name="commands", description="Returns all commands available")
async def commands(ctx):
    helptext = "```"
    for command in bot.commands:
        helptext += f"{command}\n"
    helptext += "```"
    await ctx.send(helptext)


@bot.command()
async def help(ctx):
    embed = discord.Embed(
        title="Help and commands",
        url=
        "https://github.com/smasherdude/The-Nerd-smasherdude-discord-bot-/wiki",
        description=
        "These are all the commands you could do. A more in depth guide will be on our wiki page",
        color=0x2316d4)
    embed.add_field(
        name="Math Commands",
        value=
        "=calculate <the problem> \n=percentof <percentage> <number> \n=ispercentof <number1> <number2> \n=hypotenuse <side1> <side2> \n=convert <conversion type> <number1> <number2 fractions only> \n=unitconvert <conversion type> <number> ",
        inline=False)
    await ctx.send(embed=embed)


@bot.command()
async def ping(ctx):  #ping
    latency = round(bot.latency * 1000, 2)
    await ctx.send(f"{latency} ms")


@bot.command()
async def test(ctx):  #random test that i should delete soon
    await ctx.send("Test successful")


@bot.command()
async def server(ctx):  #server info and stuff
    embed = discord.Embed(
        title="Minecraft Server",
        url=
        "https://discord.com/channels/686062264192860211/864093314964652052/864093931843092480",
        description="Join the Smasherdude Server",
        color=discord.Color.blue())
    embed.add_field(name="IP Address",
                    value="smasherdude.aternos.me",
                    inline=False)
    embed.add_field(name="Version",
                    value="1.17.1 on Java and the current version of Bedrock",
                    inline=False)
    await ctx.send(embed=embed)


#calculator
@bot.command()
async def calculate(ctx, *nums):
    operation = " + ".join(nums)
    await ctx.send(f'{operation} = {eval(operation)}')


async def calculate(ctx, *nums):
    operation = " - ".join(nums)
    await ctx.send(f'{operation} = {eval(operation)}')


async def calculate(ctx, *nums):
    operation = " * ".join(nums)
    await ctx.send(f'{operation} = {eval(operation)}')


async def calculate(ctx, *nums):
    operation = " / ".join(nums)
    await ctx.send(f'{operation} = {eval(operation)}')


#percentage calculations
@bot.command()
async def percentof(ctx, a: int, b: int):
    c = (a / 100) * b
    await ctx.send(f'{a}% of {b} = {c}')


@bot.command()
async def ispercentof(ctx, a: int, b: int):
    c = (a / b) * 100
    await ctx.send(f'{a} is {c}% of {b}')


@bot.command()
async def hypotenuse(ctx, a: float, b: float):
    c = (a * a) + (b * b)
    await ctx.send(f'{math.sqrt(c)} is the hypotenuse of {a} and {b}')


#percentage to fraction to decimal converter
@bot.command()
async def convert(ctx, args, a: float, b: Optional[int] = 5):
    ftod = a / b
    dtof = Fraction(a)
    dtop = a * 100
    ptod = a / 100
    ptof = Fraction(a / 100)
    ftop = (a / b) * 100
    if args == 'ftod':
        await ctx.send(f'{a}/{b} is converted to {ftod}')
    elif args == 'dtof':
        await ctx.send(f'{a} is {dtof}')
    elif args == 'dtop':
        await ctx.send(f'{a} is {dtop}%')
    elif args == 'ptod':
        await ctx.send(f'{a}% is {ptod}')
    elif args == 'ptof':
        await ctx.send(f'{a}% is {ptof}')
    elif args == 'ftop':
        await ctx.send(f'{a}/{b} is {ftop}%')
    else:
        await ctx.send('an error has occured')


#conversion between units
@bot.command()
async def unitconvert(ctx, args, a: float):
    mtokm = a / 1000
    kmtom = a * 1000
    cmtom = a / 100
    mtocm = a * 100
    cmtokm = a / 100000
    kmtocm = a * 100000
    ctof = (a * 9 / 5) + 32
    ftoc = (a - 32) * 5 / 9
    if args == 'mtokm':
        await ctx.send(f'{a}m is converted to {mtokm}km')
    elif args == 'kmtom':
        await ctx.send(f'{a}km is converted to {kmtom}m')
    elif args == 'cmtom':
        await ctx.send(f'{a}cm is converted to {cmtom}m')
    elif args == 'mtocm':
        await ctx.send(f'{a}m is converted to {mtocm}cm')
    elif args == 'cmtokm':
        await ctx.send(f'{a}cm is converted to {cmtokm}km')
    elif args == 'kmtocm':
        await ctx.send(f'{a}km is converted to {kmtocm}cm')
    elif args == 'ctof':
        await ctx.send(f'{a}c is converted to {ctof}f')
    elif args == 'ftoc':
        await ctx.send(f'{a}f is converted to {ftoc}c')
    else:
        await ctx.send('an error has occured')


keep_alive()
token = os.environ['TOKEN']
bot.run(token)
