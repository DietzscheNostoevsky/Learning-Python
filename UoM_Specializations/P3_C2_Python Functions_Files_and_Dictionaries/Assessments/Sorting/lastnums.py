# Create a function called last_four that takes in a single ID number and returns the last four digits.
# For example, the number 17573005 should return 3005.
# Then, use the resulting function to sort the list of ids stored in the variable, ids, from lowest to highest.
# Save this sorted list in the variable, sorted_ids.
# Hint: Remember that only strings can be indexed, so conversions may be needed.

def last_four(x):
    y = str(x)
    return y[-4:]


ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]

sorted_ids = sorted(ids, key=last_four, reverse=False)


ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]
sorted_id = sorted(ids, key=lambda x: str(x)[-4:], reverse=False)
