print("Радий вітати вас в угадайці")
import random
def maximum():
    while True:
        s = input("Вкажіть максимальне значення: ")
        if int(s.isdigit()) and int(s) > 0:
            return int(s)
        else:
            print("Вкажіть число більше за нуль")
            continue
q = maximum()
num1 = random.randint(0,q)
print("Я обрав число спробуєш вігадати?")
n = input("Вкажіть свій варіант: ")
def game(n):
    flag = False
    total = 0
    while flag != True:
        if n.isdigit():
            if int(n) == num1:
                total += 1
                flag = True
            elif int(n) > num1:
                print("Забагато, спробуй ще")
                total += 1
                n = input("Вкажіть свій варіант: ")
            elif int(n) < num1:
                print("Замало спробуй ще")
                total += 1
                n = input("Вкажіть свій варіант: ")
        else:
            print("Тільки число")
            n = input("Вкажіть свій варіант: ")
    return f"Кількість спроб: {total}" '''
Ви перемогли
    '''
print(game(n))