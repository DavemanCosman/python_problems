from itertools import product
import math

if __name__ == '__main__':
    K, M = input().split( )
    
    list_dict = {}
    
    for k in range(int(K)):
        list_input = input().split()
        length = int(list_input[0])
        my_tuple = tuple(map(int, list_input[1:]))
        
        list_dict[f"list{k+1}"] = {'length':length,'my_tuple':my_tuple}
    
    cartesian_product = product(*[list_dict[f"list{i+1}"].get('my_tuple') for i in range(int(K))])
    
    S_list = []
    for item in cartesian_product:
        S = 0
        for i in range(int(K)):
            S += pow( item[i] , 2)       
        S = S%int(M)
        S_list.append(S)
    
    print(max(S_list))
    