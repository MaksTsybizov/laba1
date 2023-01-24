# Задание 1

arr = []

for _ in range(10):

   arr.append(int(input('Введите число: ')))

for i in range(9):

   if arr[i] < 0 and arr[i + 1] < 0:

       print('Пара:', arr[i], arr[i + 1])

print()

# Задание 2

arr = []

arr_2 = []

for _ in range(10):

   arr.append(int(input('Введите число: ')))

for el in arr:

   if el not in arr_2:

       arr_2.append(el)

print(arr_2)