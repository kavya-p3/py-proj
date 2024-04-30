lst = [4, 2, 9, 7]
output = [1]*len(lst)
product = 1
i = 0

while i < len(lst):
    # Set index as cumulative product
    output[i] = product

    # Cumulative product
    product *= lst[i]

    # Move forward
    i += 1

# Now for our Greedy run Backwards
product = 1

# Start index at last (taking into account index 0)
i = len(lst) - 1

# Until the beginning of the list
while i >= 0:
    # Same operations as before, just backwards
    output[i] *= product
    product *= lst[i]
    i -= 1

print(output)