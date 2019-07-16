# coding: utf-8

import requests
import json

from slackbot.bot import respond_to
from slackbot.bot import listen_to
from slackbot.bot import default_reply

import slackbot_settings


@default_reply()
def default_func(message):
    query = message.body['text']
    response = requests.post(
        slackbot_settings.TALK_API_URL,
        {
            'apikey': slackbot_settings.TALK_API_KEY,
            'query': query
        }
    )
    if response.status_code != 200:
        message.reply('よくわかりませんでした')
    else:
        message.reply(response.json()['results'][0]['reply'])
