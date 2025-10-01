# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    k = int(input()) #size of each group
    
    room_numbers = list(
        map(int, input().split())
    )
    #print(f"{k}")
    #print(room_numbers)
    
    roomno_freq = {} # amount of times a room number shows
    for roomno in room_numbers:
        roomno_freq[roomno] = roomno_freq.get(roomno,0)+1
    
    unique_roomnos = list(set(room_numbers))
    for roomno in unique_roomnos:
        if roomno_freq[roomno] ==1:
            print(roomno)
            break
