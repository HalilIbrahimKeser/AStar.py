# alternative 2 from
# https://www.geeksforgeeks.org/merge-sort/
import random
import timeit
import sorting

from pandas.core import sorting

start_time = timeit.default_timer()


def random_string(length=5):
    consonants = "abcdefghjklmnpqrstvwxyz"
    vowels = "aeiouæøå"
    return "".join(random.choice((consonants, vowels)[i % 2]) for i in range(length))


string_list2 = [random_string(5) for i in range(1000)]
print("\nUnsorted array is : ")
print(*string_list2)


def merge_sort(values):
    if len(values) > 1:
        m = len(values) // 2
        left = values[:m]
        right = values[m:]
        left = merge_sort(left)
        right = merge_sort(right)
        values = []
        while len(left) > 0 and len(right) > 0:
            if left[0] < right[0]:
                values.append(left[0])
                left.pop(0)
            else:
                values.append(right[0])
                right.pop(0)
        for i in left:
            values.append(i)
        for i in right:
            values.append(i)
    return values


merge_sorted_list = merge_sort(string_list2)

print("\nMerge sorted array is alternative 2: ")
print(*merge_sorted_list)

print("The time difference is :", timeit.default_timer() - start_time)

start_time_2 = timeit.default_timer()


# alternative 1

def merge_sort_2(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort_2(L)
        merge_sort_2(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr


merge_sorted_list1 = merge_sort_2(string_list2)

print("\nMerge sorted array is alternative 1: ")
print(*merge_sorted_list1)

print("The time difference is :", timeit.default_timer() - start_time_2)


#Innebygd sorting mekanisme, installert via PIP

#sorted_list_innebygd = sorting.mergesort(string_list2)