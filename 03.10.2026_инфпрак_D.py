# Первый тур. D

n = 14
s = [[0, 0], [0, 2], [0, 7], [0, 8], [4, 4], [4,7 ], [6, 1], [6, 5], [9, 0], [9, 1], [9, 4], [9, 7], [11, 2], [11, 6]]
ans = 1e9
for i in range(n):
    for j in range(i + 1, n):
        if s[i][0] == s[j][0]:
            continue
        a = (s[i][1] - s[j][1]) / (s[i][0] - s[j][0])
        b = s[i][1] - s[i][0] * a
        vr = 0
        for k in range(n):
            vr += abs(a * s[k][0] + b - s[k][1])
        ans = min(ans, 1 / n * vr)
print(f"{ans:.6f}")