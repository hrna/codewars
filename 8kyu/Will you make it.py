def zero_fuel(distance_to_pump, mpg, fuel_left):
    
    reachable = mpg*fuel_left

    # Check if there is enough fuel to cover the distance to pump
    if reachable >= distance_to_pump:
        return True
    else:
        return False

print(zero_fuel(50, 25, 2))
print(zero_fuel(100, 50, 1))