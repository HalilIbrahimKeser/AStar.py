# 1:
from collections import namedtuple, Counter
from heapq import heappop, heappush

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
print('\n', final_list[-5], '\n', final_list[-4], '\n', final_list[-3], '\n', final_list[-2], '\n', final_list[-1],
      '\n')

# 2:
postnummer_list = set([personer.postnummer for personer in final_list])
print(len(postnummer_list), "\n")

# 3:
etternavn_list = Counter([personer.etternavn for personer in final_list])
print(*etternavn_list.most_common(10), "\n")


# 4:
heap_list = list(personer.etternavn for personer in final_list)

def heap_sort(array):
    heap = []
    for element in array:
        heappush(heap, element)

    ordered = []

    # While we have elements left in the heap
    while heap:
        ordered.append(heappop(heap))

    return ordered

sortedList = heap_sort(heap_list)
print(sortedList.__getitem__(0), sortedList.__getitem__(20000), sortedList.__getitem__(40000),
      sortedList.__getitem__(60000), sortedList.__getitem__(80000))
