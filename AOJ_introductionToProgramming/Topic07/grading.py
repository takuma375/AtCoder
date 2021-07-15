while True:
    m, f, r = list(map(int, input().split()))
    if m == -1 and f == -1 and r == -1:
        break
    
    sum_mf = m + f

    if m == -1 or f == -1:
        print("F")
    elif sum_mf >= 80:
        print("A")
    elif 65 <= sum_mf < 80:
        print("B")
    elif 50 <= sum_mf < 65:
        print("C")
    elif 30<= sum_mf < 50:
        if r >= 50:
            print("C")
        else:
            print("D")
    elif sum_mf < 30:
        print("F")
