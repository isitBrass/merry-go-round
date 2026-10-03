def f(n):
    x = [1, 0]
    sv = [0, 1]
    while len(x) < n:
        x.append(x[-1] + x[-2])
        sv.append(sv[-1] + sv[-2])
    ans = (123456123456123456 - sv[-1])
    if (ans % x[-1] != 0):
        ans = 0
    ans = ans // x[-1]
    return ans

ans = []
for i in range(3, 101):
    ans.append(f(i))

ans.sort()
cnt = 0
for i in ans:
    if i == 0:
        cnt += 1
ans = ans[cnt:]

print(*ans)
