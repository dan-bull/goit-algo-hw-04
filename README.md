# Результати дослідження
| Розмір списку | Алгоритм             | Несортований список | Напівсортований список | 1/4 сортований список |
| ------------- | -------------------- | ------------------- | ---------------------- | --------------------- |
| 1000          | Сортування вставками | 0.03465 с           | 0.02752 с              | 0.03482 с             |
|               | Сортування злиттям   | 0.02145 с           | 0.02228 с              | 0.02460 с             |
|               | Timsort              | 0.00006 с           | 0.00007 с              | 0.00006 с             |
| 10,000        | Сортування вставками | 3.53671 с           | 2.62005 с              | 3.11773 с             |
|               | Сортування злиттям   | 0.26911 с           | 0.26983 с              | 0.27359 с             |
|               | Timsort              | 0.00067 с           | 0.00080 с              | 0.00093 с             |
| 50,000        | Сортування вставками | 99.36754 с          | 68.60610 с             | 93.14649 с            |
|               | Сортування злиттям   | 1.61673 с           | 1.54678 с              | 1.72326 с             |
|               | Timsort              | 0.00440 с           | 0.00345 с              | 0.00521 с             |

## Висновки:

Timsort виявився найшвидшим алгоритмом сортування у всіх трьох випадках. Сортування злиттям трохи повільніше за Timsort, але все ж значно швидше, ніж сортування вставками. Сортування вставками, хоч і найповільніше, може бути корисним для невеликих списків.

### Деякі додаткові спостереження:

- Час виконання сортування вставками та сортування злиттям зростає приблизно квадратично з розміром списку, що робить їх менш ефективними для великих обсягів даних. У той час як час виконання Timsort зростає майже лінійно з розміром списку, що свідчить про його високу швидкість та ефективність, особливо для великих масивів даних.
- Напівсортовані списки сортуються швидше, ніж несортовані списки, за допомогою всіх трьох алгоритмів сортування. Списки, які 1/4 сортовані, 2/4 несортовані, 1/4 сортовані, сортуються трохи швидше, ніж несортовані списки, за допомогою алгоритмів сортування вставками та сортування злиттям. Timsort сортує ці списки майже так само швидко, як і напівсортовані списки, що свідчить про його стійкість та надійність у різних сценаріях сортування.
