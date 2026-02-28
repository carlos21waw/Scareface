import os
import discord
from discord.ext import commands, tasks
import asyncio
from aiohttp import web

# Step 2: check if Fly secret is loaded
TOKEN = os.getenv("BOT_TOKEN")
print("TOKEN:", TOKEN)  # <- This will show your token in Fly logs

if TOKEN is None:
    raise Exception("BOT_TOKEN is missing! Did you deploy the secret?")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=">", intents=intents)

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

# Dummy web server to keep Fly happy
async def handle(request):
    return web.Response(text="Bot is running")

async def start_server():
    app = web.Application()
    app.router.add_get("/", handle)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", 8080)
    await site.start()

async def main():
    await asyncio.gather(bot.start(TOKEN), start_server())

asyncio.run(main())
