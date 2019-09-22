from instabot import Bot
import os
import sys
import time
import datetime
import random
import requests

sys.path.append(os.path.join(sys.path[0], "../../"))

secondsInOneDay = 60 * 60 * 16  # 16 horas de trabalho


# Metodo para salvar safra atual, para caso de erro, nao perder quem ja foi seguido
def savePartialSafra(userPk, token, safra, nodeServerURL):
    try:
        response = requests.post(
            '{nodeServerURL}/partialSafra', headers=token, data={'safraFollowed': safra})
    except:
        pass


def runFollowService(bot, listOfProfilesId, token, nodeServerURL):
    try:
        print('Iniciando serviço de Follow Diário às {}'.format(
            datetime.datetime.now()))

        # Segundos médios entre seguidas baseado na quantidade diária
        meansSecondBetweenFollows = secondsInOneDay / len(listOfProfilesId)

        # Lista para adicionar todos seguidos
        allFollowedProfiles = []

        while len(listOfProfilesId) > 0:
            # Escolhendo numero de perfis a serem seguidos por safra
            profilesPerSafra = random.randint(5, 16)

            # Para nao quebrar o ciclo de index do vetor
            if profilesPerSafra >= len(listOfProfilesId):
                profilesPerSafra = len(listOfProfilesId) - 1

            print('Safra atual é de {} perfis para serem seguidos'.format(
                profilesPerSafra))

            partialSafra = []
            # Fazendo o loop para seguir a quantidade selecionada por safra
            for i in range(profilesPerSafra):
                  # Sorteando um perfil aleatório na lista diária
                profileSorted = random.choice(listOfProfilesId)

                # Mandando seguir
                bot.follow(profileSorted)

                # Adicionando usuario seguido na safra parcial
                partialSafra.append(profileSorted)

                # Removendo usuário seguido da lista principal
                listOfProfilesId.remove(profileSorted)

                # Dormingo por mini follow
                timeSleepInMs = random.uniform(11, 25)
                time.sleep(timeSleepInMs)

            print('Fim da safra atual, ainda restam {} perfis'.format(
                len(listOfProfilesId)))

            # Salvando safra temporaria
            savePartialSafra(bot.user_id, token, partialSafra, nodeServerURL)

            # Adicionando safra atual a lista de todos perfis seguidos
            allFollowedProfiles.append(partialSafra)

            # Média de segudos * quantidade de perfis por safra
            timeSleepBetweenSafra = meansSecondBetweenFollows * profilesPerSafra

            # Randomizando 70 segundos para + ou -
            timeSleepBetweenSafra = random.uniform(
                (timeSleepBetweenSafra - 70), (timeSleepBetweenSafra + 70))

            timeOfEnd = datetime.datetime.now()
            print('O sistema vai dormir por {} minutos a partir de agora. HORA: {}'.format(
                int(timeSleepBetweenSafra/60), timeOfEnd))

            time.sleep(timeSleepBetweenSafra)  # Sleep

        try:
            requests.post('{nodeServerURL}/endDialyFollow', headers=token,
                          data={'followedProfiles': allFollowedProfiles})
        except:
            print('Erro ao enviar lista de Dialy Follow. HORA: {}'.format(
                datetime.datetime.now()))

    except:
        return False


def savePartialSafra(userPk, token, safra, nodeServerURL):
    response = requests.post('{nodeServerURL}/partialSafra', headers=token)
