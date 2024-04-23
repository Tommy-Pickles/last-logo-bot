from telegram.ext import Updater, CommandHandler, MessageHandler, filters

from PIL import Image

# Define your bot token
TOKEN = '6376369294:AAEbHILI4rC-R7q-f-cZLg-FqEW8QRrkS4g'

# Define the path to your logo image
LOGO_IMAGE_PATH = '/Users/tg-bots/last-logo-bot/last-logo-60-transparent.png'

# Define handler for the /start command
def start(update, context):
    update.message.reply_text("Welcome to the Image Bot! Send me an image and I'll add a logo to it.")

# Define handler for processing images
def process_image(update, context):
    # Get the photo that user sent
    photo = update.message.photo[-1].get_file()

    # Download the photo
    photo_path = 'user_photo.jpg'
    photo.download(photo_path)

    # Open the photo using Pillow
    image = Image.open(photo_path)

    # Open the logo image using Pillow
    logo = Image.open(LOGO_IMAGE_PATH)

    # Calculate position to place the logo (bottom right corner)
    position = (image.width - logo.width, image.height - logo.height)

    # Paste the logo onto the image
    image.paste(logo, position, logo)

    # Save the new image
    new_image_path = 'processed_image.jpg'
    image.save(new_image_path)

    # Send the processed image back to the user
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(new_image_path, 'rb'))

# Define main function
def main():
    # Create the Updater and pass in the bot's token
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Register command handlers
    dp.add_handler(CommandHandler("start", start))

    # Register message handler for images
    dp.add_handler(MessageHandler(filters.Filters.photo, process_image))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C
    updater.idle()

# Run the main function
if __name__ == '__main__':
    main()
