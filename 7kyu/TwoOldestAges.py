#https://www.codewars.com/kata/511f11d355fe575d2c000001/train/python

def two_oldest_ages(ages):
    '''
    oldest = []
    oldest.append(max(ages))
    ages.pop(ages.index(max(ages)))
    
    if oldest[0] in ages:
        oldest.append(max(ages))
    else:
        for a in ages:
            if max(ages) not in oldest:
                oldest.insert(0, max(ages))
        
    return oldest
    '''

    return sorted(ages)[-2:]
    
print(two_oldest_ages([1, 5, 87, 45, 8, 8]))
print(two_oldest_ages([6, 5, 83, 5, 3, 18]))
print(two_oldest_ages([10, 1]))