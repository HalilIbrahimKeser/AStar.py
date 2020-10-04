import random
import timeit

start_time = timeit.default_timer()


def random_string(length=5):
    consonants = "abcdefghjklmnpqrstvwxyz"
    vowels = "aeiouæøå"
    return "".join(random.choice((consonants, vowels)[i % 2]) for i in range(length))


string_list = [random_string(5) for i in range(1000)]
print("\nUnsorted array is : ")
print(*string_list)


def partition(arr, low, high):
    i = (low - 1)
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] < pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)
        return arr


n = len(string_list)
quick_sorted_list = quick_sort(string_list, 0, n - 1)

print("\nQuick Sorted array is : ")
print(*quick_sorted_list)

print("The time difference is :", timeit.default_timer() - start_time)
