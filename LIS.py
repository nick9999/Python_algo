import bisect


def lis(nums):
    tmp = []
    ans = 1
    tmp.append(nums[0])
    for num in nums:
        if num < tmp[0]:
            tmp[0] = num
        elif num>tmp[-1]:
            tmp.append(num)
            ans += 1
        else:
            tmp[bisect.bisect_left(tmp,num)]=num
    return ans

if __name__ == '__main__':
    nums = [10, 22, 9, 33, 21, 50, 41, 60]
    ans = lis(nums)
    print ans