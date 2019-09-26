import datetime
import requests
import time

NODE_SERVER = 'http://localhost:3334'

token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyUGsiOiIyMDUzMjAyMTAxNSIsImxvZ2luIjoiZ2F0b3BhZ2luYSIsImlhdCI6MTU2OTQ2MDU2NX0.syK4AELiyOowUV2J711380xK7tgYcr8wuqGQf92t6ko'


def getHeaders(token):
    token = 'Bearer {}'.format(token)

    headers = {"Authorization": token}

    return headers


# 3
dayControl = 0
activedInThisDay = False

while True:
    dayVigent = datetime.datetime.now()

    # Se o dia for diferente, indica que preciso executar ação
    if dayVigent.day != dayControl:
        # Atualizo variável de controle para não repetir no mesmo dia
        dayControl = dayVigent.day
        # Setando hora de inicio
        if datetime.datetime.now().hour == 22:
            print('INICIANDO SERVIÇO -- HORA: {}'.format(datetime.datetime.now()))
            headers = getHeaders(token)
            # Request para Follow Dialy
            requests.get('{}/getFollow'.format(NODE_SERVER), headers=headers)
            requests.get('{}/getUnfollow'.format(NODE_SERVER), headers=headers)

    time.sleep(60 * 30)  # 30 min
    print('Nada executado')
