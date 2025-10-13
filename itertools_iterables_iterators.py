from itertools import combinations

if __name__ == '__main__':
    # handle input
    N = int(input()) # num of space separated lowercase English letters
    lcase_list = [str(i.strip()) for i in input().split(' ')]
    K = int(input()) # num of indices to be selected
        
    # Single line consisting of probability that at least one of the K indices contains the letter 'a'
    combination_list = list(combinations(lcase_list, K))
    
    length = len(combination_list)
    valid_combos = 0
    for i in range (length):
        if 'a' in combination_list[i]:
            valid_combos += 1
    
    print("{:.3f}".format(valid_combos/length))