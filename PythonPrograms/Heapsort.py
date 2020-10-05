# 1:
from collections import namedtuple, Counter

final_list = []
personer_list = namedtuple('personer', ['etternavn', 'fornavn', 'adresse', 'postnummer', 'poststed'])

try:
    with open("personer.dta", "r", encoding='latin1') as file:
        for lines in file:
            data = lines.strip("\n").split(';')
            personer = personer_list(etternavn=data[0], fornavn=data[1], adresse=data[2],
                                     postnummer=data[3], poststed=data[4])
            final_list.append(personer)
except FileNotFoundError as err:
    print(err)
finally:
    file.close()

print(final_list[-5:])

# 2:
postnummer_list = set([personer.postnummer for personer in final_list])
print( "\n", len(postnummer_list), "\n")

# 3:
etternavn_list = Counter([personer.etternavn for personer in final_list])
print(*etternavn_list.most_common(10), "\n")

# 4:
heap_list = list(personer for personer in final_list)


def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        heapify(arr, n, largest)


def heapSort(arr):
    n = len(arr)

    for i in range(n, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


if __name__ == '__main__':
    heapSort(heap_list)

print(heap_list[0])
print(heap_list[20000])
print(heap_list[40000])
print(heap_list[60000])
print(heap_list[80000])
