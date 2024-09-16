





def script():
    print("---")
    optype = input("What is the operation? (mult, dev, add, sub, expo)  ")
    if optype != "mult" and optype != "dev" and optype != "add" and optype != "sub" and optype != "expo":
        print("not vaild operator!")
        script()
    else:
        print("---")
        try:
            firstnum = float(input("What is the first number? "))
            print("---")
            secnum = float(input("What is the second number? "))
            print("---")

        except ValueError:
            print("needs to be a number value!")
            script()


        result = 0


        if optype == "mult":
            result = firstnum * secnum
        elif optype == "add":
            result = firstnum + secnum
        elif optype == "sub":
            result = firstnum - secnum
        elif optype == "expo":
            result = firstnum ** secnum
        
        if optype == "dev":
            if firstnum == 0 or secnum == 0:
                print("cannot Divid by zero! try again")
                script()
            else:
                result = firstnum / secnum


        print(str(round(result, 4)))

        restart = str(input("Restart y/n : "))
        if restart == "y":
            print("restarting program")
            script()
        else:
            print("Good Bye :)")

script()
