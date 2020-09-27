# 1:
from collections import namedtuple, Counter
from heapq import heappop, heappush

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

# Fem siste på en fin utksrift. Kunne brukt final_list[-5:]
print(final_list[-5], '\n', final_list[-4], '\n', final_list[-3], '\n',
      final_list[-2], '\n', final_list[-1], '\n')

# 2:
postnummer_list = set([personer.postnummer for personer in final_list])
print(len(postnummer_list), "\n")

# 3:
etternavn_list = Counter([personer.etternavn for personer in final_list])
print(*etternavn_list.most_common(10), "\n")

# 4:
# -----------------------------------------------------------------------
# Funskjon 1, den sorterer ikke fult ut av en eller annen grunn
x = -1
heap = [0] * 100000
heap_list = list(personer.etternavn for personer in final_list)
sorted_list = list()


def heapForm(k):
    global x
    x += 1
    heap[x] = k
    child = x
    index = x // 2
    while index >= 0:
        if heap[index] > heap[child]:
            tmp = heap[index]
            heap[index] = heap[child]
            heap[child] = tmp
            child = index
            index = index // 2
        else:
            break


def heapSort():
    global x
    while x >= 0:
        k = heap[0]
        heap[0] = heap[x]
        x = x - 1
        tmp = -1
        index = 0
        length = x
        left1 = 1
        right1 = left1 + 1
        sorted_list.append(k)

        while left1 <= length:
            if (heap[index] <= heap[left1] and
                    heap[index] <= heap[right1]):
                break
            else:
                if heap[left1] < heap[right1]:
                    tmp = heap[index]
                    heap[index] = heap[left1]
                    heap[left1] = tmp
                    index = left1
                else:
                    tmp = heap[index]
                    heap[index] = heap[right1]
                    heap[right1] = tmp
                    index = right1
            left1 = 2 * left1
            right1 = left1 + 1


def sort(k):
    for i in range(len(heap_list)):
        heapForm(k[i])
    heapSort()


if __name__ == '__main__':
    sort(heap_list)
print("Funksjon 1:")
print(sorted_list[0], sorted_list[20000], sorted_list[40000], sorted_list[60000], sorted_list[80000])


# ----------------------------------------------------

# Funskjon 2, den sorterer riktig
def heap_sort(array):
    heap1 = []
    for element in array:
        heappush(heap1, element)

    ordered = []

    while heap1:
        ordered.append(heappop(heap1))

    return ordered


sorted_list2 = heap_sort(heap_list)
print("Funksjon 2:")
print(sorted_list2[0], sorted_list2[20000], sorted_list2[40000], sorted_list2[60000], sorted_list2[80000])
# ----------------------------------------------------
