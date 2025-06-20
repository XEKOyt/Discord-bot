# 🤖 Discord System Bot

This is a multifunctional Python-based Discord bot designed to execute PowerShell commands, download and open files, take screenshots, start local programs, and open websites like [amogus.io](https://amogus.io) — all via Discord chat.

> ⚠️ **Security Warning**: This bot executes code and opens files on the machine it's running on. Use **only on systems you own or have permission to control**. Never run this on public or shared machines.

---

## 🧰 Features

| Command          | Description                                                                 |
|------------------|-----------------------------------------------------------------------------|
| `!exec <cmd>`    | Executes a PowerShell command and returns the output.                      |
| `!open <url>`    | Downloads a file from a URL and optionally opens it.                        |
| `!start <path>`  | Starts or executes a file from a local path.                                |
| `!ss`            | Takes a screenshot of the desktop and sends it to the channel.              |
| `!sus`           | Opens [https://amogus.io](https://amogus.io) in the default web browser.    |
| `!help`          | (Default help command from `discord.ext.commands`) Lists all commands.      |

---

## 🚀 Setup

### 🔧 Prerequisites

- Python 3.8+
- Discord bot token
- A Windows system (uses PowerShell and `os.startfile`)

### 📦 Installation

1. Clone this repo:
   ```bash
   git clone https://github.com/XEKOyt/Discord-bot.git
   cd Discord-bot
````

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` or directly modify the `TOKEN` and `CHANNEL_ID` in the script.

---

### 📄 requirements.txt

```
discord.py
pyautogui
```

---

## 🔐 Configuration

In the Python file:

```python
TOKEN = ''  # Add your bot token here
CHANNEL_ID = 69420  # Replace with the channel ID where the bot should send the startup message
```

---

## 🏁 Running the Bot

```bash
python bot.py
```

You’ll see logs printed in the terminal and also saved to `bot.log`.

---

## ⚠️ Legal & Ethical Use

This bot has **remote access features**. Running this bot without informed user consent may violate privacy laws and Discord's Terms of Service.

It is intended strictly for:

* Educational purposes
* Remote system automation on machines you control

---

## 🧪 Example Usage

```txt
!exec Get-ChildItem C:\Users
!open https://example.com/file.exe
!start "C:/Windows/System32/notepad.exe"
!ss
!sus
```

---

## 📜 License

This project is licensed under the Do whatever you want but if theres a law case don't call me License.

```

---

Let me know if you'd like:

- A sample `.env` file format for safer config
- A version that uses slash commands (`discord.app_commands`) instead of prefix commands
- A version without logs
```
