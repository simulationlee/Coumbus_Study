input_str = input()
stack = []
tmp = 1
result = 0

for i in range(len(input_str)):   
    if input_str[i] == '(':
        tmp *= 2
        stack.append(input_str[i])
    elif input_str[i] == '[':
        tmp *= 3
        stack.append(input_str[i])

    elif input_str[i] == ')':
        if not stack or stack[-1] == '[':
            result = 0
            break
        if input_str[i-1] == '(':
            result += tmp
        tmp //= 2
        stack.pop()  
    else:
        if not stack or stack[-1] == '(':
            result = 0
            break
        if input_str[i-1] == '[':
            result += tmp
        tmp //= 3
        stack.pop() 

if stack:
    print(0)
else:
    print(result)
