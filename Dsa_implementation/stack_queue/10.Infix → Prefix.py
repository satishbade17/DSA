def precedence(op):
    if op in ['+', '-']:
        return 1
    elif op in ['*', '/']:
        return 2
    elif op == '^':
        return 3
    return 0

def infix_to_postfix(exp):
    stack = []
    result = []

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
                   precedence(stack[-1]) >= precedence(ch)):
                result.append(stack.pop())
            stack.append(ch)

    while stack:
        result.append(stack.pop())

    return ''.join(result)

def infix_to_prefix(exp):
    exp = exp[::-1]

    temp = ""
    for ch in exp:
        if ch == '(':
            temp += ')'
        elif ch == ')':
            temp += '('
        else:
            temp += ch

    return infix_to_postfix(temp)[::-1]

print(infix_to_prefix("(A+B)*(C-D)"))