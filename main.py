import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.messages = True
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

# Bot start message
@bot.event
async def on_ready():
    print("Bot Online")

# Welcome message and auto assign default role
@bot.event
async def on_member_join(member):
    role_id = 1417506472727810139
    role = member.guild.get_role(role_id)

    # Try to find a channel named "welcome"
    welcome_channel = discord.utils.get(member.guild.text_channels, name='welcome')

    # If no welcome channel try to find general
    if not welcome_channel:
        welcome_channel = discord.utils.get(member.guild.text_channels, name='general')

    # Assign role if found
    if role:
        try:
            await member.add_roles(role)
        except discord.Forbidden:
            print(f"I don't have permission to add {role} to {member}")

    if welcome_channel:
        await welcome_channel.send(f"Welcome to the Hideout, {member.mention}!")

# Tell me a joke feature
async def main():
    async with bot:
        await bot.load_extension("cogs.fun")
        await bot.start(token)

asyncio.run(main())
