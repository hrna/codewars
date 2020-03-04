def spin_words(sentence):
    words = sentence.split(" ")
    s = []
    for word in words:
        if len(word) >= 5:
            word = word[::-1] 
        s.append(word) 
    sentence = " ".join(s)      
    return sentence


print(spin_words("Thissss is a test"))