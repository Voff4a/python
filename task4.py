Задание 4.

Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма
(прибыль — выручка больше издержек, или убыток — издержки больше выручки).
Выведите соответствующее сообщение. Если фирма отработала с прибылью,
вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите
прибыль фирмы в расчете на одного сотрудника.

Пример:
Введите выручку фирмы: 1000
Введите издержки фирмы: 500
Финансовый результат - прибыль. Ее величина: 500
Значит вычисляем рентабельность выручки (соотношение прибыли к выручке)
Рентабельность выручки = 0.5
Введите численность сотрудников фирмы: 10
Прибыль фирмы в расчете на одного сотрудника = 50.0

plus = int(input('Enter profit value'))
minus = int(input('Enter cost value'))
people = int(input('Enter the number of employees'))
if plus > minus:
    print('Revenue is greater than costs')
    clear_plus = plus - minus
    rent = clear_plus/plus
    print('profit {} of revenue {}: {:.2f'  .format(is, rent))
    clear_for_person = float(clear_plus/people)
    print('The company's profit per employee: %s'%clear_for_person)
else:
    print('The company is operating at a loss')