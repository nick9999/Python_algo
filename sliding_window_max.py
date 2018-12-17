import collections

def sliding_window_max(nums,k):
    dq = collections.deque()
    dq.append(0)
    for i in range(k):
        while dq and nums[i]>=nums[dq[-1]]:
            dq.pop()
        dq.append(i)
    ans = []
    ans.append(nums[dq[0]])
    for i in range(k,len(nums)):
        while dq and dq[0] <= i-k:
            dq.popleft()
        while dq and nums[i]>=nums[dq[-1]]:
            dq.pop()
        dq.append(i)
        ans.append(nums[dq[0]])
    return ans


if __name__ == '__main__':
    nums = [12, 1, 78, 90, 57, 89, 56]
    ans = sliding_window_max(nums,3)
    print ans