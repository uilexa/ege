from math import sqrt
def delit(n):
    de = set()
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            de.add(i)
            de.add(n // i)
    return sorted(de)

cnt = 0
for i in range(700001, 1000000):
    s = delit(i)
    d = []
    for x in s:
        if x % 10 == 7 and x != 7:
            d.append(x)
    if len(d) >= 1:
        print(i, min(d))
        cnt += 1
    if cnt == 5:
        break