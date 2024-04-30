def arraypair(arr,k):
    if len(arr) < 2:
        return

        # Sets for tracking
    seen = set()
    output = set()

    # For every number in array
    for num in arr:

        # Set target difference
        target = k - num

        # Add it to set if target hasn't been seen
        if target not in seen:
            seen.add(num)

        else:
            # Add a tuple with the corresponding pair
            output.add((min(num, target), max(num, target)))
    print(output)

arr=[1,6,0,4,5,-1,-2,8,3]
arraypair(arr,4)
