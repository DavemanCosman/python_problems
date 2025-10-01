def sum_divisible_by_3_or_5_not_both(numbers):
    total = 0
    for num in numbers:
        if num % 3 == 0 or num % 5 == 0:
            total += num
        if num % 15 == 0:
            total -= num
    return total
    
if __name__ =='__main__':
    print('Please enter a list of integers to check if their sum is divisible by 3 xor 5.') 
    user_input = input('Separate your inputs by commas: ')
    numbers = [int(x.strip()) for x in user_input.split(',')]
    print(f"Return: {sum_divisible_by_3_or_5_not_both(numbers)}")