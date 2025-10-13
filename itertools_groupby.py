from itertools import groupby

if __name__ == '__main__':
    S = str(input())
    
    for key, group in groupby(S):
        my_tuple = (list(group).count(key), int(key))
        print(f"{my_tuple} ", end='')