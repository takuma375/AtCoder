n = int(input())

tbl = [[0 for i in range(1, 14)] for j in range(4)]

for i in range(n):
    category, rank = input().split()
    rank = int(rank) - 1
    if category == "S":
        category = 0
    elif category == "H":
        category = 1
    elif category == "C":
        category = 2
    elif category == "D":
        category = 3
    tbl[category][rank] = rank + 1

for i, row in enumerate(tbl):
    for j, elem in enumerate(row):
        if elem == 0:
            if i == 0:
                print("S ", end="")
                print(j+1)
            elif i == 1:
                print("H ", end="")
                print(j+1)
            elif i == 2:
                print("C ", end="")
                print(j+1)
            elif i == 3:
                print("D ", end="")
                print(j+1)

