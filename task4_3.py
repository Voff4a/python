Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.


lst = list(map(int, input("Enter space-separated digits:\n").split()))
print(f"Original list: {lst}")
new_lst = []
[new_lst.append(i) for i in lst if i not in new_lst]
print(f"List of unrepeated elements: {new_lst}")