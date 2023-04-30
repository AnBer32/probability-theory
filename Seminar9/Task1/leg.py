#Даны значения величины заработной платы заемщиков банка (zp) и значения их поведенческого 
#кредитного скоринга (ks): zp = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110], 
#ks = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832]. 
#Используя математические операции, посчитать коэффициенты линейной регрессии, 
#приняв за X заработную плату (то есть, zp - признак), 
#а за y - значения скорингового балла (то есть, ks - целевая переменная).
#Произвести расчет как с использованием intercept, так и без.

import numpy as np
import matplotlib.pyplot as plt

zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])

plt.scatter(zp, ks)
plt.xlabel('Заработая плата заемщиков')
plt.ylabel('Поведенческий кредитный скоринг', rotation = 90)
plt.show()

b = (np.mean(zp * ks) - np.mean(zp) * np.mean(ks)) / (np.mean(zp ** 2) - np.mean(zp) ** 2)
b

a = np.mean(ks) - b * np.mean(zp)
a

plt.scatter(zp, ks)
plt.plot(zp, a + b * zp, c = 'r')
plt.xlabel('Заработая плата заемщиков')
plt.ylabel('Поведенческий кредитный скоринг', rotation = 90)
plt.show()
