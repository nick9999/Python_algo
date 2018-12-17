def rotatedDigits( N):
    def is_good(num):
        print num
        good = {'0': '0', '1': '1', '2': '5', '5': '2', '6': '9', '8': '8', '9': '6'}
        num = str(num)
        new_num = ""
        for char in num:
            if char not in good:
                return False
            new_num += good[char]
            
        return int(num) != int(new_num)

    ans = 0
    for i in range(N + 1):
        if is_good(i):
            ans += 1
    print ans
    return ans

if __name__ == '__main__':
    rotatedDigits(10)