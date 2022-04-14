import os
import discord
from discord.ext import commands
from fractions import Fraction
import math
from typing import Optional
from discord.ext import tasks
import asyncio

bot = commands.Bot(command_prefix="=")


@bot.event
async def on_command_error(ctx, error):
    await ctx.send(f"An error occured: {str(error)}")
    print(f"An error occured: {str(error)}")


#bot is online
@bot.event
async def on_ready():
    print(f"Ready!\nUsername: {bot.user}")
    await bot.change_presence(activity=discord.Game(name="Minecraft"))


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

token = os.environ['TOKEN']
bot.run(token)
