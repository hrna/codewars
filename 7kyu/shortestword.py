def find_short(s):
    # your code here
    words =  s.split(" ")
    lenghts = []
    for word in words:
        lenghts.append(len(word))
    l = min(lenghts)    
    return l # l: shortest word length


print(find_short("bitcoin take over the world maybe who knows perhaps"))

