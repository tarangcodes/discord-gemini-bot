import os # To access environment variables.
import discord # Important to interact with Discord API.
import google.generativeai as genai # To interact with Gemini API.
from dotenv import load_dotenv #Loading env variables from .env file.

load_dotenv() #take env variables from .env.file.

<<<<<<< HEAD
GEMINI_API_KEY = os.getenv('gemini_api_key') # Access the Gemini API key from environment variables.
DISCORD_BOT_TOKEN = os.getenv('DISCORD_TOKEN') # Access the Discord Bot Token from environment variables.
=======
gemini_api_key = os.getenv('GEMINI_API_KEY') # Access the Gemini API key from environment variables.
>>>>>>> 86e57de2379f827d2abb9f67df8cbc4c5211f13a
genai.configure(api_key=gemini_api_key) # Configure the Gemini API with key.
DISCORD_BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')
# Asynchronous function to get response from Gemini API
async def get_gemini_response(prompt):
    try:
        model = genai.GenerativeModel("gemini-2.5-pro") # Using 'gemini-1.5-flash for faster responses, you can change it to other models.

        response = await model.generate_content_async(prompt) # Generate content asynchronously.
        return response.text # This will return the text response from Gemini Large Language Model.
       # Incase an error occurs, it will be caught and printed.
    except Exception as e:
        print(f"Oops! Looks Like something went wrong.😅 {e}") 
        return "Sorry, I couldn't process that request for now."

# Custom client class inheriting attributes from discord.Client
class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}')
        print("Your Adam Smasher is ready to answer questions!")
        # The bot gets ready and prints a message to the console to let you know it's online.

    async def on_message(self, message):
        if message.author == self.user:
            return # Ignore messages from the bot itself to prevent infinite loops.

        if message.content.startswith('$a '): # Bot's command starts with $a to trigger a response. You can change this.


            async with message.channel.typing():
                # Get the user's question by removing the command part.
                prompt = message.content.replace('$a ', '').strip()

                # If the prompt is not empty, get a response from Gemini.
                if prompt:
                    gemini_response = await get_gemini_response(prompt)
                    await message.channel.send(gemini_response)
                else:
                    await message.channel.send("Please ask a question after the `$a` command!")



# Create intents keyword argument.
intents = discord.Intents.default()
intents.message_content = True

# Update the call here by passing the 'intents' keyword argument.
client = MyClient(intents=intents)
discord_token = os.getenv('DISCORD_TOKEN')
client.run(discord_token)

