from bs4 import BeautifulSoup
import requests
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import pymongo

# Make a request to the website
def check_url_patterns(url):
    patterns = [
        r"ww\.mirrobox\.com",
        r"www\.nephobox\.com",
        r"freeterabox\.com",
        r"www\.freeterabox\.com",
        r"1024tera\.com",
        r"4funbox\.co",
        r"www\.4funbox\.com",
        r"mirrobox\.com",
        r"nephobox\.com",
        r"terabox\.app",
        r"terabox\.com",
        r"www\.terabox\.ap",
        r"www\.terabox\.com",
        r"www\.1024tera\.co",
        r"www\.momerybox\.com",
        r"teraboxapp\.com",
        r"momerybox\.com",
        r"tibibox\.com",
        r"www\.tibibox\.com",
        r"www\.teraboxapp\.com",
    ]

    for pattern in patterns:
        if re.search(pattern, url):
            return True

    return False
url = pattern # replace with the url you want to scrape
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find data within the HTML structure
data = soup.find_all('div', class_='example-class')  # replace 'div' and 'example-class' with relevant HTML tag and class

# Print the scraped data
for item in data:
    print(item.get_text())


# Replace 'your_token' with your bot's token
updater = Updater(token='7237123123:AAFTWrP0eSpk2eJLm277cZdGLI8p1VLWKRA', use_context=True)

# Replace 'your_mongodb_connection_string' with your MongoDB connection string
client = pymongo.MongoClient('your_mongodb_connection_string')
db = client.test

def save_to_db(update: Update, context: CallbackContext) -> None:
    # This will save all incoming messages to the 'messages' collection in MongoDB
    db.messages.insert_one(update.message.to_dict())
    context.bot.send_message(chat_id=update.effective_chat.id, text="Message saved!")

start_handler = CommandHandler('start', start)
message_handler = MessageHandler(Filters.text & (~Filters.command), save_to_db)

updater.dispatcher.add_handler(start_handler)
updater.dispatcher.add_handler(message_handler)

updater.start_polling()
