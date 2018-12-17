import collections


def freq_sort(nums):
    cnt = collections.Counter(nums)
    cnt = collections.Counter.most_common(cnt)
    ans = []
    for items in cnt:
        ans += [items[0]]*items[1]
    print ans

if __name__ == '__main__':
    nums = [2, 3, 2, 4, 5, 12, 2, 3, 3, 3, 12]
    freq_sort(nums)