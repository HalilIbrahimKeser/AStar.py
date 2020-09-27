x = -1
heap = [0] * 100000

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
        sorted_list.append(k)
        heap[0] = heap[x]
        x = x - 1
        tmp = -1
        index = 0
        length = x
        left1 = 1
        right1 = left1 + 1

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
    for i in range(100000):
        heapForm(k[i])
    heapSort()


if __name__ == '__main__':
    heap_list = list()
    try:
        with open("personer.dta", "r") as file:
            for lines in file:
                data = lines.strip().split('\n')
                heap_list.append(data)
    except FileNotFoundError as err:
        print(err)
    finally:
        file.close()

    heap_list_etternavn = list(personer for personer in heap_list)

    sort(heap_list_etternavn)

    print(sorted_list.__getitem__(0), sorted_list.__getitem__(20000), sorted_list.__getitem__(40000),
          sorted_list.__getitem__(60000), sorted_list.__getitem__(80000))