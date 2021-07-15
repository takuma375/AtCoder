n = int(input())

tbl = [[[0 for i in range(10)] for j in range(3)] for k in range(4)]

for i in range(n):
    b, f, r, v = list(map(int, input().split()))

    tbl[b-1][f-1][r-1] += v

for i, building in enumerate(tbl):
    for j, floor in enumerate(building):
        for k, room in enumerate(floor):
            print(f" {room}", end="")
        print()
    if i < 3:
        print("####################")
