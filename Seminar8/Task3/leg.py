#Известно, что рост футболистов в сборной распределен нормально с дисперсией генеральной совокупности, 
#равной 25 кв.см. Объем выборки равен 27, среднее выборочное составляет 174.2. 
#Найдите доверительный интервал для математического ожидания с надежностью 0.95.

import numpy as np
import pandas as pd
from scipy import stats


left=174.2-(1.96*25**0.5)/27**0.5
right=174.2+(1.96*25**0.5)/27**0.5
print(f'95%-й доверительный интервал для оценки мат. ожидания генеральной совокупности: [{left: .4f};{right: .4f}].')