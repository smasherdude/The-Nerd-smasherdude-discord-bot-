import os
import discord
from discord.ext import commands
from fractions import Fraction
import math
from typing import Optional
from discord.ext import tasks
from webserver import keep_alive
from discord import app_commands
from discord.app_commands import Choice



intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@client.event
async def on_command_error(ctx, error):
    await ctx.send(f"An error occured: {str(error)}")
    print(f"An error occured: {str(error)}")


#bot is online
@client.event
async def on_ready():
  await tree.sync()
  print(f"Ready!\nUsername: {client.user}")
  await client.change_presence(activity=discord.Game(name="Minecraft"))
  
#these first two commands are the test commands
@tree.command(name = "test", description = "My first application Command") #Add the guild ids in which the slash command will appear. If it should be in all, remove the argument, but note that it will take some time (up to an hour) to register the command if it's for all guilds.
async def first_command(interaction: discord.Interaction, number: int, string: str):
    await interaction.response.send_message(f'{number=} {string=}')

@tree.command(name = "test2", description = "test123")
@app_commands.describe(number='The file to upload', number2='number2')
async def upload(interaction: discord.Interaction, number: int, number2: int):
    await interaction.response.send_message(f'Test successful {number}!', ephemeral=True)

#these are the imported commands from the previous version

@tree.command(name = "help", description = "Help")
async def help(interaction):
    embed = discord.Embed(
        title="Help and commands",
        url=
        "https://github.com/smasherdude/The-Nerd-smasherdude-discord-bot-/wiki",
        description=
        "Check out our wiki page for more information",
        color=0x2316d4)
    await interaction.response.send_message(embed=embed)

@tree.command(name = "ping", description = "Shows bot latency")
async def ping(interaction):  #ping
    latency = round(client.latency * 1000, 2)
    await interaction.response.send_message(f"{latency} ms")

@tree.command(name = "server", description = "My minecraft server")
async def server(interaction):  #server info and stuff
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
    await interaction.response.send_message(embed=embed)

#calculator
@tree.command(name = "calculate", description = "Calculate with some basic arithmetic")
async def calc(interaction, operation:str):
  await interaction.response.send_message(f'{operation} = {eval(operation)}')

@tree.command(name = "percentagecalculator", description = "Calculates Percentages")
@app_commands.describe(name="Operation")
@app_commands.choices(name=[
        Choice(name = "percentof", value = "c"),
        Choice(name = "ispercentof", value = "d")
    ])
async def testing(interaction: discord.Interaction, num1:int, name: str, num2:int):
  c = (num1 / 100) * num2
  d = (num1 * num1) + (num2 * num2)
  if name == 'c':
    await interaction.response.send_message(f'{num1}% of {num2} = {c}')
  else:
    await interaction.response.send_message(f'{num1} is {d}% of {num2}')


keep_alive()
token = os.environ['TOKEN']
client.run(token)
