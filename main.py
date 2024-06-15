import sys
import random
import time

from controls.tda.list.linked_list import Linked_List

sys.path.append("../")


lista = Linked_List()
for i in range(25000):
    lista.add(random.randint(0, 1000))


print("Quick sort:")
start = time.time()
lista.sort_numbers(algorithm="quick_sort")
end = time.time()
print(f"Tiempo de ejecución: {round(end - start, 4)} \n")

print("Shell sort:")
start = time.time()
lista.sort_numbers(algorithm="shell_sort")
end = time.time()
print(f"Tiempo de ejecución: {round(end - start, 4)} \n")

print("Merge Sort:")
start = time.time()
lista.sort_numbers(algorithm="merge_sort")
end = time.time()
print(f"Tiempo de ejecución: {round(end - start, 4)} \n")
