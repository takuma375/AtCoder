n, m = list(map(int, input().split()))
matrix = [[0 for i in range(m)] for j in range(n)]
vec_b = [[0] for i in range(m)]

for i in range(n):
    row = list(map(int, input().split()))
    for j, value in enumerate(row):
        matrix[i][j] = value

for i in range(m):
    value = int(input())
    vec_b[i][0] = value

vec_c = [[0] for i in range(n)]

for i in range(n):
    value_c = 0
    for j in range(m):
        value_c += matrix[i][j] * vec_b[j][0]
    vec_c[i][0] = value_c

for i in range(n):
    print(vec_c[i][0])