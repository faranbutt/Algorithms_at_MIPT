def popper(x):
    stack  = []
    d = {')':'(','}':'{',']':'['}
    for i in x:
        if i in '[{(':
            stack.append(i)
        elif i in ')}]':
            if not stack or stack[-1] != d[i]:
                return 'no'
            stack.pop()
    return 'yes' if not stack else 'no'


a = list(input())
print(popper(a))