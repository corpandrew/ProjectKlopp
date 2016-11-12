# import draw_golden as dg
# import turtle
#
# def main():
#     # Get user input for rectangles and spiral.
#     #x_coord, y_coord, length, number, color, spir_color = dg.get_input()
#
#     screen = turtle.Screen()
#
#     # click the image icon in the top right of the code window to see
#     # which images are available in this trinket
#     image = "rocketship.png"
#
#     # add the shape first then set the turtle shape
#     screen.addshape(image)
#     turtle.shape(image)
#
#     # Draw the rectangles and inscribed spiral.
#     #dg.draw_golden(x_coord, y_coord, length, number, color, spir_color)
#     dg.draw_golden(1, 1,1100,10,'red','blue')
#
# main()
#
# turtle.mainloop()

import json
import threading
import urllib.request
from Player import *


milner = Player('James Milner', 7 , 'Liverpool')
coutinho = Player('Philippe Coutinho', 10, 'Liverpool')
mane = Player('Sadio Mane', 19, 'Liverpool')

liverpool = [milner, coutinho, mane]

# print (milner.getName())
# print (coutinho.getName())
# print (mane.getName())


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
        print(player['firstName'] + ' ' + player['lastName'])

for i in range(1,623):
    parse(i)