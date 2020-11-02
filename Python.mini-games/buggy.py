import random
num1 = random.randint(1, 10)
num2 = random.randint(1, 10)
print('Сколько будет: ' + str(num1) + '+' + str(num2) + '?')
answer = input()
if int(answer) == num1 + num2:
    print('TRUE!')
else:
    print('No! Correct answer - ' + str(num1 + num2))
    
