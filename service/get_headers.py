def getHeaders(token):
    token = 'Bearer {}'.format(token)

    headers = {"Authorization": token}

    return headers
