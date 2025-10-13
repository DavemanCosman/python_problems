from itertools import combinations

if __name__ == '__main__':
    S, k = input().split()
    
    sorted_string = sorted(S)
    for i in range(1, int(k)+1):
        combination_list = [''.join(c) for c in combinations(sorted_string, i)]
        combination_list.sort()
        print('\n'.join(combination_list) ) 