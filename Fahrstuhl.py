'''
    Programm Fahrstuhl
'''
from time import sleep

# Variabeln
auswahl = 0
etage = 0

print('+------------------------------+')
print('|       Fahrstuhl Menü         |')
print('| ____________________________ |')
print('|                              |')
print('|       Auswahl Menü:          |')
print('|                              |')
print('|       Etage 6                |')
print('|       Etage 5                |')
print('|       Etage 4                |')
print('|       Etage 3                |')
print('|       Etage 2                |')
print('|       Etage 1                |')
print('|       EG                     |')
print('|       Etage -1               |')
print('|       Etage -2               |')
print('|                              |')
print('|       -------------------    |')
print('|       Wähle deine Etage      |')
print('+------------------------------|')
print()

eg = 0
auswahl = int(input('Etage: '))
while eg < auswahl:
    print('Aktuelle Etage: ', eg)
    sleep(0.1)
    eg = eg +1
    if eg == auswahl:
        print('Zieletage erreicht', eg)

while eg > auswahl:
    print('Es geht abwärts')
    break
