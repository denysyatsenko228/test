# Крестики - нолики

import random

def drawBoard(board):
    # Выводит на экран игровое поле

    # board - список из 10 строк(индекс 0 - игнорируеться)
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])

def inputPlayerLetter():
    # Ввод выбранной играком буквы
    # Список где буква игрока - 1 элемент, буква компьютера - 2
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Вы выбираете Х или O?')
        letter = input().upper()

    # text
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def whoGoesFirst():

    if random.randint(0, 1) == 0:
        return 'PC'
    else:
        return 'Владик-лох'

def makeMove(board, letter, move):
    board[move] = letter

def isWinner(bo, le):
    # True, если игрок выиграл(bo - board, le - letter)

    return ((bo[7] == le and bo[8] == le and bo[9] == le)or #через верх
    (bo[4] == le and bo[5] == le and bo[6] == le) or
    (bo[1] == le and bo[2] == le and bo[3] == le) or
    (bo[7] == le and bo[4] == le and bo[1] == le) or
    (bo[8] == le and bo[5] == le and bo[2] == le) or
    (bo[9] == le and bo[6] == le and bo[3] == le) or
    (bo[7] == le and bo[5] == le and bo[3] == le) or
    (bo[9] == le and bo[5] == le and bo[1] == le))

def getBoardCopy(board):
    #Копирует поле и возвр его
    boardCopy = []
    for i in board:
        boardCopy.append(i)
    return boardCopy

def isSpaceFree(board, move):
    # True, если сделан ход в свободную клетку
    return board[move] == ' '

def getPlayerMove(board):
    # Разришает игроку сделать ход
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('Ваш следующий ход? (1 - 9)')
        move = input()
    return int(move)

def chooseRandomMoveFromList(board, movesList):
    # Возвращает допустимый ход,
    # Возвращает значение None, если больше нет допустимых ходов
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def getComputerMove(board, computerLetter):

    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    # Это алгоритм для ИИ крестиков - ноликов
    # Сначала проверяем победим ли мы сделав след ход
    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, computerLetter, i)
            if isWinner(boardCopy, computerLetter):
                return i

    # Проверяем победит ли игрок
    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, playerLetter, i)
            if isWinner(boardCopy, playerLetter):
                return i

    # Пробуем занять 1 из углов если есть свободные
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move

    # пробуем занять центр
    if isSpaceFree(board, 5):
        return 5

    # Делаем ход по одной стороне
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])

def isBoardFull(board):
    # True, если если клетка занята. В противном случае False
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True


print('Игра "Крестики-нолики"')

while True:
    # Reload
    theBoard = [' '] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('' + turn + ' ходит первым.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'Man':
            # Ход игрока
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('Ура! Вы выиграли!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('Ничья!')
                    break
                else:
                    turn = 'PC'

        else:
            # Ход ПК
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)

            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('PC win! You are lose!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('Ничья!')
                else:
                    turn = 'Man'

    print('Сыграем еще? да или нет?')
    if not input().lower().startswith('д'):
        break









