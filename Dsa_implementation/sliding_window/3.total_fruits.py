def totalfruits(arr):
    basket = {}          # Stores fruit count in current window
    start = 0            # Left pointer
    max_fruit = 0        # Maximum fruits collected

    for end in range(len(arr)):      # Right pointer
        # Add current fruit to basket
        basket[arr[end]] = basket.get(arr[end], 0) + 1

        # If more than 2 fruit types, shrink window
        while len(basket) > 2:
            basket[arr[start]] -= 1

            if basket[arr[start]] == 0:
                del basket[arr[start]]

            start += 1

        # Update maximum window size
        max_fruit = max(max_fruit, end - start + 1)

    return max_fruit

arr = [1, 2, 1]
print(totalfruits(arr))