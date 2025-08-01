![Python](https://img.shields.io/badge/python-3.10+-blue)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

# 📷 Camcord

**Camcord** is a lightweight, Linux-based RTSP camera hub that connects your surveillance or IP cameras to a Discord server.  
It supports multiple cameras, automated snapshots, and on-demand video clips — all controlled via a Discord bot.

## 🚀 Features

- 🖼️ Auto-snapshots posted to Discord every X seconds
- 🎞️ On-demand video clips via Discord command (e.g. `/clip driveway 10s`)
- 🔐 Secure password generation and encrypted camera config
- 🔧 Easy setup with YAML config for multiple cameras
- 🧠 Smart port hardening and logging for better security
- 🐧 Designed to run as a background Linux service or Docker container

## 🔧 Use Cases
- Home security snapshot monitoring
- Remote jobsite camera access for teams
- Wildlife observation posting to private Discord
- Lightweight camera alerts without cloud services

## Quick Start
1. `git clone https://github.com/Byte420/camcord.git`
2. `pip install -r requirements.txt`
3. Create `.env` with `DISCORD_BOT_TOKEN=...`
4. `python main.py`


---
Built with Python, ffmpeg, and 💬 Discord bot integration.
