def guess_blue(blue_start, red_start, blue_pulled, red_pulled):
    
    # Counting whats left
    bLeft = blue_start - blue_pulled
    rLeft = red_start - red_pulled

    # Total left in the bag
    totalLeft = bLeft + rLeft

    # Probability for blue
    return bLeft / totalLeft


print(guess_blue(5, 5, 2, 3))
print(guess_blue(5, 7, 4, 3))
print(guess_blue(12, 18, 4, 6))