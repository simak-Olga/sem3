#1.Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
def getsum (list):
    result = 0
    for i in range(1, len(list), 2):
        result += list[i]
    return result