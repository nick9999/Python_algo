
def helper(str,l,r,ans):
    if l==r:
        ans.append("".join(str))
    for i in range(l,r+1):
        str[l],str[i]=str[i],str[l]
        helper(str,l+1,r,ans)
        str[l], str[i] = str[i], str[l]

def string_perm(str):
    ans = []
    str=list(str)
    helper(str,0,len(str)-1,ans)
    return ans

if __name__ == '__main__':
    s = "abc"
    ans = string_perm(s)
    print ans