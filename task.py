import timeit
import random

def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >=0 and key < lst[j] :
                lst[j+1] = lst[j]
                j -= 1
        lst[j+1] = key 
    return lst

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    # Спочатку об'єднайте менші елементи
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Якщо в лівій або правій половині залишилися елементи, 
		# додайте їх до результату
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

# Повністю несортований список чисел
array1 = [random.randint(1, 100000) for _ in range(50000)]

# Наполовину сортований, наполовину не сортований список чисел
array2 = sorted(random.sample(range(1, 100001), 25000))
array2 += random.sample(range(1, 100001), 25000)

# 1/4 посортований список, 2/4 непосортовані, 1/4 посортований список чисел
array3 = []
pattern = [True, False, False, True]

for is_sorted in pattern:  
    block = random.sample(range(1, 100001), 12500)
    if is_sorted:
        block.sort()
    array3 += block

print("Результати сортування повністю несортованого списку чисел")
print("Сортування вставками:")
timeit_result = timeit.timeit("insertion_sort(array1)", number=10, globals=locals())
print(f"Час виконання: {timeit_result:.5f} секунд")

print("Сортування злиттям:")
timeit_result = timeit.timeit("merge_sort(array1)", number=10, globals=locals())
print(f"Час виконання: {timeit_result:.5f} секунд")

print("Timsort:")
timeit_result = timeit.timeit("array1.sort()", number=10, globals=locals())
print(f"Час виконання: {timeit_result:.5f} секунд")

print("Результати сортування наполовину сортований, наполовину не сортований список чисел")
print("Сортування вставками:")
timeit_result = timeit.timeit("insertion_sort(array2)", number=10, globals=locals())
print(f"Час виконання: {timeit_result:.5f} секунд")

print("Сортування злиттям:")
timeit_result = timeit.timeit("merge_sort(array2)", number=10, globals=locals())
print(f"Час виконання: {timeit_result:.5f} секунд")

print("Timsort:")
timeit_result = timeit.timeit("array2.sort()", number=10, globals=locals())
print(f"Час виконання: {timeit_result:.5f} секунд")

print("Результати сортування 1/4 посортований список, 2/4 непосортовані, 1/4 посортований список чисел")
print("Сортування вставками:")
timeit_result = timeit.timeit("insertion_sort(array3)", number=10, globals=locals())
print(f"Час виконання: {timeit_result:.5f} секунд")

print("Сортування злиттям:")
timeit_result = timeit.timeit("merge_sort(array3)", number=10, globals=locals())
print(f"Час виконання: {timeit_result:.5f} секунд")

print("Timsort:")
timeit_result = timeit.timeit("array3.sort()", number=10, globals=locals())
print(f"Час виконання: {timeit_result:.5f} секунд")



""" 
1000 sample
Результати сортування повністю несортованого списку чисел
Сортування вставками:
Час виконання: 0.03465 секунд
Сортування злиттям:
Час виконання: 0.02145 секунд
Timsort:
Час виконання: 0.00006 секунд
Результати сортування наполовину сортований, наполовину не сортований список чисел
Сортування вставками:
Час виконання: 0.02752 секунд
Сортування злиттям:
Час виконання: 0.02228 секунд
Timsort:
Час виконання: 0.00007 секунд
Результати сортування 1/4 посортований список, 2/4 непосортовані, 1/4 посортований список чисел
Сортування вставками:
Час виконання: 0.03482 секунд
Сортування злиттям:
Час виконання: 0.02460 секунд
Timsort:
Час виконання: 0.00006 секунд

10k sample

Результати сортування повністю несортованого списку чисел
Сортування вставками:
Час виконання: 3.53671 секунд
Сортування злиттям:
Час виконання: 0.26911 секунд
Timsort:
Час виконання: 0.00067 секунд
Результати сортування наполовину сортований, наполовину не сортований список чисел
Сортування вставками:
Час виконання: 2.62005 секунд
Сортування злиттям:
Час виконання: 0.26983 секунд
Timsort:
Час виконання: 0.00080 секунд
Результати сортування 1/4 посортований список, 2/4 непосортовані, 1/4 посортований список чисел
Сортування вставками:
Час виконання: 3.11773 секунд
Сортування злиттям:
Час виконання: 0.27359 секунд
Timsort:
Час виконання: 0.00093 секунд

50k sample:
Результати сортування повністю несортованого списку чисел
Сортування вставками:
Час виконання: 99.36754 секунд
Сортування злиттям:
Час виконання: 1.61673 секунд
Timsort:
Час виконання: 0.00440 секунд
Результати сортування наполовину сортований, наполовину не сортований список чисел
Сортування вставками:
Час виконання: 68.60610 секунд
Сортування злиттям:
Час виконання: 1.54678 секунд
Timsort:
Час виконання: 0.00345 секунд
Результати сортування 1/4 посортований список, 2/4 непосортовані, 1/4 посортований список чисел
Сортування вставками:
Час виконання: 93.14649 секунд
Сортування злиттям:
Час виконання: 1.72326 секунд
Timsort:
Час виконання: 0.00521 секунд
"""