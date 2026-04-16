s = open('24_28765.txt').readline().replace('BC', '*#')
L = -1
bc = 0
mx = 0
for R in range(len(s)):
    if s[R] == '#':
        bc += 1
    while bc > 180:
        if s[L] == '*':
            bc -= 1
        L += 1
    mx = max(mx, R - L + 1)

print(mx)
