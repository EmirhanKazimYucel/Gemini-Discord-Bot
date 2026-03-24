# 🌌 Gemini Discord Bot

A cutting-edge, modular Discord assistant powered by **Google Gemini 2.5 Flash**. Built with a focus on high-speed processing, advanced vision analysis, and seamless user interaction.

## ✨ Key Features
- **🧠 Advanced Context Awareness:** Uses the latest Gemini 2.5 Flash capabilities to maintain persistent, smart conversations with users.
- **👁️ Next-Gen Vision AI:** Process and analyze images instantly using the `!bak` command.
- **🏗️ Professional Architecture:** Developed using the **Discord Cogs** framework, ensuring the codebase is clean, modular, and easy to scale.
- **🐳 Dockerized Environment:** Fully containerized with Docker and Docker Compose for effortless deployment on any system.
- **🛡️ Enterprise-Grade Security:** Sensitive API keys and tokens are managed via environment variables to ensure zero leakage.

## 🛠️ Tech Stack
- **Language:** Python 3.10+
- **Model:** Google Gemini 2.5 Flash
- **Framework:** [discord.py](https://github.com/Rapptz/discord.py)
- **Deployment:** Docker & Docker Compose
- **Image Processing:** Pillow (PIL) & aiohttp

---

## 🚀 Quick Start

### 1. Prerequisites
- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- Discord Bot Token ([Discord Developer Portal](https://discord.com/developers/applications))
- Gemini API Key ([Google AI Studio](https://aistudio.google.com/))

### 2. Setup
Clone the repository:
```bash
git clone [https://github.com/yourusername/Gemini-Discord-Bot.git](https://github.com/yourusername/Gemini-Discord-Bot.git)
cd Gemini-Discord-Bot
```
###3. Configuration
Create a .env file in the root directory and add your credentials:

```bash
DISCORD_TOKEN=your_discord_bot_token_here
GEMINI_API_KEY=your_google_gemini_api_key_here
```
### 4. Deployment
Run the bot using Docker Compose:
```bash
docker-compose up -d --build
```

## 📂 Project Structure

```text
Gemini-Discord-Bot/
├── src/                    # Source code directory
│   ├── ai/                 # Gemini 2.5 Flash integration logic
│   │   └── gemini_client.py
│   ├── bot/                # Discord bot core and command modules
│   │   ├── core.py         # Main bot class and initialization
│   │   └── cogs/           # Modular command extensions (Cogs)
│   │       ├── chat.py     # AI Chat memory logic
│   │       └── image.py    # Vision analysis logic
│   └── utils/              # System utilities and config management
│       └── config.py       # Environment variable handler
├── data/                   # Local data and logs storage
├── .env                    # PRIVATE: API keys and tokens (Git-ignored)
├── .gitignore              # Git exclusion rules
├── Dockerfile              # Docker build instructions
├── docker-compose.yml      # Docker container orchestration
├── requirements.txt        # Python dependencies
└── main.py                 # Application entry point
```
