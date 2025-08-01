import os
import discord
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv
from main import load_camera_config, take_snapshot

load_dotenv()
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

if not TOKEN:
    raise ValueError("Missing DISCORD_BOT_TOKEN in environment")

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)
tree = bot.tree

@tree.command(name="snapshot", description="Take a snapshot from a camera")
@app_commands.describe(camera_name="Name of the camera")
async def snapshot_command(interaction: discord.Interaction, camera_name: str):
    await interaction.response.defer(thinking=True)
    try:
        camera_data = load_camera_config(camera_name)
        image_path = take_snapshot(camera_data)
        await interaction.followup.send(file=discord.File(image_path))
    except Exception as e:
        await interaction.followup.send(f"Snapshot failed: {e}")

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    await tree.sync()
    print("Slash commands synced.")

bot.run(TOKEN)

