# Discord Gemini Bot 🤖

A powerful Discord bot that uses Google's Gemini API to bring generative AI and LLM capabilities to your Discord Server!

## Features:

*   **Intelligent Conversations & Responses:** Chat with a LLM AI right in your Discord channels.
*   **Easy to Set Up:** Get the bot running in just a few simple steps.
*   **Secure:** Uses environment variables to keep your API keys safe.

## Setup & Installation

To get this bot running on your own machine, follow these steps below :

### 1. Prerequisites

*   Python 3.8 or higher (latest one recommended)
*   A Discord Bot Token ([How to get one](https://discordpy.readthedocs.io/en/stable/discord.html))
*   A Google Gemini API Key ([Get one here](https://aistudio.google.com/app/apikey))


### 2. Clone the Repository

Clone this repository to your local machine:
```sh
git clone https://github.com/tarangcodes/discord-bot-project.git
cd discord-bot-project
```

### 3. Set Up the Environment

Create a virtual environment to keep dependencies isolated:
```sh
# For Windows
python -m venv .venv
.\.venv\Scripts\activate

# For macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
```

### 4. Install Dependencies ⬇️

Install the required Python packages using pip:
```sh
pip install -r requirements.txt
```

### 5. Configure Your API Keys 🔑

Create a file named `.env` in the main project directory. **This file is crucial and should not be shared.** Add your secret keys to it like this:

```
DISCORD_BOT_TOKEN="YOUR_DISCORD_BOT_TOKEN_HERE"
GEMINI_API_KEY="YOUR_GEMINI_API_KEY_HERE"
```

### 6. Run the Bot 

You're all good to go now! Start the bot with this command below:
```sh
python bot.py
```

### 7. Results 

The bot is up and running in your discord channel! Don't forget it to give permissions in developer portal!

<img width="500" height="200" alt="Image" src="https://github.com/user-attachments/assets/c75223da-1de5-4933-82c7-b1b69bbe877f" />