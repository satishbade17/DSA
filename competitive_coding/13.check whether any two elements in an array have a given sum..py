arr = [0, 2, 57, 4, 6, 10, 20]
target = 10

seen = set()

for num in arr:
    required = target - num

    if required in seen:
        print("Pair exists:", required, num)
        break

    seen.add(num)
else:
    print("No pair exists")