def get_grade(s1, s2, s3):

    # Calculate the mean value
    mean = (s1+s2+s3)/3

    # Check grades based on mean value
    if 90 <= mean <= 100:
        result = "A"
    elif 80 <= mean < 90:
        result = "B"
    elif 70 <= mean < 80:
        result = "C"
    elif 60 <= mean < 70:
        result = "D"
    else:
        result = "F"

    return result


print(get_grade(95, 90, 93))
    