def pivot_element(nums):
    if len(nums) == 0:
        return -1
    l,r = 0, len(nums)-1
    if nums[l]<= nums[r]:
        return 0
    while l<=r:
        mid = (l+r)/2
        if mid < len(nums)-1 and nums[mid]>nums[mid+1]:
            return mid+1
        elif nums[l]<=nums[mid]:
            l = mid+1
        else:
            r = mid -1
    return 0


def normal_bin_serach(nums, key):
    if not len(nums):
        return -1
    l, r = 0, len(nums)-1
    while l<=r:
        m = l + (r-l)/2
        if nums[m] == key:
            return m
        if key < nums[m]:
            r = m-1
        else:
            l = m+1
    return -1


def gen_bin_search(nums, key):
    if not len(nums):
        return -1
    l,r = 0, len(nums)-1
    while l <= r:
        m = l + (r-l)/2
        if nums[m] == key:
            return m
        if nums[l] <= nums[m]:
            if nums[l] <= key <= nums[m]:
                r = m-1
            else:
                l = m+1
        else:
            if nums[m] <= key <= nums[r]:
                l = m+1
            else:
                r = m-1
    return -1

if __name__ == '__main__':
    arr = [5,6,7,8,1,2,3,4]
    arr1 = [1,2,3,4]
    arr2 = [2,3,4,1]
    print pivot_element(arr)
    print pivot_element(arr1)
    print pivot_element(arr2)
    print gen_bin_search(arr,2)
    print gen_bin_search(arr1,2)
    print gen_bin_search(arr2,2)
    print normal_bin_serach(arr1,3)