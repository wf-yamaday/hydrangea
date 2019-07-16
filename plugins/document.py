# coding: utf-8

from slacker import Slacker
from slackbot.bot import respond_to

import requests
import os

import slackbot_settings

prefix = os.path.join(os.getcwd(), 'static')
channel_name = 'chatbot'


@respond_to('運動会')
@respond_to('体育祭の資料')
def reply_hello(message):
    user = message.body['user']
    response = requests.get(slack_api_url(slackbot_settings.API_TOKEN, user))
    print(prefix)
    if response.status_code != 200:
        message.reply('よくわかりませんでした')
    else:
        role = response.json()['user']['profile']['title']
        if role == '教務':
            file = os.path.join(prefix, '体育祭')
            slacker = Slacker(slackbot_settings.API_TOKEN)
            slacker.files.upload(file_=file+'/'+role +
                                 '/Readme.md', channels=channel_name)
            # message.send(reply_message(role))
        elif role == '':
            file = os.path.join(prefix, '体育祭')
            slacker = Slacker(slackbot_settings.API_TOKEN)
            slacker.files.upload(file_=file+'/'+'体育祭.md',
                                 channels=channel_name)
            message.reply('体育祭の資料です')


def slack_api_url(token, id):
    return 'https://slack.com/api/users.info?token={}&user={}&pretty=1'.format(token, id)


def reply_message(role):
    return '{}の体育祭の資料です'.format(role)
