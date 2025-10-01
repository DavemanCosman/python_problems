def iterative_fibonacci(n):
    if n < 0: # reject negative numbers
        return "Invalid input. Please enter a non-negative integer."
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    
    a, b = 0, 1
    print(f"a = {a}, b = {b}")
    for _ in range(2, n + 1): # iterate from 2 to n + 1
        a, b = b, a + b
        print(f"a = {a}, b = {b}")
    
    return b
    
if __name__ =='__main__':
    print('Please enter a non-negative integer to perform iterative fibonacci')
    n = int(input())
    print(f"Return: {iterative_fibonacci(n)}")
