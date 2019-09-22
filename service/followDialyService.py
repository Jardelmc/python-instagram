from instabot import Bot
import argparse
import requests
import os
import sys
import json
import random
import time
import datetime

sys.path.append(os.path.join(sys.path[0], "../"))

parser = argparse.ArgumentParser(add_help=True)
parser.add_argument("-u", type=str, help="username")
parser.add_argument("-p", type=str, help="password")
parser.add_argument("-proxy", type=str, help="proxy")

args = parser.parse_args()


def getHeaders(token):
    token = 'Bearer {}'.format(token)

    headers = {"Authorization": token}

    return headers

# usuarios = [{'login': 'gatopagina', 'token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyUGsiOjIwNTMyMDIxMDE1LCJsb2dpbiI6ImdhdG9wYWdpbmEiLCJpYXQiOjE1Njg4NzExNDF9.dvV2nHANjdnn9VpNOgl_ISPIwMsZtS11Zo_3UVzIRh4'}]


user = 'gatopagina'
token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyUGsiOjIwNTMyMDIxMDE1LCJsb2dpbiI6ImdhdG9wYWdpbmEiLCJpYXQiOjE1Njg4NzExNDF9.dvV2nHANjdnn9VpNOgl_ISPIwMsZtS11Zo_3UVzIRh4'

server_url = 'http://localhost:3334'


def getListOfProfileIds():
    response = requests.get(
        '{}/getfollow'.format(server_url), headers=getHeaders(token))

    listOfIds = json.loads(response.content)

    formattedList = []

    for profile in listOfIds:
        for pk in profile['profiles']:
            if pk not in formattedList:
                formattedList.append(pk)

    return formattedList


secondsInOneDay = 57600


def runFollowService(bot):
    print('Iniciando serviço de Follow Diário às {}'.format(
        datetime.datetime.now()))

    # Lista de perfis para serem seguidos no dia
    listOfProfilesId = getListOfProfileIds()

    # Segundos médios entre seguidas baseado na quantidade diária
    meansSecondBetweenFollows = secondsInOneDay / len(listOfProfilesId)

    while len(listOfProfilesId) > 0:
        # Escolhendo numero de perfis a serem seguidos por safra
        profilesPerSafra = random.randint(5, 16)
        print('Safra atual é de {} perfis para serem seguidos'.format(profilesPerSafra))

        # Fazendo o loop para seguir a quantidade selecionada por safra
        for i in range(profilesPerSafra):
             # Sorteando um perfil aleatório na lista diária
            profileSorted = random.choice(listOfProfilesId)

            # Mandando seguir
            bot.follow(profileSorted)

            # Removendo usuário seguido da lista principal
            listOfProfilesId.remove(profileSorted)

            # Dormingo por mini follow
            timeSleepInMs = random.uniform(11, 25)
            time.sleep(timeSleepInMs)

        print('Fim da safra atual, ainda restam {} perfis'.format(
            len(listOfProfilesId)))

        # Média de segudos * quantidade de perfis por safra
        timeSleepBetweenSafra = meansSecondBetweenFollows * profilesPerSafra

        # Randomizando 70 segundos para + ou -
        timeSleepBetweenSafra = random.uniform(
            (timeSleepBetweenSafra - 70), (timeSleepBetweenSafra + 70))

        timeOfEnd = datetime.datetime.now()
        print('O sistema vai dormir por {} minutos a partir de agora. HORA: {}'.format(
            timeSleepBetweenSafra/60, timeOfEnd))

        time.sleep(timeSleepBetweenSafra)  # Sleep


def init(username, password):
    try:
        os.mkdir('./payload')
        os.mkdir('./payload/{}'.format(username))
    except:
        pass
    whitelist_file = "./payload/{}/whitelist.txt".format(username)
    blacklist_file = "./payload/{}/blacklist.txt".format(username)
    comments_file = "./payload/{}/comments.txt".format(username)
    followed_file = "./payload/{}/followed.txt".format(username)
    unfollowed_file = "./payload/{}/unfollowed.txt".format(username)
    skipped_file = "./payload/{}/skipped.txt".format(username)
    friends_file = "./payload/{}/friends.txt".format(username)

    bot = Bot(filter_private_users=False,
              whitelist_file=whitelist_file, blacklist_file=blacklist_file, comments_file=comments_file, followed_file=followed_file, unfollowed_file=unfollowed_file, skipped_file=skipped_file, friends_file=friends_file)
    bot.login(username=username, password=password)
    runFollowService(bot)


init('gatopagina', 'lara1999')
