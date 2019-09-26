from instabot import Bot
import os
import sys
import time
import datetime
import random
import json

sys.path.append(os.path.join(sys.path[0], "../../"))

# Recebe uma lista ["message", "userId"]


def sendDirect(bot, malote):

    print("Iniciando envio de Direct -- USER> {} -- HORA: {}".format(bot.username,
                                                                     datetime.datetime.now()))

    while len(malote) > 0:
        instance = random.choice(malote)

        print('USER> {} - Mandando mensagem para {} - Mensagem: {}'.format(
            bot.username, instance['userId'], instance['message']))

        # Enviando mensagem
        bot.send_message(instance['message'], instance['userId'])
        print('Mensagem enviada às {}'.format(datetime.datetime.now()))

        malote.remove(instance)

        timeSleepInMs = random.uniform(20, 30)
        time.sleep(timeSleepInMs)

    print('USER> {} -- Remessa e direct acabou -- HORA> {}'.format(bot.username,
                                                                   datetime.datetime.now()))
