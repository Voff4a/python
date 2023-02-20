Задание 2.

Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.

Пример:
Введите время в секундах: 3600
Время в формате ч:м:с - 1.0 : 60.0 : 3600

time_sec = int(input'3600')
hours = time_sec//3600
hours_res = (hours) if hours > 10 else ('0' + str(hours))
minutes = (time_sec % 3600)//60
minutes_res = (minutes) if minutes > 10 else ('0' + str(minutes))
seconds = (time_sec % 3600) % 60
seconds_res = (seconds) if seconds > 10 else ('0' + str(seconds))
if hours > 24:
    print('Number of hours exceeding the number of hours per day, correct the input')
else:
    print('Moscow time: {hours_res} : {minutes_res} : {seconds_res}')