def add(x,y):
    return x + y;
def subtract(x,y):
    return x - y;

while True:
    print("Select operation.")
    print("1.Add      : + ")
    print("2.Subtract : - ")
    print("3.Multiply : * ")
    print("4.Divide   : / ")
    print("5.Power    : ^ ")
    print("6.Remainder: % ")
    print("7.Terminate: # ")
    print("8.Reset    : $ ")
    
    choice = input("Enter Choice : ")
    if choice in ('1','2','3','4','5','6','7','8'):
        num1 = int(input("Enter First Number = "))
        num2 = int(input("Enter 2nd Number = "))
    
        if choice == '1':
            print(num1, "+", num2, "=", add(num1,num2))
        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1,num2))
    
