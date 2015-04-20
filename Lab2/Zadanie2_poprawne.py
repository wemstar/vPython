__author__ = 'wemstar'

import random

wygrane=0

bramki=[1, 2, 3]

n=int(input('Ilość iteracji: '))
zmieniamy=(input('Czy zmieniamy: (y/n): ')=="y")

for x in range(n):
        nagroda=random.choice(bramki)
        bramka=random.choice(bramki)

        if zmieniamy:
                nowe=bramki[:]
                nowe.remove(bramka)
                prowadzacy=nowe[:]
                if bramka != nagroda:
                        prowadzacy.remove(nagroda)

                nowe.remove(random.choice(prowadzacy))

                bramka=random.choice(nowe)
        if nagroda==bramka:
                wygrane+=1


print("Wygrane  {0} ".format(wygrane/n))
