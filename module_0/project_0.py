# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 18:22:48 2020

Modified code. Binary search. Result: 5 attempts

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
    #Решаем задачу с помощью бинарного поиска
    count = 0
    predict = 0 
    low = 0
    high = 100
    while low <= high:
        count+=1
        predict = (low + high) // 2
        if number < predict:
            high = predict - 1
        elif number > predict:
            low = predict + 1
        else:
            break
    return(count) # выход из цикла, если угадали

# Проверяем
score_game(game_core_v3)
