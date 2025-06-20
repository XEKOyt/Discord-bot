
````markdown
# 🕵️‍♂️ Discord Bot with System Access Capabilities

This project is a Python-powered Discord bot with extended system-level capabilities for educational, administrative, or personal use. It includes functions like PowerShell command execution, desktop screenshot capture, file opening, and redirection to a humorous website (`amogus.io`).

> ⚠️ **Disclaimer**: This bot has the potential to control parts of the host system. Use responsibly and **never run or share this bot without full transparency and consent** from the target user.

---

## 📦 Requirements

The bot uses the following Python libraries:

```python
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
````

You can install the required dependencies with:

```bash
pip install -r requirements.txt
```

<details>
<summary><code>requirements.txt</code> contents</summary>

```
discord.py
pyautogui
```

</details>

---

## 🚀 Features and Commands

The bot listens for specific command messages in Discord and responds as follows:

| Command        | Description                                                          |
| -------------- | -------------------------------------------------------------------- |
| `!exec <cmd>`  | Executes the given PowerShell command and returns the output.        |
| `!open <path>` | Opens a file or application at the specified local path.             |
| `!sus`         | Opens [https://amogus.io](https://amogus.io) in the default browser. |
| `!ss`          | Captures a screenshot of the user's current desktop.                 |
| `!help`        | Displays a help menu listing all available commands.                 |

---

## ⚙️ Running the Bot

Make sure your environment is ready:

1. Python 3.8+ installed
2. Dependencies installed (`pip install -r requirements.txt`)
3. A valid Discord bot token

Then run the bot with:

```bash
python bot.py
```

Replace `bot.py` with the actual filename if different.

---

## 🔐 Security & Ethics Warning

This bot gives control over the host system to a remote Discord channel. **Never use this bot for malicious purposes**. It is intended for **educational use only**.

---

## 🧾 License

This project is distributed under the MIT License. See `LICENSE` for more details.

---

## 👀 Example

```txt
User: !exec Get-Process
Bot : [Lists all running processes]

User: !open C:/Windows/System32/notepad.exe
Bot : ✅ File opened.

User: !ss
Bot : [Sends a screenshot image]

User: !sus
Bot : ✅ Amogus engaged.

User: !help
Bot : [Displays list of commands and usage]
```

---

Made with ❤️ and a little bit of ✨sus✨.

```

---

Let me know if you want this converted into a `requirements.txt` and `LICENSE` file or want a section added for environment variables (like the bot token).
```
