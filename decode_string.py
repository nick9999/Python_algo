def decodeString(s):
    stack = []
    stack.append(["", 1])
    num = ""
    for ch in s:
        if ch.isdigit():
            num += ch
        elif ch == '[':
            stack.append(["", int(num)])
            num = ""
        elif ch == ']':
            st, k = stack.pop()
            stack[-1][0] += st * k
        else:
            stack[-1][0] += ch
    return stack[0][0]

if __name__ == '__main__':
    decodeString("3[a2[c]]")
