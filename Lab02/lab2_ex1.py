import random


def simuleaza_experiment():
    # Bile inițiale în urnă
    urn = {'rosie': 3, 'albastra': 4, 'neagra': 2}

    # Aruncăm zarul
    zar = random.randint(1, 6)

    # Actualizăm urna în funcție de rezultatul zarului
    if zar in [2, 3, 5]:  # Număr prim
        urn['neagra'] += 1
    elif zar == 6:  # Numărul 6
        urn['rosie'] += 1
    else:  # Numărul 1 sau 4
        urn['albastra'] += 1

    # Creăm lista totală de bile pentru a simula extragerea
    bile = ['rosie'] * urn['rosie'] + ['albastra'] * urn['albastra'] + ['neagra'] * urn['neagra']

    # Extragerea unei bile
    extrasa = random.choice(bile)

    return extrasa


# Simulăm de multe ori pentru a estima probabilitatea
def estimeaza_probabilitatea_rosie(n_experimente):
    numar_rosii = 0

    for _ in range(n_experimente):
        if simuleaza_experiment() == 'rosie':
            numar_rosii += 1

    # Probabilitatea estimată
    return numar_rosii / n_experimente


# Simulăm de 10000 de ori
n_experimente = 10000
probabilitate_rosie = estimeaza_probabilitatea_rosie(n_experimente)
print(f"Probabilitatea estimată de a extrage o bilă roșie: {probabilitate_rosie:.4f}")
