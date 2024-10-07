import random


def simulare_joc():
    N = 0  # Numărul de pași
    S = 0  # Suma totală

    while True:
        N += 1
        moneda = random.choice(['stemă', 'ban'])

        if moneda == 'stemă':
            zar = random.randint(1, 6)  # Aruncăm zarul
            S += zar - 3  # z - 3 $
            break
        else:
            S -= 0.5  # Pierde 0.5 $ dacă pică ban

    return N, S


# Simulare de exemplu
N, S = simulare_joc()
print(f"Numărul de pași: {N}, Suma totală: {S}$")

import matplotlib.pyplot as plt


def simulare_multe_jocuri(numar_jocuri):
    S_values = []

    for _ in range(numar_jocuri):
        _, S = simulare_joc()
        S_values.append(S)

    return S_values

##################################################################################

# Simulăm 10.000 de jocuri
numar_jocuri = 10000
S_values = simulare_multe_jocuri(numar_jocuri)

# Calculăm media lui S
media_S = sum(S_values) / len(S_values)
print(f"Media lui S după {numar_jocuri} jocuri: {media_S}$")

# Afișăm histograma lui S
plt.hist(S_values, bins=30, color='lightblue', edgecolor='black')
plt.title('Distribuția lui S după 10.000 de jocuri')
plt.xlabel('Suma totală ($)')
plt.ylabel('Frecvența')
plt.show()

####################################################################################

def simulare_joc_masluit(p_stema):
    N = 0  # Numărul de pași
    S = 0  # Suma totală

    while True:
        N += 1
        moneda = 'stemă' if random.random() < p_stema else 'ban'

        if moneda == 'stemă':
            zar = random.randint(1, 6)  # Aruncăm zarul
            S += zar - 3  # z - 3 $
            break
        else:
            S -= 0.5  # Pierde 0.5 $ dacă pică ban

    return N, S


def simulare_multe_jocuri_masluite(numar_jocuri, p_stema):
    S_values = []

    for _ in range(numar_jocuri):
        _, S = simulare_joc_masluit(p_stema)
        S_values.append(S)

    return S_values


# Simulăm pentru probabilitatea stemei p = 0.3 și p = 0.7
p_values = [0.3, 0.7]
numar_jocuri = 10000

for p_stema in p_values:
    S_values = simulare_multe_jocuri_masluite(numar_jocuri, p_stema)
    media_S = sum(S_values) / len(S_values)
    print(f"Media lui S pentru p_stema = {p_stema}: {media_S}$")

    # Afișăm histograma lui S
    plt.hist(S_values, bins=30, color='lightblue', edgecolor='black')
    plt.title(f'Distribuția lui S pentru p_stema = {p_stema}')
    plt.xlabel('Suma totală ($)')
    plt.ylabel('Frecvența')
    plt.show()
