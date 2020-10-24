import random
import timeit

start_time = timeit.default_timer()

selection_sorted_list = []


def random_string(length=5):
    consonants = "abcdefghjklmnpqrstvwxyz"
    vowels = "aeiouæøå"
    return "".join(random.choice((consonants, vowels)[i % 2]) for i in range(length))


string_list = [random_string(4) for i in range(10000)]
print("\nUnsorted array is : ")
print(*string_list)


def selection_sort(string_list, size):
    A = string_list
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):
            if string_list[i] < string_list[min_idx]:
                min_idx = i
        (string_list[step], string_list[min_idx]) = (string_list[min_idx], string_list[step])


selection_sort(string_list, len(string_list))

for i in range(len(string_list)):
    selection_sorted_list.append(string_list[i])

print("Sorted array is:")
print(*selection_sorted_list)

print("The time difference is :", timeit.default_timer() - start_time)

