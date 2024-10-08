import csv
import random


def select_random_elements_from_csv(file_path, num_elements):
    # Citim conținutul fișierului CSV
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        data_list = [row[0] for row in reader]  # Presupunem că fiecare rând are un singur element

    # Verificăm dacă numărul de elemente cerut este mai mic sau egal cu dimensiunea listei
    if num_elements > len(data_list):
        raise ValueError("Numărul de elemente cerut este mai mare decât dimensiunea listei din fișier.")

    # Selectăm un număr de elemente fără repetiție
    selected_elements = random.sample(data_list, num_elements)

    # Returnăm elementele selectate
    return selected_elements


# Exemplu de utilizare
file_path = 'lista.csv'  
num_elements = 2  # Numărul de elemente pe care vrem să le selectăm

selected_elements = select_random_elements_from_csv(file_path, num_elements)
print("Elementele selectate sunt:", selected_elements)
