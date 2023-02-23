Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


num = int(input("Enter the digit: "))
i = 2  # first simple digit
lst = []
old = num
while i <= num:
    if num % i == 0:
        lst.append(i)
        num //= i
        i = 2
    else:
        i += 1
print(f"Simple multipliers of the digit {old} listed: {lst}")