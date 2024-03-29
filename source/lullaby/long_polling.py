#!/usr/bin/env python3
# coding: utf8


def get_updates(telegram_bot, on_updates, **kwargs):

    last_update_id = None

    while True:

        if last_update_id:
            result = telegram_bot.getUpdates(offset=last_update_id+1, **kwargs)['result']
        else:
            result = telegram_bot.getUpdates(**kwargs)['result']

        if result:
            on_updates(result)
            last_update_id = result[-1]['update_id']
