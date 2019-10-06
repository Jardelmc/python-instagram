from instabot import Bot
import os
import sys
import time
import datetime
import random
import requests
import json

sys.path.append(os.path.join(sys.path[0], "../../"))

secondsInOneDay = 60 * 60 * 16  # 16 horas de trabalho


# Metodo para salvar safra atual, para caso de erro, nao perder quem ja foi seguido
def savePartialSafra(userPk, headers, safra, nodeServerURL):
    if len(safra) == 0:
        print('Nenhum perfil foi seguido nesta safra, requisição POST não será realizada')
        return

    try:
        data = {'safra': safra}

        response = requests.post(
            '{}/partialSafra'.format(nodeServerURL), headers=headers, json=data)

        if response.status_code == 200:
            print('Safra salva com sucesso no servidor NODE')
        else:
            print('Falha ao salvar a safra')
            print(response.text)
    except Exception as e:
        print('Falha no try-cath da função savePartialSafra -- FollowDialy')
        print(e)
        pass


def runFollowService(bot, listOfProfilesId, headers, nodeServerURL):
    try:
        print('Iniciando serviço de Follow Diário às {}'.format(
            datetime.datetime.now()))

        # Segundos médios entre seguidas baseado na quantidade diária
        meansSecondBetweenFollows = secondsInOneDay / len(listOfProfilesId)

        # Lista para adicionar todos seguidos
        allFollowedProfiles = []

        # Para contar quantos perfis foram seguidos
        countFollowedProfiles = 0

        while len(listOfProfilesId) > 0:
            # Escolhendo numero de perfis a serem seguidos por safra
            profilesPerSafra = random.randint(8, 16)

           # profilesPerSafra = 2  # TESTE --------- REMOVER LINHA

            # Para nao quebrar o ciclo de index do vetor
            if profilesPerSafra >= len(listOfProfilesId):
                profilesPerSafra = len(listOfProfilesId) - 1

            print('Safra atual é de {} perfis para serem seguidos'.format(
                profilesPerSafra))

            # Variável para salvar todos perfis que deram sucesso ao seguir
            partialSafra = []

            # Fazendo o loop para seguir a quantidade selecionada por safra
            for i in range(profilesPerSafra):

                # Sorteando um perfil aleatório na lista diária
                profileSorted = random.choice(listOfProfilesId)
                print('PROFILE SORTED: {}'.format(profileSorted))

                # Mandando seguir | Retorna True ou False de acordo com o sucesso no follow
                checkIfHasFollow = bot.follow(profileSorted)

                if checkIfHasFollow == True:
                    # Adicionando usuario seguido na safra parcial
                    partialSafra.append(profileSorted)

                    countFollowedProfiles += 1
                    print(
                        'USER> {} -- PERFIS SEGUIDOS HOJE: {}'.format(bot.username, countFollowedProfiles))

                    # Dormingo por mini follow quando dá sucesso
                    timeSleepInMs = random.uniform(11, 25)
                    time.sleep(timeSleepInMs)

                # Removendo usuário seguido da lista principal
                listOfProfilesId.remove(profileSorted)

            print('Fim da safra atual, ainda restam {} perfis'.format(
                len(listOfProfilesId)))

            # Salvando safra temporaria
            savePartialSafra(bot.user_id, headers, partialSafra, nodeServerURL)

            # Média de segudos * quantidade de perfis seguidos com sucesso por safra
            timeSleepBetweenSafra = meansSecondBetweenFollows * \
                len(partialSafra)

            # Randomizando 70 segundos para + ou -
            timeSleepBetweenSafra = random.uniform(
                (timeSleepBetweenSafra - 650), (timeSleepBetweenSafra + 650))

            timeOfEnd = datetime.datetime.now()
            print('USER> {} -- FOLLOW DIALY -- O sistema vai dormir por {} minutos a partir de agora. HORA: {}'.format(
                bot.username, int(timeSleepBetweenSafra/60), timeOfEnd))

            time.sleep(timeSleepBetweenSafra)  # Sleep

            # Mecanismo de segurança
            if countFollowedProfiles == 59 or countFollowedProfiles == 119 or countFollowedProfiles == 179:
                print(
                    'PAUSA DE 3 HORAS A CADA 60 PERFIS SEGUIDOS - INÍCIO: {}'.format(datetime.datetime.now()))
                time.sleep(60 * 60 * 3)  # Pausa de 3 horas

        now = datetime.datetime.now()
        print('TÉRMINO DE DIALY FOLLOW -- USER> {} - QTD PERFIS SEGUIDOS: {} - HORA: {}'.format(
            bot.username, countFollowedProfiles, now))

    except:
        now = datetime.datetime.now()
        print('Erro no serviço de follow dialy -- USER> {} -- HORA: {}'.format(bot.username, now))
        return False
