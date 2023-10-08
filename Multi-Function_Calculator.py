from fractions import Fraction
from sympy import symbols, Eq
from sympy.solvers import solve
import math
import sympy
from sympy import *



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

def proportions():
    print("Proportion example: (n1 / d1) = (n2 / d2)")
    print("Enter 0 for an unknown variable")
    
    n1 = float(input("Enter n1: "))
    d1 = float(input("Enter d1: "))
    n2 = float(input("Enter n2: "))
    d2 = float(input("Enter d2: "))

    if n1 == 0:
        answer = (n2 * d1) / d2
        print("n1 =", answer)

    if d1 == 0:
        answer = (n1 * d2) / n2
        print("d1 =", answer)

    if n2 == 0:
        answer = (n1 * d2) / d1
        print("n2 =", answer)

    if d2 == 0:
        answer = (n2 * d1) / n1
        print("d2 =", answer)

def factor_expression():
    eq_str = input("Enter the equation you want to factor (e.g., x**3 - 2*x**2 - 5*x + 6): ")
    
    try:
        
        eq = sympy.sympify(eq_str)
        
        factored_eq = sympy.factor(eq)
    
        print("Factored expression:", factored_eq)
    except sympy.SympifyError:
        print("Invalid input. Please enter a valid equation.")
 
def main_menu():
    while True:
        print("Menu:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Solve proportions")
        print("6. Prime Number Detection")
        print("7. Finding all factors")
        print("8. Solve for x")
        print("9. Factor square roots")
        print("10. Factor expressions")
        print("11. Exit")


        choice = input("Enter the number of your choice (1-11): ")

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
            print("You selected solve proportions.")
            proportions()
        elif choice == "6":
            print("You selected Prime Number Detection.")
            prime()
        elif choice == "7":
            print("You selected finding all factors.")
            factors()
        elif choice == "8":
            print("You selected solve for x.")
            solvex()
        elif choice == "9":
            print("You selected factor square roots.")
            factor_roots()
        elif choice == "10":
            print("You selected factor expressions.")
            factor_expression()
        elif choice == "11":
            print("Exiting the program.")
            break 
        else:
            print("Invalid choice. Please select a valid option (1-11).")


main_menu()








