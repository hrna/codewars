# https://www.codewars.com/kata/559536379512a64472000053/train/python
import string
def play_pass(s, n):

    alphabets = list(string.ascii_uppercase)
    specialChar = list(string.punctuation)
    splitWord = s.split(" ")
    newWord = ""
    passList = []

    # Check each word through
    for word in splitWord:

        # Check each character from the word
        for letter in word:

            # Check if character is in alphabets but not numeric
            if letter in alphabets and not letter.isnumeric():
                letterIndex = alphabets.index(letter)
                index = letterIndex + n

                # If leap is more than the lenght of the list,
                # start from the beginning of the list
                if index >= len(alphabets):
                    newWord += alphabets[index - len(alphabets)]
                else:
                    newWord += alphabets[index]

            # If numeric replace each digit by its complement to 9
            elif letter.isnumeric():
                diff = 9 - int(letter)
                newWord += str(diff)

            # Keep such as non alphabetic and non digit characters
            elif letter in specialChar:
                newWord += letter

        passList.append(newWord)
        # Reset newWord once appended to list
        newWord = ""

    password = ""

    # Lowercase every odd number of characters
    passString = " ".join(passList)
    count = 0
    for i in passString:
        if count %2 == 0:
            password += i
        else:
            password += i.lower()         
        count += 1

    return password[::-1]
            

print(play_pass("MY GRANMA CAME FROM NY ON THE 23RD OF APRIL 2015", 2))