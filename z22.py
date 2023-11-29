n = int(input("Введите кол-во элементов первого множества: "))
m = int(input("Введите кол-во элементов второго множества: "))
тут я внес правки
set1 = set()
set2 = set()
и тут
print("Введите элементы первого множества: ")
for _ in range(n):
    set1.add(int(input()))

print("Введите элементы второго множества: ")
for _ in range(m):
    set2.add(int(input()))
common = list(set1 & set2)
common.sort()

for num in common:
    print(num)
