#Монету подбросили 144 раза. Какова вероятность, что орел выпадет ровно 70 раз?


from math import factorial, exp
def bernulli(n, k, p):
    comb=factorial(n)/(factorial(k)*factorial(n-k))
    return comb*(p**k)*(1-p)**(n-k)

print(f'P = {bernulli(144,70,0.5): .4f}')