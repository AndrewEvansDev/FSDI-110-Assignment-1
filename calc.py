#imports
from my_math import is_it_odd, print_n_times

#global variables

#functions

def print_menu():
    print("  Welcome to python")
    print("---------------")
    print("1 - sum")
    print("2 - subtract")
    print("3 - multiply")
    print("4 - divide")
    print("5 - is it odd?")
    print("6 - print hello n times")
    print("7 - Is it prime ?")

    print("q - quit")
    print("---------------")



#instructions
selected_option = ""
while(selected_option != 'q'):
    
    print("\n\n")
    print_menu()

    selected_option = input("choose an option: ")
    if(selected_option == "q"):
        exit
    print("")

    num1 = float(input("provide num1: "))
    num2 = float(input("provide num2: "))

    if(selected_option == '1'):
        res = num1 + num2
        print(f"result: + {res}")

    elif(selected_option == '2'):
        res = num1 - num2
        print(f"result:  {res}")

    elif(selected_option == '3'):
        res = num1 * num2
        print(f"result: {res}")
    
    elif(selected_option == '4'):
        res = num1 / num2
        print(f"result: {res}")
    
    elif(selected_option == '5'):
        if(is_it_odd(num1)):
            print("your number is odd")
        else:
            print("your number is even")
    elif(selected_option == '6'):
        print_n_times("hello there!")
