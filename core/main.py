#!/usr/bin/env python3
"""
Module: Runs bot client
"""

import core.bot as bot
import os

def bot_client():
  bot_secret = os.environ['BOTTOKEN']
  bot.client.run(bot_secret)

if __name__ == "__main__":
    """ This is executed when run from the command line """
    bot_client()