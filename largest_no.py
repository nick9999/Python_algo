
def cmp1(x,y):
    return int(y+x)-int(x+y)

def largest_no(nums):
    nums = sorted(nums, cmp=cmp1)
    ans = ""
    for num in nums:
        ans += num
    return ans

if __name__ == '__main__':
    nums = ["3", "30", "34", "5", "9"]
    ans = largest_no(nums)
    print ans