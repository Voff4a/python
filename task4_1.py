Вычислить число c заданной точностью d

Пример:

- при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

import math

d = input('Enter the power of rounding in the format 0.01 from 10 to the -1 power to 10 to the -10 power -> ')
d = d[2:len(d)]
print(round(math.pi,len(d)))