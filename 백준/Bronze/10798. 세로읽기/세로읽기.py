back = []
for i in range(5):
    line = list(input())
    back.append(line)

lenlist = []
for k in back:
    lenlist.append(len(k))

maxlen = max(lenlist)

for i in range(5):
    if len(back[i]) < maxlen:
        back[i].extend([-1]*(maxlen - len(back[i])))

a = ''
for col in range(maxlen):
  for row in range(5):
    a = a + str(back[row][col])

result = a.replace("-1", "")
print(result)