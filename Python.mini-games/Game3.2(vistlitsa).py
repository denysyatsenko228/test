import random

HANGMAN_PICS = ['''
    +---+
        |
        |
        |
        ==''', '''
    +---+
    0   |
        |
        |
        ==''', '''
    +---+
    0   |
    |   |
        ==''', '''
    +---+
    0   |
   /|   |
        |
        ==''', '''
    +---+
    0   |
   /|\  |
        |
        ==''', '''
    +---+
    0   |
   /|\  |
   /    |
        ==''', '''
    +---+
    0   |
   /|\  |
   / \  |
        ==''', '''
    +---+
   [0   |
   /|\  |
   / \  |
        ==''', '''
    +---+
   [0]  |
   /|\  |
   / \  |
        ==''']
words = {'Цвета':'красный оранжевый желтый зеленый синий голубой '
                 'фиолетовый белый черный коричневый'.split(),
'Фигуры':'квадрат треугольник прямоугольник круг эллипс ромб трапеция'
         ' параллелограмм пятиугольник шестиугольник восьмиугольник'.split(),
'Фрукты':'яблоко апельсин лимон лайм груша мандарин виноград грейпфрут'
         ' персик банан абрикос манго банан нектарин'.split(),
'Животные':'аист бабуин баран барсук бык волк зебра кит коза корова кошка'
           ' кролик крыса лев лиса лось медведь мул мышь норка носорог'
           ' обезьяна овца олень осел панда пума скунс собака сова тигр'
           ' тюлень хорек ящерица'.split()}


def getRandomWord(wordDict):
    wordKey = random.choice(list(wordDict.keys()))
    wordIndex = random.randint(0, len(wordDict[wordKey]) - 1)
    return wordDict[wordKey][wordIndex]


def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('Ошибочные буквы:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)):  # заменяет пропуски отгаданными буквами
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i + 1:]

    for letter in blanks:  # показывает секретное слово с пробелами между буквами
        print(letter, end=' ')
    print()


def getGuess(alreadyGuessed):
    # возвращает букву, введенную игроком. Эта функция проверяет, что игрок ввел тольок 1 букву
    while True:
        displayBoard(missedLetters, correctLetters, secretWord)
        print('Введите букву.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Пожалуйста, введите 1 букву.')
        elif guess is alreadyGuessed:
            print('Вы уже называли эту букву. Выберите другую')
        elif guess not in 'абвгдеежзийклмнопрстуфхцчшщъыьэюя':
            print('Пожалуйста, введите БУКВУ(рус алфавит)')
        else:
            return guess


def playAgain():
    print('Хотите сыграть еще? (да или нет)')
    return input().lower().startswith('д')


print('В И С Е Л И Ц А')
difficulty = ''
while difficulty not in 'ЛСТ':
    print('Выберите уровень сложноси: Л - Легкий, С - Средний, Т -Тяжелый')
    difficulty = input().upper()
if difficulty == 'С':
    del HANGMAN_PICS[8]
    del HANGMAN_PICS[7]
if difficulty == 'Т':
    del HANGMAN_PICS[8]
    del HANGMAN_PICS[7]
    del HANGMAN_PICS[5]
    del HANGMAN_PICS[3]
missedLetters = ''
correctLetters = ''
secretSet = getRandomWord(words)
secretWord = getRandomWord(word)
gameIsDone = False

while True:
    print('Секретное слово из набора: ' + secretSet)
    displayBoard(missedLetters, correctLetters, secretWord)

    # Позволяет игроку ввести букву
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        # Проверяет выиграл ли игрок
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
            if foundAllLetters:
                print('ДА! Секретное слово - "' + secretWord + '"! Вы угадали!')
                gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        # Проверяет, превысил ли игрок лимит попыток и проиграл.
        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)

            print('Вы исчерпали все попытки!\nНе угадано букв: ' + str(len(missedLetters)) + ' и угадано букв: ' + str(
                len(correctLetters)) + '. Было загадано слово "' + secretWord + '".')
            gameIsDone = True
            # Запрос, хочет ли игрок играть заново(только если игра завершена)
        if gameIsDone:
            if playAgain():
                missedLetters = ''
                correctLetters = ''
                gameIsDone = False
                secretWord, secretSet = getRandomWord(words)
            else:
                break
