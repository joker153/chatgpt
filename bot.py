import os
import openai
from pyrogram import Client, filters
from pyrogram.types import Message

# Get the OpenAI API key from the environment variable
openai.api_key = os.environ.get("OPENAI_API_KEY")

# Set the API hash and ID from the environment variables
api_id = int(os.environ.get("API_ID"))
api_hash = os.environ.get("API_HASH")

# Create a Pyrogram client instance
app = Client(
    "my_bot",
    bot_token=os.environ.get("BOT_TOKEN"),
    api_id=api_id,
    api_hash=api_hash
)

# Define the handler function for handling incoming messages
@ app.on_message(filters.command("gpt") & filters.private)
def generate_text(client: Client, message: Message):
    # Get the text to generate the completion from the user's message
    text = message.text.split(" ", 1)[1]

    # Generate the completion using the OpenAI API
    response = openai.Completion.create(
        engine="davinci",
        prompt=text,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )

    # Get the generated text from the OpenAI API response
    generated_text = response.choices[0].text

    # Send the generated text back to the user
    message.reply_text(generated_text)

# Start the Pyrogram client
app.run()
