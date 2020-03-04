#https://www.codewars.com/kata/545cedaa9943f7fe7b000048/train/python

import string

def is_pangram(s):

    # Construct a list holding letters
    letters = list(string.ascii_lowercase)

    # Transform the sentence into lower
    s = s.lower()

    # Loop and pop out a letter if found in the list
    for l in s:
        if l in letters: letters.pop(letters.index(l))

    result = not letters and True or False
    return result

pangram = "The quick, brown fox jumps over the lazy dog!"
print(is_pangram(pangram))
