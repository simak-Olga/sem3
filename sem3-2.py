#Задача 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
def getmultiplication(list):
s = len(list)//2 + 1 
if len(list) % 2 != 0 
else len(lst)//2
   new_list = [list[i]*list[len(list)-i-1] 
    for i in range(s)]
print(new_list)

list = [2, 3, 4, 5, 6]
multiplication_list(list)
list = list(map(int, input("Введите числа через пробел:\n").split()))
multiplication_list(list)