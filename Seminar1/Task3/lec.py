#В ящике имеется 15 деталей, из которых 9 окрашены. Рабочий случайным образом извлекает 3 детали. 
#Какова вероятность того, что все 3 извлеченные детали окрашены?


from math import factorial
def combinations(n, k):
    return int(factorial(n) / (factorial(k) * factorial(n - k))) 

P=combinations(9,3)/combinations(15,3)
print(f'P(3 из 3-х окрашены) = {round(P,4)}')

print(f'P(3 из 3-х окрашены) = {round(9/15*8/14*7/13,4)}')
