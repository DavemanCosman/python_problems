def fibionacci_recursive(n):
    if (n == 0):
        return 0

    if (n == 1):
        return 1
    
    if (n >= 2):
        print(f"input: {n}; {n-1} + {n-2}")
        return fibionacci_recursive(n-1) + fibionacci_recursive(n-2)

if __name__ == "__main__":
    n = int(input())
    print(f"{fibionacci_recursive(n)}")
    