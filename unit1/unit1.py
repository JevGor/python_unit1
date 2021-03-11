# Task 1
# a = int(input())
# if 1 <= a <= 2 or a == 12:
#     print('Winter')
# elif 3 <= a <= 5:
#     print('spring')
# elif 6 <= a <= 8:
#     print('summer')
# elif 9 <= a <= 11:
#     print('fall')
# else:
#     print('As year have only 12 month, only numbers 1 to 12 are accepted')

# Task 2
# num_1 = input('enter 1st number')
# num_2 = input('enter 2nd number')
# num_1 = int(num_1)
# num_2 = int(num_2)
# if num_1 == num_2:
#     num_1 = num_2 = (num_1 + num_2)
#     print(num_1, num_1)
# elif num_1 != num_2:
#     num_1 = num_2 = 0
#     print(num_1,num_2)
# else:
#     print('dude!')

# Task 3. Значения переменных X, Y, Z поменять местами так, чтобы они оказались упорядоченными по возрастанию.

# num_1 = input('enter 1st number')
# num_2 = input('enter 2nd number')
# num_3 = input('enter 3rd number')
#
# num_1 = int(num_1)
# num_2 = int(num_2)
# num_3 = int(num_3)
#
# a = [num_1,num_2,num_3]
# a.sort()
# a = ' '.join(map(str, a))
# print(a)


# Task 4 Дан номер некоторого года (положительное целое число).
# Вывести число дней в этом году, учитывая, что обычный год насчитывает 365 дней, а високосный — 366 дней.
# Високосным считается год, делящийся на 4, за исключением тех годов, которые делятся на 100 и не делятся на 400
# (например, годы 300, 1300 и 1900 не являются високосными, а 1200 и 2000 — являются).
#
# year = int(input())
#
# if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
#     print("Обычный")
# else:
#     print("Високосный")

#Task 5  Дано целое число, лежащее в диапазоне от –999 до 999. Вывести строку — словесное описание данного числа вида
# "отрицательное двузначное число", "нулевое число", "положительное однозначное число" и т.д.

# n = int(input())
# if -999 <= n < -99:
#     print('отрицательное трех число')
# elif -99 <= n < -9:
#     print('отрицательное двузначное число')
# elif -9 <= n < 0:
#     print('отрицательное однозначное число')
# elif n == 0:
#     print('Нуль')
# elif 1 <= n < 10:
#     print('положительное однозначное число')
# elif 10 <= n < 100:
#     print('положительное двух число')
# elif 100 <= n < 999:
#     print('положительное трех число')
# else:
#     print('Введенное Вами число не диапозона от -999 до 999')

# Task 6 Проверить истинность высказывания: "Сумма цифр данного трехзначного числа является четным числом".
#
# n = int(input('Input three-digit number'))
#
# if len(str(n)) == 3:
#     d1 = n % 10
#     n = n // 10
#     d2 = n % 10
#     n = n // 10
#     if n % 2 == 0:
#         print('The sum is even number')
#     else:
#             print('The sum is odd number')
# else:
#     print('Entered number is not three-digit')

# Task 7 Дано целое число в диапазоне 0 – 9. Вывести строку — название соответствующей цифры на русском языке
# (0 — "ноль", 1 — "один", 2 — "два", ...).
# n = int(input('Input number from 0 to 9'))
# if n == 0:
#     print('Zero')
# elif n == 1:
#     print('One')
# elif n == 2:
#     print('Two')
# elif n == 3:
#     print('Three')
# elif n == 4:
#     print('Four')
# elif n == 5:
#     print('Five')
# elif n == 6:
#     print('Six')
# elif n == 7:
#     print('Seven')
# elif n == 8:
#     print('Eight')
# elif n == 9:
#     print('Nine')
# else:
#     print('Entered number is out of 0 to 9 range')

# Task 8. Из трех данных чисел выбрать наибольшее.
# a = int(input())
# b = int(input())
# c = int(input())
#
# m = a
# if m < b:
#     m = b
# if m < c:
#     m = c
#
# print('m')
