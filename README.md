<div align="center">

# 🤖 Friday — Virtual Assistant

### *"Good evening. I'm Friday, your personal AI assistant."*

[![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Gemini API](https://img.shields.io/badge/Gemini%20API-2.5%20Flash%20Lite-orange?style=for-the-badge&logo=google&logoColor=white)](https://ai.google.dev/)
[![Speech Recognition](https://img.shields.io/badge/Speech-Recognition-green?style=for-the-badge&logo=microphone&logoColor=white)](https://pypi.org/project/SpeechRecognition/)

A voice-activated AI assistant inspired by Iron Man's **F.R.I.D.A.Y.** — wake it with your voice, give it commands, and it responds intelligently using Google's Gemini AI.

[Features](#-features) · [Setup](#-setup) · [Usage](#-usage) · [Commands](#-commands) · [Project Structure](#-project-structure)

</div>

---

## ✨ Features

- 🎤 **Wake word activation** — just say *"Friday"* to activate
- 🧠 **AI-powered responses** — powered by Google Gemini 2.5 Flash Lite
- 🌐 **Open websites** — launch Google, YouTube, GitHub, Codeforces by voice
- 🎵 **Play music** — say "play [song name]" to open songs from your library
- 📰 **Read the news** — fetches and reads top headlines aloud
- 🔊 **Text-to-speech** — speaks every response using `pyttsx3`
- 😴 **Deactivate by voice** — say *"deactivate"* to shut Friday down

---

## 🛠️ Tech Stack

| Package | Purpose |
|---|---|
| `speech_recognition` | Converts your voice to text |
| `pyttsx3` | Text-to-speech (offline) |
| `google-genai` | Gemini AI for smart responses |
| `requests` | Fetches live news from NewsAPI |
| `webbrowser` | Opens URLs in browser |
| `pyaudio` | Microphone input support |

---

## ⚙️ Setup

### Prerequisites

- Python **3.11** recommended (3.12 works too)
- A **Gemini API key** → [Get one free here](https://aistudio.google.com/app/apikey)
- A **NewsAPI key** → [Get one free here](https://newsapi.org/)

---

### 1. Clone the repository

```bash
git clone https://github.com/Mayurkshirsagar-web/friday-virtual-assistant.git
cd friday-virtual-assistant
```

---

### 2. Create a virtual environment

```bash
# Windows
py -3.11 -m venv venv
venv\Scripts\activate

# Mac / Linux
python3.11 -m venv venv
source venv/bin/activate
```

You should see `(venv)` appear at the start of your terminal prompt.

---

### 3. Install all packages

```bash
pip install -r package_friday.txt
```

> **Windows users:** `pyaudio` may fail to install. If it does, run:
> ```bash
> pip install pipwin
> pipwin install pyaudio
> ```
> If that also fails, download the prebuilt `.whl` from [Gohlke's site](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio) and install manually:
> ```bash
> pip install PyAudio-0.2.14-cp311-cp311-win_amd64.whl
> ```

---

### 4. Add your API keys

Open `main.py` and replace the placeholders:

```python
# Line ~12 — Gemini API key
gemini_client = genai.Client(api_key="YOUR_GEMINI_API_KEY_HERE")

# Line ~60 — NewsAPI key
r = requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=YOUR_NEWS_API_KEY_HERE")
```

---

### 5. Run Friday

```bash
python main.py
```

Friday will say *"Initializing Friday.."* — you're good to go.

---

## 🗣️ Usage

```
Say "Friday"  →  Friday activates and says "What's up!"
Then give a command  →  Friday responds
Say "deactivate"  →  Friday shuts down
```

---

## 📋 Commands

| Voice Command | What Friday Does |
|---|---|
| `"Friday"` | Wakes up Friday |
| `"open google"` | Opens google.com |
| `"open youtube"` | Opens youtube.com |
| `"open github"` | Opens github.com |
| `"open codeforces"` | Opens codeforces.com |
| `"play [song name]"` | Opens song from music library |
| `"news"` | Reads top US headlines aloud |
| `"deactivate"` | Shuts Friday down |
| *anything else* | Sends to Gemini AI for a smart response |

---

## 📁 Project Structure

```
friday-virtual-assistant/
│
├── main.py              # Core assistant logic
├── musicLibrary.py      # Song name → URL mapping
├── package_friday.txt   # All required packages
└── README.md
```

---

## 🎵 Adding Songs to the Music Library

Open `musicLibrary.py` and add songs to the `music` dictionary:

```python
music = {
    "believer": "https://www.youtube.com/watch?v=7wtfhZwyrcc",
    "blinding lights": "https://www.youtube.com/watch?v=4NRXx6U8ABQ",
    "your song name": "https://youtube-link-here",
}
```

Then just say *"Friday, play believer"* and it opens in your browser.

---

## 🔐 API Keys — Keep Them Safe

Never commit your API keys to GitHub. Use environment variables instead:

```python
import os
gemini_client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))
```

Set them in your terminal before running:

```bash
# Windows
set GEMINI_API_KEY=your_key_here

# Mac / Linux
export GEMINI_API_KEY=your_key_here
```

---

## 🤝 Contributing

Pull requests are welcome! Feel free to open an issue for bugs or feature suggestions.

---

<div align="center">

Made by [Mayur Kshirsagar](https://github.com/Mayurkshirsagar-web)

</div>
