def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
print("CALCULATOR MENU")
print("1.sum\n")
print("2.subtract\n")
print("3.multiply\n")
print("4.divide\n")
print("5.Exist\n")
choice=input("Enter your choice:")
if choice=='5':
    print("Existing...")
elif choice in ['1','2','3','4']:
     a=int(input("Enter your first number:"))
     b=int(input("Enter your second number:"))
     if choice=='1':
        print("Sum of",a,"and",b,"is",add(a,b))
     elif choice=='2':
         print("Subtract",a,"and",b,"is",subtract(a,b))
     elif choice=='3':
         print("Multiply",a,"and",b,"is",multiply(a,b))
     elif choice=='4':
          print("Divide",a,"and",b,"is",divide(a,b))
else:
    print("Invalid Choice")
