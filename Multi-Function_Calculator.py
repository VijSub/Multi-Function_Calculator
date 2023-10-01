from fractions import Fraction
from sympy import symbols, Eq
from sympy.solvers import solve
import math


def add():
    total = 0
    
    first_number = int(input("Enter the first number: "))
    total = first_number

    while True:
        user_input = input("Enter another number to add (or press Enter to finish): ")
        
        if user_input == "":
            break
        
        try:
            num = int(user_input)
            total += num
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    print("Sum of entered numbers:", total)

def subtract():
    total = 0  
    
    first_number = int(input("Enter the first number: "))
    total = first_number 
    
    while True:
        user_input = input("Enter another number to subtract (or press Enter to finish): ")
        
        if user_input == "":
            break  
        
        try:
            num = int(user_input)
            total -= num 
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    print("Result of subtraction:", total)


def multiply():
    result = 1    
    
    first_number = int(input("Enter the first number: "))
    result = first_number
    
    while True:
        user_input = input("Enter another number to multiply (or press Enter to finish): ")
    
        if user_input == "":
            break
        
        try:
            num = int(user_input)
            result *= num 
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    print("Result of multiplication:", result)


def divide():
    result = 1    
    
    first_number = int(input("Enter the first number: "))
    result = first_number
    
    while True:
        user_input = input("Enter another number to divide (or press Enter to finish): ")
    
        if user_input == "":
            break
        
        try:
            num = int(user_input)
            result /= num 
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    print("Result of division:", result)

def prime():
    number = int(input("Enter a positive integer: "))

    prime_or_comp = "The number is prime number."

    for test_number in range(2,number):
        # Change the if statement to test one factor here:
        if number%test_number==0:
            prime_or_comp = "The number is a composite number."

    print(prime_or_comp)

def factors():
    number = int(input('Enter an integer: '))

    for test_factor in range(1, number+1):
        if number%test_factor==0:
            print(test_factor)

def solvex():
    import sympy
    x = symbols('x')

    eq_str = input('Enter an equation to solve for x: 0 = ')
    eq = Eq(eval(eq_str), 0)

    solutions = solve(eq, x)

    if len(solutions) == 0:
        print("No solutions found.")
    else:
        print("Number of solutions:", len(solutions))
        for i, solution in enumerate(solutions):
            print(f"x{i + 1} =", solution)

def factor_roots():
    import sympy

    n = int(input('Without the radical, enter a square root to factor: '))

    upper_limit = math.floor(math.sqrt(n)) + 1
    max_factor = 1
    other_factor = 1
    square_root = 1

    for maybe_factor in range(1, upper_limit):
        if n % (maybe_factor ** 2) == 0:
            max_factor = maybe_factor ** 2

    other_factor = n / max_factor

    square_root = int(math.sqrt(max_factor))
    other_factor = int(other_factor)
    output = square_root * sympy.sqrt(other_factor)

    print(f"The factored square root of {n} is: {output}")

def main_menu():
    while True:
        print("Menu:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Prime Number Detection")
        print("6. Finding all factors")
        print("7. Solve for x")
        print("8. Factor square roots")
        print("9. Exit")

        choice = input("Enter the number of your choice (1-9): ")

        if choice == "1":
            print("You selected Addition.")
            add()
        elif choice == "2":
            print("You selected Subtraction.")
            subtract()
        elif choice == "3":
            print("You selected Multiplication.")
            multiply()
        elif choice == "4":
            print("You selected Division.")
            divide()
        elif choice == "5":
            print("You selected Prime Number Detection.")
            prime()
        elif choice == "6":
            print("You selected finding all factors.")
            factors()
        elif choice == "7":
            print("You selected solve for x.")
            solvex()
        elif choice == "8":
            print("You selected factor square roots.")
            factor_roots()
        elif choice == "9":
            print("Exiting the program.")
            break 
        else:
            print("Invalid choice. Please select a valid option (1-9).")

if __name__ == "__main__":
    main_menu()








