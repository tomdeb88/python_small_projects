import os
from ascii_art import calculator



def add(n1,n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2

clear=lambda:os.system('clear')

dict={"+":add,
      "-":subtract,
      "*":multiply,
      "/":divide,}


def calculating(number1,number2,operation):
    print(calculator,"\n\n")
    return dict[operation](number1,number2)





while True:
    first_number=float(input("What's  the first number?: "))
    operator=input("+\n-\n*\n/\nPick an operator: ")
    second_number=float(input("What's the next number?: "))

    result=calculating(first_number,second_number,operator)

    print(f'{first_number} {operator} {second_number} = {result}')

    keep_going=input(f"Type 'y' to  continue with {result}, or typr 'n' to start a new calculation:").lower()



    if keep_going=='y':
        while True:
            first_number=result
            operator=input("+\n-\n*\n/\nPick an operator: ")
            second_number=float(input("What's the next number?: "))
            result=calculating(first_number,second_number,operator)
            print(f'{first_number} {operator} {second_number} = {result}')
            keep_going=input(f"Type 'y' to  continue with {result}, or typr 'n' to start a new calculation:").lower()
            if keep_going=='n':
                clear()
                break
    else:
        clear()
        continue           
    
        




    


