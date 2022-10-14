# 1_Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#Пример:
#- 6782 -> 23
#- 0,56 -> 11
# 
# 2_Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#Пример:
#- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
# 
# 3_Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
#Пример:
#- Для n = 3: {1: 2.0, 2: 2.25, 3: 2.37 }
# 
# 4_Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.
#
# Реализуйте алгоритм перемешивания списка.


print ('Введите номер задания (1-5): ')
n = int (input ())

if n==1: # № 1
    print ('Введите вещественное число: ')
    ch = (input())
    
    ch_sum = 0
    for i in ch:
    
        if (i != ".") and (i != ","):
            ch_sum = ch_sum + int (i)

    print (f"Сумма чисел вещественного числа: {ch_sum}")

elif n==2: # № 2
    print ('Введите целое число N: ')
    N = int (input())
    print ('----------------')

    def fact (ch):
        fact_ch=1

        for i in range (1, ch + 1):
            fact_ch = fact_ch * i
        return fact_ch

    for i in range (1, N + 1):
        print (f'{fact (i)} ')
    
elif n==3: # №3
    print ('Введите целое число n: ')
    n = int(input()) 

    def fun(n):
        ret_fun = [round((1 + 1 / i)**i, 2) for i in range (1, n + 1)]
        return ret_fun   

    ch = fun(n)
    print(ch)

    ch_sum = round ( sum(fun(n)) )
    print(ch_sum)

elif n==4: # №4
    
    import random
    from random import Random, randint
    
    print ('Введите целое число N: ')
    N4 = int(input())

    num = []
    for i in range (N4):

        num.append (randint ( -1*N4 , N4+1 ))
        
    print(num)
  
    f_txt = open ( 'file.txt', 'w' )

    while True:
        pos = input ('Позиция для вычисления (0-певый элемент, q-выход): ')
        if pos == "q" or int (pos) > N4:
            break
        f_txt.write(pos + "\n")

    f_txt.close()

    ch = 1
    f_txt = open ( 'file.txt', 'r' )

    for j in f_txt:
        if j == "q":
            break
        ch = ch* num [ int(j) ]
    
    f_txt.close()

    print (f"Произведение заданных элементов: {ch}")

    random.shuffle (num)
    print (f"Итог перемешивания списка: {num}")

else:
    print ('Номер задания должен быть от 1 до 5 !!!')


