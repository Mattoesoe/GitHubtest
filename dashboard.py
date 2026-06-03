print('Hello, World!')

print (4+4)

print('Hallo nog een keer')

import random

geheim_getal = random.randint(1, 100)
pogingen = 0

print("Ik heb een getal tussen 1 en 100 gekozen!")

while True:
    gok = int(input("Jouw gok: "))
    pogingen += 1

    if gok < geheim_getal:
        print("Te laag!")
    elif gok > geheim_getal:
        print("Te hoog!")
    else:
        print(f"Goed geraden! Het getal was {geheim_getal}.")
        print(f"Je had {pogingen} pogingen nodig.")
        break