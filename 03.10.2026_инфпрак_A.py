def f(n):
    x = [1, 0]
    su1 = 1
    sv = [0, 1]
    su2 = 1
    while len(x) < n:
        x.append(x[-1] + x[-2])
        su1 += x[-1]
        sv.append(sv[-1] + sv[-2])
        su2 += sv[-2]

    ans = (123456123456123456 - su2) / su1
    if ans < 0 or int(ans) != ans: ans = 0
    return int(ans)

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
