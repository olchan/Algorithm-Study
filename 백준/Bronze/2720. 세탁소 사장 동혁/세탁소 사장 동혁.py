
num = int(input())
money = [25, 10, 5, 1]

for _ in range(num):
    tot = int(input())
    
    lst = []
    for unit in money:
        lst.append(str(int(tot // unit)))
        tot = tot % unit
    print(' '.join(lst))