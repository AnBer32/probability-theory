Из колоды в 52 карты извлекаются случайным образом 4 карты.

a) Найти вероятность того, что все карты – крести.

В колоде из 52 листов 52/4 = 13 карт одной масти.
Использую формулу подсчета количества сочетаний по k элементов из множества n:
$\displaystyle C^k_n=\frac{n!}{k!(n-k)!}$
и формулу классической вероятности:
$\displaystyle P(A)=\frac{m}{n}$
где m-число благоприятных исходов,n-общее число всех исходов.
$\displaystyle n=C^4_{52}$ т.е. количество способов извлечь 4 карты из 52, а $\displaystyle m=C^4_{13}$, способов извлечь 4 карты одной масти.

Из классической формулы вероятности следует, что вероятность извлечь первой картой из 4-х крестовую: $\displaystyle\frac{13}{52}$;
вторую крестовую: $\displaystyle\frac{12}{51}$;
третью крестовую: $\displaystyle\frac{11}{50}$;
четвертую: $\displaystyle\frac{10}{49}$.
Т.к., по условию и первая, и вторая, и третья, и четвертая должны быть крестовые, то $\displaystyle P(4 крести)=\frac{13}{52}\cdot\frac{12}{51}\cdot\frac{11}{50}\cdot\frac{10}{49}$

б) Найти вероятность, что среди 4-х карт окажется хотя бы один туз.

Общее число исходов $\displaystyle n=C^4_{52}$

а $\displaystyle m$
 будет складываться из 4 вариантов:

1. из 4-х карт 1 туз:
- число способов достать 1 туз из 4-х $C^1_4$, число способов достать три остальные карты $С^3_{48}$, общее количество сочетаний 1 туз и 3 не туза $C^1_{4}\cdotС^3_{48}$
 2. из 4-х карт 2 туза:
число способов достать 2 туза из 4-х $C^2_4$, число способов достать две остальные карты $С^2_{48}$, общее количество сочетаний 2 туза и 2 не туза $C^2_{4}\cdotС^2_{48}$
 3. из 4-х карт 3 туза:
число способов достать 3 туза из 4-х $C^3_4$
, число способов достать оставшуюся карту $С^1_{48}$
, общее количество сочетаний 3 туза и 1 не туз 
$C^3_{4}\cdotС^1_{48}$
 4. из 4-х карт 4 туза:
число способов достать 4 туза из 4-х $C^4_4=1$

Можно использовать то, что сумма вероятностей противоположных событий равна 1, т.е.$\displaystyle P(A)+P(\bar{A})=1$,
тогда $\bar{A}$
-событие, когда из 4-х извлеченных карт не оказалось ни одного туза. Для этого события общее число исходов $\displaystyle n=C^4_{52}$, а $\displaystyle m=C^4_{48}$ т.е. количество способов извлечь 4 карты из колоды без тузов. Тогда $\displaystyle P(A)=1-P(\bar{A})$

ОТВЕТ: 

-а) $P(\text{4 крести})\approx 0.0026 \approx 0.26\%$

-б) $P(\text{хотя бы 1 туз})\approx 0.2813 \approx 28.13\%$