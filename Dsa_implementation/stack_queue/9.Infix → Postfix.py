def infix_to_postfix(exp):
    stack = []
    result = []
    prec = {'+':1, '-':1, '*':2, '/':2, '^':3}

    for ch in exp:
        if ch.isalnum():
            result.append(ch)

        elif ch == '(':
            stack.append(ch)

        elif ch == ')':
            while stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()

        else:
            while (stack and stack[-1] != '(' and
                   prec[stack[-1]] >= prec[ch]):
                result.append(stack.pop())
            stack.append(ch)

    while stack:
        result.append(stack.pop())

    return ''.join(result)

print(infix_to_postfix("A+B*(C-D)"))