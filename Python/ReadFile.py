# 1: Legg hver rad inn i en passende datastruktur,
# feks. tuple, dict, list eller namedtuple. Skriv så ut de 5 siste radene i en celle.
# Lager tuples med personer fra filen
from collections import namedtuple, Counter

final_list = []
personer_list = namedtuple('personer', ['etternavn', 'fornavn', 'adresse', 'postnummer', 'poststed'])

try:
    with open("personer.dta", "r") as file:
        for lines in file:
            data = lines.strip().split(';')
            personer = personer_list(etternavn=data[0], fornavn=data[1], adresse=data[2],
                                     postnummer=data[3], poststed=data[4])
            final_list.append(personer)
except FileNotFoundError as err:
    print(err)
finally:
    file.close()

# Fem siste på en fin utksrift. Kunne brukt final_list[-5:]
print('\n', *final_list[-5], '\n', *final_list[-4], '\n', *final_list[-3], '\n', *final_list[-2], '\n', *final_list[-1],
      '\n')

# 2: Hvor mange unike postnummer finnes i "Personer.dta"?
# Telle antall forekomster av postnummer
postnummer_list = set([personer.postnummer for personer in final_list])
print(len(postnummer_list), "\n")

# 3: Hva er de 10 vanligste etternavnene (som forekommer flest ganger) i "Personer.dta"?
etternavn_list = Counter([personer.etternavn for personer in final_list])
print(*etternavn_list.most_common(10))


# 4: Implementer sorteringsalgoritmen Heap Sort og sorter listen "persons" utfra rekkefølgen radene er lest inn i.
# Ferdig implementerte funksjoner som sorted skal ikke benyttes.
# Skriv så ut indexene [0,20000,40000,60000,80000] fra den sorterte listen.
def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # left = 2*i + 1
    right = 2 * i + 2  # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if left < n and arr[i] < arr[left]:
        largest = left

        # See if right child of root exists and is
    # greater than root
    if right < n and arr[largest] < arr[right]:
        largest = right

        # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # Heapify the root.
        heapify(arr, n, largest)


def heapSort(arr):
    n = len(arr)

    # Build a maxheap.
    # Since last parent will be at ((n//2)-1) we can start at that location.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

        # One by one extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)

#-------------------------------------Søk etter heapsort geek lexiograpic
personer = [personer.etternavn for personer in personer_list]
heapSort(personer)
n = len(personer)
for i in range(n):
    print(personer[i])