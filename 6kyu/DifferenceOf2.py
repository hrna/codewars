# https://www.codewars.com/kata/5340298112fa30e786000688/python
def twos_difference(lst): 
    result = []
    for a in lst:
        for b in lst:
            if a+2 == b:
                result += [(a,b)]
    return sorted(result)


print(twos_difference([1,3,2,4]))
