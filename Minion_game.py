def minion_game(string):
    stuart_score = 0
    kevin_score = 0
    length = len(string)

    for i in range(length):
        if string[i].upper() in 'AEIOU':
            kevin_score += length-i
        else:
            stuart_score += length-i

    if stuart_score > kevin_score:
        print("Stuart", stuart_score)
    elif kevin_score > stuart_score:
        print("Kevin", kevin_score)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)