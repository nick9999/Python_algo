import collections

def customSortString(S, T):

    tmp = collections.Counter(T)
    ans = ""
    for char in S:
        if tmp[char]:
            ans += tmp[char]*char
            del tmp[char]
    for k in tmp:
        ans += tmp[k]*k
    return ans


if __name__ == '__main__':
    S = "cba"
    T = "abcd"
    ans = customSortString(S,T)
    print ans