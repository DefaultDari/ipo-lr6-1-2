rows = 4
columns = 4
value = [-3,-5,-2,-12,0,15,4,7,2]
arr = [[0 for _ in range(columns)] for _ in range(rows)]
index = 0
for i in range(4):
    for j in range(4):
        arr[i][j] = value[index % len(value)]
        index += 1
for row in arr:
    print("\t".join(map(str,row)))