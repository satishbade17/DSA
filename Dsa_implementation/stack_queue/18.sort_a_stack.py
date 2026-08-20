def insertSorted(stack, item):
    if not stack or stack[-1] <= item:
        stack.append(item)
        return

    temp = stack.pop()
    insertSorted(stack, item)
    stack.append(temp)


def sortStack(stack):
    if not stack:
        return

    temp = stack.pop()
    sortStack(stack)
    insertSorted(stack, temp)


# Example
stack = [30, 10, 50, 20, 40]

print("Original Stack:", stack)

sortStack(stack)

print("Sorted Stack:", stack)