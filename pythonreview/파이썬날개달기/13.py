import random

rotto = []
while True:
    if len(rotto) == 6:
         break

    tmp = random.randint(1, 45)
    if tmp not in rotto:
        rotto.append(tmp)


print(rotto)
