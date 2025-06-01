# Get input from the user
num = int(input("Enter a number: "))

def check_even_odd(number):
    if number % 2 == 0:
        print(f"{number} is an even number.")
    else:
        print(f"{number} is an odd number.")

# Call the function to check if the number is even or odd
check_even_odd(num)