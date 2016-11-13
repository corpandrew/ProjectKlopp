import json
import urllib.request

from Player import *

players = []
form442 = ['']


def downloadAndParse(i):
    url = 'http://www.easports.com/fifa/ultimate-team/api/fut/item?page=' + str(i)

    jsonFile = urllib.request.urlopen(url)

    with open('fut' + str(i) + '.json', 'wb') as output:
        output.write(jsonFile.read())

    jsonFileString = open('fut' + str(i) + '.json').read()

    jsonObject = json.loads(jsonFileString)

    for player in jsonObject['items']:
        print(player['firstName'] + ' ' + player['lastName'])


def parse(i):
    jsonFileString = open('fut' + str(i) + '.json').read()

    jsonObject = json.loads(jsonFileString)

    for player in jsonObject['items']:
        players.append(
            Player(player['firstName'] + ' ' + player['lastName'], player['nation']['name'], player['club']['name'],
                   player['position']))


#
# for i in range(1,623):
#     parse(i)

vars = "darkLargeImageUrl, normalLargeImageUrl, abbrName, id, imgUrl, name"
for var in vars.split(','):
    print('self.' + var.strip() + ' = ' + var.strip())

for var in vars.split(','):
    print('def get' + var.strip()[0].upper() + var.strip()[1:] + '(self):\nreturn self.' + var.strip())

    # while True:
    #     text = str(input('What would you like to be printed?: '))
    #     if(text.__contains__('name=')):
    #         for player in players:
    #             if (player.getName() == text[5:].strip()):
    #                 print(player)
    #     elif(text.__contains__('form=4-4-2') or text.__contains__('form=442')):
    #         for player in players:
    #             print(player)
    #             # print(team + ' players: \n')
    #             # for player in players:
    #             #     if(player.getTeamName() == team):
    #             #         print(player)
