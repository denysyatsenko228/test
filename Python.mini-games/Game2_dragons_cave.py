import random
import time


def displayIntro():
    print('''Вы находитесь в землях, заселенных драконами.
    Перед собой вы видите две пещеры. В одной из них- дружелюбный дракон,
    который готов поделиться сокровищами. Во второй - 
    жадный и голодный дракон, который мигом вас сьест''')
    print()


def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print('В какую пещеру вы пойдете?(Нажмите 1 или 2)')
        cave = input()

    return cave


def checkCave(chosenCave):
    print('Вы приближаетесь к пещере...')
    time.sleep(3)
    print('Ее темнотоа заставляет вас дрожать от страха...')
    time.sleep(3)
    print('Большой дракон выпрыгивает перед вами! Он раскрывает свою пасть и...')
    print()
    time.sleep(5)

    friendlyCave = random.randint(1, 2)

    if chosenCave == str(friendlyCave):
        print('... делится с вами сокровищами!')
    else:
        print('... моментально вас съедает!')


playAgain = 'ДА'
while playAgain == 'ДА' or playAgain == 'да':
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)

    print('Попытаете удачу еще раз? (да или нет)')
    playAgain = input()
