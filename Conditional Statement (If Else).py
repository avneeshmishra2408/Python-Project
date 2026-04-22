# number = int(input("Enter the Number :"))
# if number % 2 == 0 :
#     print("Number is Even")
# else:
#     print("Number is Odd")

Indian = ["Litti", "DaalBati", "Roti"]
Chinese = ["Egg Roll", "Momos", "Fried Rice"]
Italian = ["Pizza", "Pasta"]

Dish = input("Dish Name :\n")
if Dish in Indian:
    print("Indian Dish")
elif Dish in Chinese:
    print("Chinese Dish")
else:
    print("Italian")
