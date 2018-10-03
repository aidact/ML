import numpy as nump
import re
import scipy.linalg
from numpy import sin, exp

func=lambda x: sin(x/5)*exp(x/10)+5*exp(-x/2)


p1=1
p2=2
p3=3
a1=[
    [1 ** n for n in range(0, p1+1)],
    [15 ** n for n in range(0, p1+1)]]

b1=[func(1), func(15)] #функция в точках 1 и 15

scipy.linalg.solve(a1, b1) #решает линейное неравенство


a2=[
    [1 ** n for n in range(0, p2+1)],
    [8 ** n for n in range(0, p2+1)],
    [15 ** n for n in range(0, p2+1)]]

b2=[func(1), func(8), func(15)] #функция в точках 1, 8 и 15

scipy.linalg.solve(a2, b2)


a3=[
    [1 ** n for n in range(0, p3+1)], #w_0
    [4 ** n for n in range(0, p3+1)], #w_1
    [10 ** n for n in range(0, p3+1)], #w_2
    [15 ** n for n in range(0, p3+1)]] #w_3

b3=[func(1), func(4), func(10), func(15)] #функция в точках 1, 4, 10 и 15

ans=scipy.linalg.solve(a3, b3)

map(lambda x: x, ans)