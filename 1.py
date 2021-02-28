#1
lst = [92, 91, 49, 87, 74, 20, 94, 12, 64, 36, 97, 2, 96, 40, 97, 36, 32, 22, 80, 83, 49, 52, 62, 31,
55, 86, 84, 1, 22, 15, 52, 18, 78, 92, 21, 9, 85, 89, 54, 99, 80, 7, 4, 31, 30, 28, 59, 35, 72, 33]

dict(enumerate(lst))
print({index+1:value for index,value in enumerate(lst)})

#2
import random
number = random.randint(1,20)
print('Что ж, ' + ', я загадываю число от 1 до 20.')

for guessesTaken in range(5):
    print('Попробуй угадать.') 
    guess = input()
    guess = int(guess)

    if guess<number:
        print("слишком мало")

    if guess>number:
        print("слишком много")

    if guess==number:
        break
if guess == number:
    guessesTaken=str(guessesTaken+1)
    print("Класс! Вы угадали!")

else:
    print("Все, вы не выиграли. Игра завершилась")

#3
some_string = "enviroment"
print(some_string[4:7])

#4
a = "Aidana"
b = "Adilet"

c = ''.join(map(''.join, zip(a, b)))
print(c)