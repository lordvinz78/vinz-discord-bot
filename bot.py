import discord
from discord.ext import commands
import os
import asyncio

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"ONLINE {bot.user}")

@bot.event
async def on_message(m):
    if m.author == bot.user: return
    if "halo" in m.content.lower() or "hi" in m.content.lower():
        await m.reply("halo jir 👋")
    await bot.process_commands(m)

async def main():
    async with bot:
        await bot.start(os.getenv("TOKEN"))

asyncio.run(main())
