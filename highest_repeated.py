# This problem was originally provided with a job interview.
# The ask: write a function highest_repeated(str), where str is a sentence with space separated words, and returns the FIRST word with the most amount of repeated letters.
# E.g. "That movie was good!" will return "THAT", because it has 2 t's. The word "GOOD" has 2 o's but it is after "That" in the sentence.

# My solution: I sorted each word to group identical letters, which lets me count repeats in a single pass. This avoids nested loops and works well for small to medium size inputs.
# Room for improvement; I’d optimize this to using a frequency counter, like one provided from collections.Counter, for better performance and clarity. Also, I'd make sure the original word was returned, rather than in all-caps.


def highest_repeated(str):
    list_input = str.upper().split()
    list_length = len(list_input)
    max_letters = 1
    return_string = 'None'

    for _ in range(list_length):
        sorted_string = sorted(list_input[_])
        k, current_max = 0, 1
        while(k < len(sorted_string)-1):
            if(sorted_string[k] == sorted_string[k+1]):
                current_max+= 1
            k+=1
        if current_max > max_letters:
            max_letters=current_max
            return_string = list_input[_]

    return return_string

# Test cases
print(highest_repeated(" ")) #None
print(highest_repeated("That movie was good!")) # THAT
print(highest_repeated("the quick brown fox jumped over the lazy dog")) # None
print(highest_repeated("racecar level")) # RACECAR
print(highest_repeated("ABABABABABABABABABABABABABABABABABABABABABABABABAB CACACACACACACACACACACACACACACACACACACACACACACACACACACACACACACACACACACACACACACACACACACACACACACACACACA AHABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABAB DACACACACACACACACACACACACACACACACACACACACACACACACACACACACACACACACACACA ABABABABABABABABABABABABABABABABABABABABABABABABAB CACACACACACACACACACACACACACACACACACACACACACACACACACACACACACACACACACACACACACACACACACACACACACACACACACA AHABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABAB DACACACACACACACACACACACACACACACACACACACACACACACACACACACACACACACACACACA")) # CACACACACACACACACACACACACACACACACACACACACACACACACACACACACACACACACACACACACACACACACACACACACACACACACACA
