"""Игра, в которой компьютер угадывает числа, загаданные Вами или генератором"""

from random import randint

####################################


"""Функция is_true_int проверяет чтобы вводимые данные были числа >= 0
    возвращает исправленное значение"""


def is_true_int(num):
    while True:
        while True:
            try:
                num = int(num)
                break
            except ValueError:
                num = input('введите корректные данные (положительное число)\n')
        if num >= 0:
            break
        else:
            num = input('введите число больше либо равное нулю\n')
    return num


####################################

####################################


"""Функция generator_of_num проверяет кто будет загадывать число и 
    чтобы вводимые данные были числа в нужном диапазоне"""


def generator_of_num(men_comp, num_min, num_max):
    """Часть функции , которая узнаёт, кто будет загадывать число"""
    if num_min > num_max:  # проверка на <>
        num_min, num_max = num_max, num_min

    while True:
        while True:
            try:
                men_comp = int(men_comp)
                break
            except ValueError:
                men_comp = input('введите ЧИСЛО 1 или 2\n')
        if men_comp == 1 or men_comp == 2:
            break
        else:
            men_comp = input('введите число 1 или 2\n')
    ################################################################
    """Та часть функции, которое загадывает число"""
    if men_comp == 2:  # загадывает генератор
        men_comp = randint(num_min, num_max)

        ######
    elif men_comp == 1:  # загадывает пользователь
        men_comp = input(f'загадайте число от {num_min} до {num_max}\n')
        while True:
            while True:
                try:
                    men_comp = int(men_comp)
                    break
                except ValueError:
                    men_comp = input(f'загадайте ЧИСЛО от {num_min} до {num_max}\n')
            if num_min <= men_comp <= num_max:
                break
            else:
                men_comp = input(f'загадайте число от {num_min} до {num_max}\n')
    return men_comp


####################################


####################################


"""Функция is_true_more_less проверяет чтобы вводимые данные были <>
    и справедливость на x <> Xnum, 
    где Xnum - загаданное пользователем число, x - загаданное компьютером число"""


def is_true_more_less(m_l, numX, x):
    while True:
        if m_l == ">" or m_l == "<":
            if x > numX and m_l == ">":
                break
            elif x < numX and m_l == "<":
                break
            else:
                print("Вы уверены что правильно выбрали знак? )))")
                m_l = input('введите верное сравнение (< или >)\n')
        else:
            m_l = input('введите корректные данные (< или >)\n')
    return m_l


####################################

####################################


"""Функция, в которой комьютер угадывает число"""


def guesser(num_min, num_max, numX):
    trying = []  # числа, которые называл компьютер
    count = 0  # количество попыток
    while True:
        """Основной алгоритм, по которому компьютер угадывает.
        Самый быстрый метод: -50% """
        if num_min > num_max:  # проверка на <>
            num_min, num_max = num_max, num_min

        count += 1
        x = (num_min + num_max) // 2
        trying.append(x)
        if x != numX:
            print(f'Computer: {name}, {x} меньше или больше Вашего числа? (Введите < или >)')
            more_or_less = input()
            more_or_less = is_true_more_less(more_or_less, numX, x)  # Проверка на корректность ввода данных <>

            if more_or_less == "<":
                num_min = x
            elif more_or_less == ">":
                num_max = x

        elif x == numX and count == 1:
            print(f'Computer: Уррааа, {name}, я угадал с первого раза, Ваше число {x}')
            break
        elif x == numX:
            print(f'Computer: Уррааа, {name}, я угадал с {count} попытки {trying}, Ваше число {x}')
            break


####################################
"""Функция score_game() высчитывает среднее значение попыток угадать за 1000 циклов"""
def score_game(): # не работает
    sum_try = 0     # сумма попыток
    for i in range(1000):
        num_min = 1
        num_max = 100
        men_comp = randint(1, 100)
        while True:   # цикл угадывания
            sum_try += 1
            x = (num_min + num_max) // 2

            if men_comp > x:
                num_min = x
                continue
            elif men_comp < x:
                num_max = x
                continue
            elif men_comp == x:
                break
    return sum_try//1000


average = 7 # среднее значение попыток

name = input('Computer: Привет! Как Вас зовут?\n')
print(f'Computer: {name}, числа от 1 до 100 я, в среднем,  угадываю за {average} попыток,'
                   f' хотите проверить - давайте сыграем!!!\n')


num_min = (input(f'Computer: {name}, введите с какого числа будем угадывать?\n'))
num_min = is_true_int(num_min)  # Проверка на корректность ввода данных
num_max = (input(f'Computer: {name}, введите до какого числа будем угадывать?\n'))
num_max = is_true_int(num_max)  # Проверка на корректность ввода данных

numX = input('Если вы хотите загадать число сами - нажмите 1, если генератор - нажмите 2\n')

numX = generator_of_num(numX, num_min, num_max)

print()

print(f'{name}: (Я загадал {numX}), угадывай Computer\n')
print("НАЧИНАЕМ!!!\n")

"""Запускаем алгоритм "угадывания" """

guesser(num_min, num_max, numX)
