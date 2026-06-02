# Mini Calculator 

import time

print("\nLoading Calculator" , end="")

for i in range(5):
    print(".", end="", flush=True)
    time.sleep(0.5)

print("\n\nWelcome to Mini Calculator!")

while True:
    try:
        num1 = int(input("Enter First Number: "))
        num2 = int(input("Enter Second Number: "))

        operation = ["Addition", "Substraction", "Multiplication", "Division", "Exit"]

        for num, operators in enumerate(operation, start=1):
            print(f"{num} - {operators}")

        operate = int(input("Choose a Number to Proceed: "))

        if operate == 1:
            sum = num1 + num2
            print("Answer: ", sum)

        elif operate == 2:
            sub = num1 - num2
            print("Answer: ", sub)

        elif operate == 3:
            multi = num1 * num2
            print("Answer: ", multi)

        elif operate == 4:

            if num2 == 0:
                print("\nDivision by Zero is Not Possible.")

            else:
                div = num1 / num2
                print("Answer: ", div)

        elif operate == 5:
            print("\n\nSee You Next Time!, Good Bye")
            exit()

        else:
            print("\nOnly Enter Number from 1 to 5.")

        print("\n" + "="*40 + " Coded by : Basant Jangra " + "="*40)

    except KeyboardInterrupt:
        print("\n\nProgram Closed By User.")
        break

    except ValueError:
        print("\nOnly Number are Allowed.")
        continue
