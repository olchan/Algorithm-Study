a = int(input())
background = [[0 for _ in range(100)] for _ in range(100)]

for _ in range(a):
  x, y = map(int, input().split())
  x, y = x-1, y-1
  for i in range(x , x+10):
    for j in range(y, y+10):
      background[i][j] = 1

total_sum = sum(sum(row) for row in background)
print(total_sum)