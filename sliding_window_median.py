import random
import bisect


def sliding_window_median(nums,k):
    tmp = sorted(nums[0:k])
    odd = k%2
    ans = list()
    start = 0
    for j in nums[k:]:
        i = nums[start]
        med = (tmp[int(k/2)]+tmp[int((k-1)/2)])/2.0 if not odd else (tmp[int((k-1)/2)])*1.0
        ans.append(med)
        tmp.pop(bisect.bisect_left(tmp,i))
        bisect.insort(tmp, j)
        start += 1
    med = (tmp[int(k / 2)] + tmp[int((k - 1) / 2)]) / 2.0 if not odd else (tmp[int((k - 1) / 2)]) * 1.0
    ans.append(med)
    return ans

if __name__ == '__main__':
    nums = [random.randint(0,100) for i in range(20)]
    print nums
    ans = sliding_window_median(nums,6)
    print ans