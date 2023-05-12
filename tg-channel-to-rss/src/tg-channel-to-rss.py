import os
import json
import logging
import telegram
import feedgen.feed
import feedgen.util
import azure.functions as func


def main(mytimer: func.TimerRequest) -> None:

    # Read in configuration values from environment variables
    telegram_channel = os.environ['TELEGRAM_CHANNEL_ID']
    telegram_token = os.environ['TELEGRAM_BOT_TOKEN']
    rss_feed_url = os.environ['RSS_FEED_URL']

    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    logging.getLogger('telegram').setLevel(level=logging.WARNING)

    try:
        # Initialize Telegram bot
        bot = telegram.Bot(token=telegram_token)
        logging.info(bot.get_me())

        # Fetch messages from Telegram channel
        messages = bot.get_chat_messages(chat_id=telegram_channel)

        # Create feed and add messages as entries
        feed = feedgen.feed.FeedGenerator()
        feed.id(rss_feed_url)
        feed.title('Telegram Channel')
        feed.author({'name': 'Telegram Channel'})
        feed.link(href=rss_feed_url, rel='self')
        for message in messages:
            entry = feed.add_entry()
            entry.id(str(message.message_id))
            entry.title(str(message.date))
            entry.description(str(message.text))
            entry.link(href='t.me/{}/{}'.format(telegram_channel, message.message_id))
            entry.pubdate(feedgen.util.parsedate_to_datetime(message.date))

        # Writing feed to disk
        feed.rss_file('rss.xml')

        logging.info('RSS feed written to rss.xml')
    
    except Exception as e:
        logging.error(str(e))