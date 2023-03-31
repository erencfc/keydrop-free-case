# import asyncio
# import websockets


# async def listen(websocket_uri):
#     async with websockets.connect(websocket_uri) as websocket:
#         while True:
#             message = await websocket.recv()
#             print(f"Received message: {message}")

# websocket_uri = "wss://kdrp3.com/socket.io/?connection=battle&EIO=4&transport=websocket"

# asyncio.run(listen(websocket_uri))

from time import sleep
import json
import requests


url = "https://kdrp2.com/CaseBattle/battle?type=active&page=0&priceFrom=0&priceTo=0.29&searchText=&sort=priceAscending&players=all&roundsCount=all"
joinUrlBase = "https://kdrp2.com/CaseBattle/joinCaseBattle/"

headers = {
    'authorization': 'Bearer token'
}

while True:
    response = requests.request("GET", url, headers=headers)

    res = json.loads(response.text)
    cases = res['data']

    for case in cases:
        isFreeBattle = case['isFreeBattle']
        users = case['users']
        maxUserCount = case['maxUserCount']

        if isFreeBattle and len(users) != maxUserCount:
            print(case['id'])
            joinUrlCase = joinUrlBase + str(case['id'])
            joinResponse = requests.request(
                "POST", joinUrlCase+'/1', headers=headers)
            print(joinResponse.text)
            sleep(2)
    sleep(3)
