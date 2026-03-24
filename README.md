# 🌌 Gemini Discord Bot

A high-performance, modular Discord assistant powered by **Google Gemini 2.5 Flash**. Designed with scalability and clean code principles in mind.

## ✨ Key Features
- **🧠 Context-Aware Conversations:** Persistent memory management per user, allowing the bot to remember previous interactions.
- **👁️ Multimodal Vision:** Advanced image analysis capabilities. Upload a photo and ask questions about it using the `!bak` command.
- **🏗️ Modular Architecture:** Built using the **Discord Cogs** system, making it easy to add new features without touching the core logic.
- **🐳 Dockerized Deployment:** Pre-configured with Docker and Docker Compose for a seamless "plug-and-play" experience.
- **🛡️ Secure Configuration:** Environment variable management ensures API keys stay private.

## 🛠️ Tech Stack
- **Language:** Python 3.10+
- **Framework:** [discord.py](https://github.com/Rapptz/discord.py)
- **AI Engine:** Google Gemini AI (Generative AI SDK)
- **Containerization:** Docker & Docker Compose
- **Image Processing:** Pillow (PIL)

---

## 🚀 Quick Start

### 1. Prerequisites
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed.
- A Discord Bot Token (from [Discord Developer Portal](https://discord.com/developers/applications)).
- A Gemini API Key (from [Google AI Studio](https://aistudio.google.com/)).

### 2. Installation
Clone the repository:
```bash
git clone [https://github.com/EmirhanKazimYucel/Gemini-Discord-Bot.git](https://github.com/yourusername/Gemini-Discord-Bot.git)
cd Gemini-Discord-Bot
