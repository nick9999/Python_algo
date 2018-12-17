
def largest_01(nums):
    for i in range(len(nums)):
        if not nums[i]:
            nums[i]= -1
    sum_map = {}
    sum = nums[0]
    sum_map[sum] = 0
    ans = 0
    for i in range(1,len(nums)):
        sum += nums[i]
        if sum == 0:
            ans = max(ans,i+1)
        elif sum in sum_map:
            ans = max(ans,i-sum_map[sum])
        else:
            sum_map[sum] = i
    print ans

if __name__ == '__main__':
    nums = [1, 1, 1, 1, 1]
    largest_01(nums)