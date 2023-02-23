Реализовать структуру «Рейтинг», представляющую собой не
возрастающий набор натуральных чисел
(каждый элемент ряда меньше или равен предыдущему).

У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.

Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.

Набор натуральных чисел можно задать непосредственно в коде,
например, my_list = [7, 5, 3, 3, 2]..
rating = [10, 10, 5, 4, 1]

print(f"Current rating: {rating}")

new_scores_count = int(input("How many new rating elements do you want to enter: "))

for i in range(1, new_scores_count + 1):
    new_score = int(input("Enter a new rating element: "))
    if new_score > 0:
        rating.append(new_score)
        rating.sort(reverse = True)
        print(f"New rating: {rating}")
    else:
        print("Error. You entered not a natural number")