import re
l1 = []
d = {}
scores = {}
n = int(input())
for x in range(n):
    l1.append(re.split('[: ]', input()))

for i in range(0, len(l1)):
    d[l1[i][0] + ' ' + l1[i][1]] = {}
    for j in range(2, len(l1[i])):
        if j % 2 == 1:
            l1[i][j] = int(l1[i][j])

for i in range(0, len(l1)):
    d[l1[i][0] + ' ' + l1[i][1]][]


print(l1)
print(d)