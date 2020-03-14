# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 18:22:48 2020

Modified code. Result: 5 attempts

@author: vysdenis
"""

import numpy as np
       
def score_game(game_core_v3):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core_v3(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)


def game_core_v3(number):
    '''Сначала устанавливаем число 50, а потом уменьшаем или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 0
    predict = 50 #Начинаем с половины диапазона
    step = 0
    while number != predict:
        count+=1
        if count == 1:
            step = 20
        elif count == 2:
            step = 10
        elif count == 3:
            step = 5
        elif count == 4:
            step = 3
        else:
            step = 1
        if number > predict: 
            predict += step
        elif number < predict: 
            predict -= step
    return(count) # выход из цикла, если угадали

# Проверяем
score_game(game_core_v3)
