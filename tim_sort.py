
BLOCK = 2


def insertion_sort(arr, l, r):
    for i in range(l+1,r+1):
        tmp = arr[i]
        j = i-1
        while arr[j] > tmp and j>= l:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = tmp
    return


def merge_sort(arr, l, r, m):
    tmp = [0]*(r-l+1)
    i, j, k = l, m+1, 0
    while i <=m and j <=r:
        if arr[i]<=arr[j]:
            tmp[k] = arr[i]
            i += 1
            k += 1
        else:
            tmp[k] = arr[j]
            j += 1
            k += 1
    while i <= m:
        tmp[k] = arr[i]
        k += 1
        i += 1
    while j<=r:
        tmp[k] = arr[j]
        j += 1
        k += 1
    arr[l:r+1] = tmp
    return


def tim_sort(arr, n):
    for i in range(0,n,BLOCK):
        insertion_sort(arr,i,min(i+BLOCK-1,n-1))

    sz = BLOCK
    while sz < n:
        for l in range(0, n, 2*sz):
            merge_sort(arr, l, min(l+2*sz-1,n-1),l+sz-1)
        sz *= 2


if __name__ == '__main__':
    arr = range(31,0,-1)
    tim_sort(arr, len(arr))
    print arr



