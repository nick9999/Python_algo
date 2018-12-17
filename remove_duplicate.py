def remove_duplicate(str):
    str = "#" + str
    prev = str[0]
    ans = []
    ans.append(str[0])
    i = 1
    while i<len(str):
        prev = ans[-1]
        j = i
        while j<len(str) and str[j]==str[i]:
            j += 1
        if abs(j-i)==1:
            if str[i]!=prev:
                ans.append(str[i])
            else:
                ans.pop()
        i =j
    return "".join(ans[1:])

if __name__ == '__main__':
    str = "azxxzy"
    ans = remove_duplicate(str)
    print ans