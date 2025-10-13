from itertools import permutations

if __name__ =='__main__':
    S, k = input().split()
    
    sorted_string = sorted(S)
    
    permuted = [''.join(p) for p in permutations(sorted_string, int(k)]
    permuted.sort()
    print('\n'.join(permuted))    
    # print ('\n'.join(str(pair) for pair in permutations(S,int(k) ) ))
    
    # print('\n'.join(str(pair) for pair in permutations(S, k)) )