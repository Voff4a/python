Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369

n = input('enter the number n')
temp = str(n)
n1 = temp + temp
n2 = temp + temp + temp
comp = n + int(n1) + int(n2)
print("result:", comp)
