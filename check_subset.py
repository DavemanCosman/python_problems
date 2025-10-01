# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    T = int(input()) # number of test cases
    for _ in range(T):
        A, B = set(), set() 
        Acount = int(input()) # number of elements in set A
        A.update(input().split()) # set A
        
        Bcount = int(input()) # number of elements in set B 
        B.update(input().split()) # set B
        
        inner_join = A & B
        if inner_join == A:
            print(True)
        else:
            print(False)
            
        # print(f"==Test Case {_+1}==")
        # print(f"count of A = {Acount} | set A = {A}")
        # print(f"count of B = {Bcount} | set B = {B}")
        # print(inner_join)
        
        del A, B