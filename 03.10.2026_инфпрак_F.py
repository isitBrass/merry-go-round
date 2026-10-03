import random

sled = {'A' : "MD", 'E' : "TSM", 'I' : "TSM", 'T' : "LN", 'M' : "LN", 'N' : "AI", 'D' : "AI", 'S' : "EID", 'L' : "EID"}

def f():
    ans = 2
    s = "DS"
    while True:
        ans += 1
        var = sled[s[-1]]
        s += random.choice(var)
        if (s[-2] + s[-1] == 'ML'): break
    return ans

random.seed(1757373)
n = 60000
ans = 0
for i in range(n):
    ans += f()
print(ans / n)
