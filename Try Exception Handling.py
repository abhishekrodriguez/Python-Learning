print("Enter the 1st number")
num1=input()
print("Enter the 2nd number")
num2=input()
try:
    print("the sum of these two no is",
          int(num1)+int(num2))
except Exception as e:
    print(e)