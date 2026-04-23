# items = list(map(int, input("Enter elements separated by space: ").split()))
# total = 0
# for i in items:
#     total = total + i
# print(total)

arr = []
Num = int(input("Enter the number of elements in list: "))

for i in range(Num):
    element = int(input(f"Enter element {i}: "))
    arr.append(element)

print("List:", arr)

total = 0
for i in arr:
    total += i

print("Total:", total)