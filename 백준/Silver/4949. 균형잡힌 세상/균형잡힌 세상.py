while True:
    stack = []
    s = input()
    is_balanced = True

    if s == '.':
        break
    
    for char in s:
        if char in "([":
            stack.append(char)
        elif char == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                is_balanced = False
        elif char == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                is_balanced = False

    if is_balanced and not stack:
        print("yes")
    else:
        print("no")