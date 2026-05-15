x = input("Enter the num1:" )
y = input("Enter the num2:" )

try:
    z = int(x)/int(y)
except Exception as e:
    print("Exception: ",e)
    z = None
print("Output" ,z)