from collections import defaultdict

def find_palindrome(s):
    char_count = defaultdict(int) # The functionality of both dictionaries and defualtdict are almost same except for the fact that defualtdict never raises a KeyError
    #keyerror: When we try to access a key that's not in the dictionary
    for c in s:
        char_count[c] +=1 #characters are keys and their occurances are values


    odd_char = ""
    palindrome = ""

    for c, cnt in char_count.items():
        if cnt%2==0:
            palindrome += c*(cnt//2) #add character in c (cnt//2) times to string palindrome. (cnt//2) returns only the integer quotient
        elif not odd_char:
            odd_char = c
            palindrome += c*(cnt//2)
        else:
            return None
    return palindrome + odd_char + palindrome[::-1] #'palindrome[::-1]' reverses the string palindrome

print(find_palindrome('mommo'))