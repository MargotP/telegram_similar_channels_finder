#!/usr/bin/env python
# coding: utf-8

"""
Telegram Similar Channels Finder Script.

This script uses the Telethon library to interact with Telegram's API. It allows users to find channels
similar to the ones they are interested in on Telegram. Users can provide a list of channel usernames,
and the script will find and display similar channels. This is useful for discovering new content and
communities on Telegram related to the user's interests.
"""

from telethon import TelegramClient, functions, types
import asyncio
from prettytable import PrettyTable
from termcolor import colored
from telethon.errors.rpcerrorlist import RpcCallFailError

__author__ = "H@ckila"
__copyright__ = "Copyright 2023"
__version__ = "1.0.0"
__status__ = "Dev"

# API ID: Your unique Telegram API ID. You can get this from https://my.telegram.org
API_ID = XXXXXXXX

# API Hash: Your unique Telegram API Hash. You can get this from https://my.telegram.org
API_HASH = ''

# Session File Name: The name of the session file to be used by Telethon.
# This file stores your login session to avoid re-logging in.
SESSION_FILE_NAME = 'telegram'

# Proxy Configuration: Configure this if you are behind a proxy.
# The format is a tuple: (proxy_type, hostname, port)
PROXY = ('http', 'proxy.example.com', 3128)

# CHANNELS: List of Telegram channel usernames to find similar channels for.
# Replace the values with the usernames of the channels you are interested in.
# The channel username can be found in the channel's invitation link, e.g., "redteamalerts" in "https://t.me/redteamalerts".
CHANNELS = ['cibsecurity','CyberSecurityTechnologies','socanalyst']

def print_header():
    """
    Prints the header for the application.
    """
    header = """
    ╔════════════════════════════════════════════════════════════════╗
    ║                Telegram Similar Channels Finder                ║
    ║              Find similar Telegram channels easily             ║
    ╚════════════════════════════════════════════════════════════════╝
    """
    print(header)

async def get_channel_id(client, username):
    """
    Retrieves the channel ID from a given username.
    """
    try:
        entity = await client.get_entity(username)
        return entity.id
    except Exception as e:
        print(f"{colored('[!]', 'red')} No channel has {colored(username, 'red')} as username")
        return None

async def safe_api_request(coroutine, comment):
    """
    Safely executes an asynchronous API request.
    """
    try:
        return await coroutine
    except RpcCallFailError as e:
        print(f"{colored('[!]', 'red')} Telegram API error, {comment}: {str(e)}")
    except Exception as e:
        print(f"{colored('[!]', 'red')} General error, {comment}: {str(e)}")
    return None

async def get_similar_channels(client, channel_username):
    """
    Finds similar Telegram channels given a channel username.
    """
    try:
        entity = await client.get_input_entity(channel_username)
        if isinstance(entity, types.InputChannel) or isinstance(entity, types.InputPeerChannel):
            input_channel = types.InputChannel(channel_id=entity.channel_id, access_hash=entity.access_hash)
            result = await safe_api_request(client(functions.channels.GetChannelRecommendationsRequest(channel=input_channel)), 'retrieving channels')
            if not result:
                return None

            similar_channels = []
            for ch in result.chats:
                channel_info = {
                    'username': ch.username,
                    'title': ch.title,
                    'id': ch.id
                }
                similar_channels.append(channel_info)

            return similar_channels
        else:
            print(f"{channel_username} is not a channel.")
            return None
    except Exception as e:
        print(f"Error retrieving similar channels for {channel_username} {e}")
        return None

def print_table(channel_data, username, channel_id):
    """
    Prints the data of similar Telegram channels in a table format.
    """
    table = PrettyTable()
    table.field_names = ["Username", "Title", "ID"]
    table.align = "c"

    for ch in channel_data:
        table.add_row([ch['username'], ch['title'], ch['id']])

    print(f"\n{colored('[INFO]', 'yellow')} Found similar channels for {colored(username, 'green')} / ID = {channel_id}")
    print(table)

async def main(channel_usernames):
    """
    Main function to process a list of Telegram channel usernames and find similar channels.
    """
    print_header()
    client = TelegramClient(SESSION_FILE_NAME, API_ID, API_HASH, proxy=PROXY)

    async with client:
        for username in channel_usernames:
            if not username:
                print(f"{colored('[!]', 'red')} Channel name not provided")
                continue

            channel_id = await get_channel_id(client, username)
            if channel_id is not None:
                similar_channels = await get_similar_channels(client, username)
                if similar_channels:
                    print_table(similar_channels, username, channel_id)
                else:
                    print(f"\n{colored('[INFO]', 'yellow')} No similar channels found for {colored(username, 'yellow')}  / ID = {channel_id}")
            else:
                print(f"{colored('[!]', 'red')} Channel {username} not found or error retrieving the ID.")

if __name__ == "__main__":
    channel_usernames = CHANNELS
    asyncio.run(main(channel_usernames))
