'''Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

Пример:

- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)'''

num = int(input('Введите число: '))
f_n = 1
for i in range(num):
    i = i + 1 
    f_n = f_n * i
print (f'Произведением чисел от 1 до {num} будет {f_n}')
