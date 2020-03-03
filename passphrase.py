# https://www.codewars.com/kata/559536379512a64472000053/train/python
import string
def play_pass(s, n):

    alphabets = list(string.ascii_uppercase)
    digits = list(string.digits)
    specialChar = list(string.punctuation)
    splitWord = s.split(" ")
    newWord = ""
    passList = []

    print(len(alphabets))
    print("---")
    # Check each word through
    for word in splitWord:

        # Check each character from the word
        for letter in word:

            if letter in alphabets:
                letterIndex = alphabets.index(letter)
                print(letterIndex+n)
                newWord += alphabets[letterIndex+n]

            elif letter.isnumeric() and letter in digits:
                diff = 9 - int(letter)
                newWord += str(diff)

            elif letter in specialChar:
                newWord += letter

        passList.append(newWord)
        newWord = ""

    newItem = ""
    newList = []

    for item in passList:
        count = 1
        for i in item:
            if count %2 == 0:
                newItem += i.lower()
            else:
                newItem += i
            count += 1
        newList.append(newItem)
        newItem = ""

    password = " ".join(list(filter(None,newList)))
    return password[::-1]
            

print(play_pass("MY GRANMA CAME FROM NY ON THE 23RD OF APRIL 2015", 2))