origmax = 0
rmbrow = 1
rmbcol = 1
for row in range(9):
  [*args] = list(map(int,input().split())) # starred assignment target must be in a list or tuple
  newmax = max(args)
  if max(origmax, newmax) != origmax:
    origmax = newmax
    rmbrow = row+1
    rmbcol = args.index(newmax)+1

print(origmax)
print(rmbrow, rmbcol)