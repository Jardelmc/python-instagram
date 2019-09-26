from aiohttp import web
import asyncio
import threading

from login import loginService
from create_user import create_user
from get_users_from_node import get_users_from_hashtags, get_users, get_users_from_provider
from follow import followDialy
from unfollow import unfollowDialy
import teste

routes = web.RouteTableDef()


loggedProfiles = {}

###################################################################################
@routes.post('/login')
async def login(request):

    data = await request.json()
    username = data['login']
    password = data['password']

    bot = loginService.login(username, password)
    if bot != False:
        loggedProfiles[bot.user_id] = bot
        userId = {'userId': bot.user_id}
        return web.json_response(userId)

# Rota para retornar dados de usuário
###################################################################################
@routes.post('/users/create')
async def createUser(request):
    data = await request.json()
    userId = data['userId']

    bot = loggedProfiles[userId]

    user = create_user.createNewUser(bot)

    return web.json_response(user)

###################################################################################
@routes.post('/usersByHashtags')
async def getManyUsers(request):

    data = await request.json()

    userId = data['userId']
    hashtags = data['hashtags']

    bot = loggedProfiles[userId]

    listOfUsersWithHashtags = get_users_from_hashtags.getUsersFromHashTag(
        bot, hashtags)

    return web.json_response(listOfUsersWithHashtags)

####################################################################################
@routes.post('/usersByUsername')
async def getUsersFromTargetUsername(request):
    data = await request.json()

    userId = data['userId']
    targetProfile = data['targetProfile']

    bot = loggedProfiles[userId]

    listOfUserFollowers = get_users_from_provider.getUsersByUsername(
        bot, targetProfile)

    return web.json_response(listOfUserFollowers)

app = web.Application()

app.router.add_routes(routes)
#app.add_routes([web.post('/login', login)])

web.run_app(app)
