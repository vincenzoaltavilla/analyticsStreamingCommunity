import configparser
# import json
import re
# from datetime import date, datetime
from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
from telethon.tl.functions.messages import (GetHistoryRequest)
from telethon.tl.types import (PeerChannel)

# some functions to parse json date
'''
class DateTimeEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.isoformat()

        if isinstance(o, bytes):
            return list(o)

        return json.JSONEncoder.default(self, o)
'''


async def get_url():
    # Reading Configs
    config = configparser.ConfigParser()
    config.read("config.ini")

    # Setting configuration values
    api_id = config['Telegram']['api_id']
    api_hash = config['Telegram']['api_hash']
    api_hash = str(api_hash)
    phone = config['Telegram']['phone']
    username = config['Telegram']['username']

    # Creating a Telegram client
    client = TelegramClient(username, api_id, api_hash)
    await client.start()
    # print("Client Created")

    # Ensure you're authorized
    iua = await client.is_user_authorized()
    if not iua:
        await client.send_code_request(phone)
        try:
            await client.sign_in(phone, input('Enter the code: '))
        except SessionPasswordNeededError:
            await client.sign_in(password=input('Password: '))

    # Connecting with the Telegram channel
    user_input_channel = "1393252619"
    if user_input_channel.isdigit():
        entity = PeerChannel(int(user_input_channel))
    else:
        entity = user_input_channel
    my_channel = await client.get_entity(entity)

    # Getting History object with the list of messages
    offset_id = 0
    limit = 100
    all_messages = []
    # total_messages = 0
    total_count_limit = 0

    while True:
        # if total_messages != 0:
        #   print("Current Offset ID is:", offset_id, "; Total Messages:", total_messages)

        history = await client(GetHistoryRequest(
            peer=my_channel,
            offset_id=offset_id,
            offset_date=None,
            add_offset=0,
            limit=limit,
            max_id=0,
            min_id=0,
            hash=0
        ))
        if not history.messages:
            break

        messages = history.messages

        for message in messages:
            all_messages.append(message.to_dict())

        offset_id = messages[len(messages) - 1].id
        total_messages = len(all_messages)

        if total_count_limit != 0 and total_messages >= total_count_limit:
            break

    # with open('channel_messages.json', 'w') as outfile:
    #     json.dump(all_messages, outfile, cls=DateTimeEncoder)

    # Getting the message with the URL from the list of messages
    all_messages = str(all_messages)
    list_mex = all_messages.split()
    domain = "Not found"

    for elem in list_mex:
        if "//streamingcommunity." in elem:
            domain = elem
            break

    pattern = r"'(http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+)'"

    # Finding pattern in the string
    match = re.search(pattern, domain)

    if match:
        # Getting URL
        url = match.group(1)
        return url
    else:
        return "Not found"