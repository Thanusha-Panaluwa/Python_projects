import time
while True:
    print("""
    1. Addition
    2. Substraction
    3. Divition
    4. Multiplication
    """)

    operator = int(input("Proceed the operator:"))

    if operator == 1:
        a = float(input("Write first number:"))
        b = float(input("Write second number:"))
        c = a+b
        print(c)
        time.sleep(2)

    elif operator == 2:
            a = float(input("Write first number:"))
            b = float(input("Write second number:"))
            c = a - b
            print(c)
            time.sleep(2)

    elif operator == 3:
        a = float(input("Write first number:"))
        b = float(input("Write second number:"))
        c = a/b 
        print(c)
        time.sleep(2)

    elif operator == 4:
        a = float(input("Write first number:"))
        b = float(input("Write second number:"))
        c = a*b
        print(c)
        time.sleep(2)

    else:
        print("You have entered wrong input! Please Try again!")
        time.sleep(2)
