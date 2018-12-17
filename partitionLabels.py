import operator

def partitionLabels(S):
    map_list = dict()
    for idx, char in enumerate(S):
        if char in map_list.keys():
            map_list[char][1] = idx
        else:
            map_list[char] = [idx, idx]
    map_list = sorted(map_list.values())
    print map_list
    tmp = list()
    for elem in map_list:
        start,end = elem
        if len(tmp) ==0:
            tmp.append(elem)
        else:
            if tmp[-1][1] > start:
                tmp[-1][1] = max(end,tmp[-1][1])
            else:
                tmp.append(elem)
    print tmp
    return [x[1]-x[0]+1 for x in tmp]


if __name__ == '__main__':
    S="ababcbacadefegdehijhklij"
    ans =partitionLabels(S)
    print ans