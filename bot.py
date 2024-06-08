#create a telegram bot which converts terabox links
import telebot

# Replace with your actual Telegram bot token
BOT_TOKEN = "7237123123:AAFTWrP0eSpk2eJLm277cZdGLI8p1VLWKRA"

# Create a Telegram bot instance
bot = telebot.TeleBot(BOT_TOKEN)

# Dictionary to store Terabox links and their corresponding direct download links
terabox_to_direct = {
    "https://teraboxapp.com/s/1RCBLl4RBXh446ZKoHgHZJt_Q": "https://example.com/download/12345"
    # Add more mappings as needed
}

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Welcome! Send me a Terabox link, and I'll convert it for you.")

@bot.message_handler(func=lambda msg: True)
def convert_terabox_link(message):
    terabox_link = message.text.strip()
    if terabox_link in terabox_to_direct:
        direct_link = terabox_to_direct[terabox_link]
        bot.reply_to(message, f"Direct download link: {direct_link}")
    else:
        bot.reply_to(message, "Invalid Terabox link. Please try again.")

if __name__ == "__main__":
    bot.polling()
