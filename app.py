def check_even_odd(number):
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")

# Test the function
num = int(input("Enter a number: "))
check_even_odd(num)
