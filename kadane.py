
def kadane(nums):
    global_max = -float("inf")
    local_max = -float("inf")
    for items in nums:
        local_max = max(local_max+items, items)
        global_max = max(local_max,global_max)
    return global_max

if __name__ == '__main__':
    arr = [1,2,3]
    ans = kadane(arr)
    print ans