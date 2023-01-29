def isSubsequence(s,t):
    if len(s) == 0:
        return True
    ans, target = [], 0
    for i in range(len(t)):
        ans.append(t[i])
        if ans[-1] != s[target]:
            ans.pop()
        else:
            target += 1
        if len(ans) == len(s):
            break
    return "".join(ans) == s