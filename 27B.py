from math import*
def center(K):
    c = 0
    mns = 1000000
    for t1 in K:
        sm = 0
        for t2 in K:
            sm += dist(t1[:-1], t2[:-1])
        if mns > sm:
            mns = sm
            c = t1
    return c



a = open('27_B_28766.txt').readlines()
for i in range(len(a)):
    a[i] = a[i].replace(',', '.').split()
    a[i][0] = float(a[i][0])
    a[i][1] = float(a[i][1])

K1 = []
K2 = []
K3 = []

for t in a:
    x, y, z = t
    if y < 15:
        K1.append(t)
    elif y < 22:
        K2.append(t)
    else:
        K3.append(t)

C1 = center(K1)
C2 = center(K2)
C3 = center(K3)

def R(K):
    mn = 10000000000
    for t1 in K:
        for t2 in K:
            if t1 != t2:
                x1, y1, z1 = t1
                x2, y2, z2 = t2
                if z1[0] == 'Z' and z1[-1] == 'I' and z1.count('I')==1 and 'V' not in z1:
                    if z2[0] == 'Z' and z2[-1] == 'I' and z2.count('I')==1 and 'V' not in z2:
                        mn = min(dist(t1[:-1], t2[:-1]), mn)
    return mn

B1 = min(R(K1)*10000, R(K2)*10000, R(K3)*10000)
print(B1)

def R2(K):
    k = 0
    for t in K:
        x, y, z = t
        if z[0] == 'Z' and z[-1] == 'I' and z.count('I')==1 and 'V' not in z:
            k += 1

    return k


print(R2(K1)) #9
print(R2(K2)) #1
print(R2(K3)) #3
B2 = dist(C1[:-1], C2[:-1])*10000
print(B2)


