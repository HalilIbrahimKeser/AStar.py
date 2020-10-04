import random
import timeit

start_time = timeit.default_timer()

bubble_sorted_list = []


def random_string(length=5):
    consonants = "abcdefghjklmnpqrstvwxyz"
    vowels = "aeiouæøå"
    return "".join(random.choice((consonants, vowels)[i % 2]) for i in range(length))


string_list = [random_string(5) for i in range(100)]
print("\nUnsorted array is : ")
print(*string_list)


def bubble_sort(string_list):
    n = len(string_list)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if string_list[j] > string_list[j + 1]:
                string_list[j], string_list[j + 1] = string_list[j + 1], string_list[j]


bubble_sort(string_list)

print("Sorted array is:")
for i in range(len(string_list)):
    bubble_sorted_list.append(string_list[i])
print(*bubble_sorted_list)

print("The time difference is :", timeit.default_timer() - start_time)
