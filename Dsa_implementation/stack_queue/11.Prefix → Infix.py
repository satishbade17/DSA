def prefix_to_infix(exp):
    stack = []

    for ch in reversed(exp):
        if ch.isalnum():
            stack.append(ch)
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            stack.append("(" + op1 + ch + op2 + ")")

    return stack[-1]

print(prefix_to_infix("*+AB-CD"))