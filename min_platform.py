def min_platform(arr,dep):
    a,b = 0,0
    ans = 0
    tmp =0
    while a<len(arr) and b<len(dep):
        if arr[a]<=dep[b]:
            a += 1
            tmp += 1
            ans = max(ans,tmp)
        else:
            b+=1
            tmp -=1
    return ans

if __name__ == '__main__':
    arr = [900 , 940 ,950, 1100, 1500, 1800]
    dep = [910, 1200, 1120, 1130, 1900 ,2000]
    ans = min_platform(arr,dep)
    print ans