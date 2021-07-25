S = []

for i in range(4):
    S.append(input())

count_H = 0
count_2B = 0
count_3B = 0
count_HR = 0

for i, value in enumerate(S):
    if value == "H":
        count_H += 1
    elif value == "2B":
        count_2B += 1
    elif value == "3B":
        count_3B += 1
    else:
        count_HR += 1

if (count_H == 1) and (count_2B == 1) and (count_3B==1) and (count_HR==1):
    print("Yes")
else:
    print("No")