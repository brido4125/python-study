for i in range(int(input())):
    stk = []
    isVPS = True
    for element in input():
        if element == '(':
            stk.append(element)
        else:
            if len(stk) != 0:
                stk.pop()
            else:
                isVPS = False
                break
    if len(stk) != 0:
        isVPS = False
    print("YES" if isVPS else "NO")



