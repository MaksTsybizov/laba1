from random import randint
lst = [randint(1,10) for i in range(10)]
print(lst)
AAA = [i for i in set(lst) if lst.count(i) > 1]
if len(AAA) == 0:
   print("Повторяющихся элементов нет")
else:
   print(AAA)
