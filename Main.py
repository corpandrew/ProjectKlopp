import json
import urllib.request

from Player import *
from League import *
from Nation import *
from Club import *

commonName = None
firstName = None
headshotImgUrl = None
lastName = None

league = None
nation = None
club = None

largeTOTWImgUrl = None
position = None
playStyle = None
playStyleId = None
height = None
weight = None
birthdate = None
age = None
aggression = None
agility = None
balance = None
ballcontrol = None
foot = None
skillMoves = None
crossing = None
curve = None
dribbling = None
finishing = None
freekickaccuracy = None
gkdiving = None
gkhandling = None
gkpositioning = None
gkreflexes = None
headingaccuracy = None
interceptions = None
jumping = None
longpassing = None
longshots = None
marking = None
penalties = None
positioning = None
potential = None
reactions = None
shortpassing = None
shotpower = None
slidingtackle = None
stamina = None
strength = None
vision = None
volleys = None
weakfoot = None

traits = []
specialties = []
attributes = []

name = None
quality = None
color = None
isGk = None
positionFull = None
isSpecialType = None
contracts = None
fitness = None
rawAttributeChemistryBonus = None
isLoan = None
squadPosition = None
itemType = None
discardValue = None
id = None
modelName = None
baseId = None
rating = None

players = []

formation3412 = ['ST', 'ST', 'LM', 'CAM', 'RM', 'CM', 'CM', 'CB', 'CB', 'CB', 'GK']
formation3421 = ['LF', 'ST', 'RF', 'LM', 'CM', 'CM', 'RM', 'CB', 'CB', 'CB', 'GK']
formation343 = ['LW', 'ST', 'RW', 'LM', 'CM', 'CM', 'RM', 'CB', 'CB', 'CB', 'GK']
formation352 = ['ST', 'ST', 'LM', 'CAM', 'RM', 'CDM', 'CDM', 'CB', 'CB', 'CB', 'GK']

formation442 = ['ST', 'ST', 'LM', 'CM', 'CM', 'RM', 'LB', 'CB', 'CB', 'RB', 'GK']
formation433 = ['LW', 'ST', 'RW', 'LM', 'CM', 'RM', 'LB', 'CB', 'CB', 'RB', 'GK']
playersUsed = []


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
    jsonFileString = open('FUTS/fut' + str(i) + '.json').read()

    jsonObject = json.loads(jsonFileString)

    for p in jsonObject['items']:
        commonName = p['commonName']
        firstName = p['firstName']
        headshotImgUrl = p['headshotImgUrl']
        lastName = p['lastName']

        league = League(p['league']['abbrName'], p['league']['id'], p['league']['imgUrl'], p['league']['name'])
        nation = Nation(p['nation']['imageUrls']['large'], p['nation']['abbrName'], p['nation']['id'], None,
                        p['nation']['name'])
        club = Club(p['club']['imageUrls']['dark']['large'], p['club']['imageUrls']['normal']['large'],
                    p['club']['abbrName'], p['club']['id'], p['club']['imgUrl'], ['name'])

        largeTOTWImgUrl = p['specialImages']['largeTOTWImgUrl']
        position = p['position']
        playStyle = p['playStyle']
        playStyleId = p['playStyleId']
        height = p['height']
        weight = p['weight']
        birthdate = p['birthdate']
        age = p['age']
        aggression = p['aggression']
        agility = p['agility']
        balance = p['balance']
        ballcontrol = p['ballcontrol']
        foot = p['foot']
        skillMoves = p['skillMoves']
        crossing = p['crossing']
        curve = p['curve']
        dribbling = p['dribbling']
        finishing = p['finishing']
        freekickaccuracy = p['freekickaccuracy']
        gkdiving = p['gkdiving']
        gkhandling = p['gkhandling']
        gkpositioning = p['gkpositioning']
        gkreflexes = p['gkreflexes']
        headingaccuracy = p['headingaccuracy']
        interceptions = p['interceptions']
        jumping = p['jumping']
        longpassing = p['longpassing']
        longshots = p['longshots']
        marking = p['marking']
        penalties = p['penalties']
        positioning = p['positioning']
        potential = p['potential']
        reactions = p['reactions']
        shortpassing = p['shortpassing']
        shotpower = p['shotpower']
        slidingtackle = p['slidingtackle']
        stamina = p['stamina']
        strength = p['strength']
        vision = p['vision']
        volleys = p['volleys']
        weakfoot = None

        # for value in p['traits']:
        #     traits.append(str(value))

        # for value in p['specialties']:
        #     specialties.append(str(value))
        # specialties = None
        # for value in p['attributes']:
        #     attributes.append(str(value))

        name = p['name']
        quality = p['quality']
        color = p['color']
        isGk = None
        positionFull = p['positionFull']
        isSpecialType = p['isSpecialType']
        contracts = p['contracts']
        fitness = p['fitness']
        rawAttributeChemistryBonus = p['rawAttributeChemistryBonus']
        isLoan = p['isLoan']
        squadPosition = p['squadPosition']
        itemType = p['itemType']
        discardValue = p['discardValue']
        id = p['id']
        modelName = p['modelName']
        baseId = p['baseId']
        rating = p['rating']
        players.append(
            Player(commonName, firstName, headshotImgUrl, lastName, league, nation, club, largeTOTWImgUrl, position,
                   playStyle, playStyleId, height, weight, birthdate, age, aggression, agility, balance, ballcontrol,
                   foot, skillMoves, crossing, curve, dribbling, finishing, freekickaccuracy, gkdiving, gkhandling,
                   gkpositioning, gkreflexes, headingaccuracy, interceptions, jumping, longpassing, longshots, marking,
                   penalties, positioning, potential, reactions, shortpassing, shotpower, slidingtackle, stamina,
                   strength, vision,
                   volleys, weakfoot, traits, specialties, attributes, name, quality, color, isGk, positionFull,
                   isSpecialType, contracts, fitness, rawAttributeChemistryBonus, isLoan, squadPosition, itemType,
                   discardValue, id, modelName, baseId, rating))


for i in range(1, 623):
    parse(i)

while True:
    text = str(input('What would you like to be printed?: '))
    if (text.__contains__('name=')):
        for player in players:
            if ((str(player.getFirstName()) + ' ' + str(player.getLastName())).__contains__(text[5:].strip())):
                print(str(player.getFirstName()) + ' ' + str(player.getLastName()) + '\t' + str(player.getPosition()))
    elif (text.__contains__('form=') or text.__contains__('form=')):
        # Andrew fix this please, it finds lousy players.
        searchText = text.split('form=')[1]
        teamToMake = str(input('Which team would you like to create the ' + searchText + ' formation for?: '))
        print(searchText)
        print(teamToMake)
        formationToCreate = None

        for i in range(0, 20):
            print('---------------------------------- Team = ' + str(i) + ' ----------------------------------\n\n\n')
            playersToMake = []
            formation442 = ['ST', 'ST', 'LM', 'CM', 'CM', 'RM', 'LB', 'CB', 'CB', 'RB', 'GK']
            formation433 = ['LW', 'ST', 'RW', 'LM', 'CM', 'RM', 'LB', 'CB', 'CB', 'RB', 'GK']
            formation343 = ['LW', 'ST', 'RW', 'LM', 'CM', 'CM', 'RM', 'CB', 'CB', 'CB', 'GK']

            if (searchText == '442'):
                formationToCreate = formation442
            elif (searchText == '433'):
                formationToCreate = formation433
            elif (searchText == '343'):
                formationToCreate = formation343

            for i in range(len(formationToCreate)):
                for j in range(len(players) - 1):
                    if (len(formationToCreate) != 0):
                        if (str(players[j].getPosition()) ==
                                formationToCreate[i] and str(players[j].getNation().getAbbrName()) == str(teamToMake)):
                            if not (playersUsed.__contains__(players[j].getBaseId())):
                                playersToMake.append(players[j])
                                formationToCreate.pop(i)
                                playersUsed.append(players[j].getBaseId())
                    else:
                        break
            for player in playersToMake:
                print(str(player.getFirstName()) + ' ' + str(player.getLastName()) + '\t' + str(
                    player.getPosition()) + '\t' + str(player.getRating()))

