

def script():
    print("---")
    optype = input("What is the operation? (mult, dev, add, sub)  ")
    print("---")
    firstnum = int(input("What is the first number? "))
    print("---")
    secnum = int(input("What is the second number? "))
    print("---")
    result = 0


    if optype == "mult":
        result = firstnum * secnum
    elif optype == "dev":
        result = firstnum / secnum
    elif optype == "add":
        result = firstnum + secnum
    elif optype == "sub":
        result = firstnum - secnum


    print(str(result))

    restart = str(input("Restart y/n : "))
    if restart == "y":
        print("restarting program")
        script()
    else:
        print("Good Bye :)")

script()