#Вероятность того, что стрелок попадет в мишень, выстрелив один раз, равна 0.8. 
#Стрелок выстрелил 100 раз. Найдите вероятность того, что стрелок попадет в цель ровно 85 раз.

from math import factorial, exp
def bernulli(n, k, p):
    comb=factorial(n)/(factorial(k)*factorial(n-k))
    return comb*(p**k)*(1-p)**(n-k)
print(f'P = {bernulli(100,85,0.8): .4f}')