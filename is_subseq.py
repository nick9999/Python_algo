from collections import defaultdict
import bisect

def isSubsequence(s, t):
    if len(s)>len(t):
        return False

    char_map = defaultdict(list)
    for idx, char in enumerate(t):
        char_map[char].append(idx)
    print char_map
    prev = char_map[s[0]][0]
    char_map[s[0]] =char_map[s[0]][1:]
    print prev
    for char in s[1:]:
        if not len(char_map[char]) or char not in char_map or prev > char_map[char][-1]:
            return False
        else:
            tmp = char_map[char]
            prev = tmp[bisect.bisect_left(tmp,prev)]
            print prev
            char_map[char] = tmp[1:]
    return True




if __name__ == '__main__':
    ans= isSubsequence("axc","ahbgdc")
    print ans