def valid_parentheses(string: str) -> bool:
    stack: list = []
    for i in string:
        if i == '(':
            stack.append(i)
        elif i == ')':
            try:
                stack.pop()
            except:
                return False

    if len(stack) == 0:
        return True
    else:
        return False
