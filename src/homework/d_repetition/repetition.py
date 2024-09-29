# Create a function named get_factorial
# Parameter: Some number N
# Returns the factorial of number N

def get_factorial(number):
    product = int(number)
    for n in range(number):
        if ((number - n) > 2):
            start_value = product
            product *= (number - n - 1)
            print(n, n-1, start_value, product)
    return product

print(get_factorial(5))