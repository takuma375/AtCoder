S = input()

dic_dic = {
    "word": "",
    "count": 0,
}

for s in S:
    print(s)
    if s == "c":
        dic_dic["word"] += s
        dic_dic["count"] += 1
    elif s=="h" and "c" in dic_dic:
        dic_dic["word"] += s
        dic_dic["count"] += 1
    elif s == "o" and "ch" in dic_dic:
        dic_dic["word"] += s
        dic_dic["count"] += 1
    elif s == "k" and "cho" in dic_dic:
        dic_dic["word"] += s
        dic_dic["count"] += 1
    elif s == "u" and "chok" in dic_dic:
        dic_dic["word"] += s
        dic_dic["count"] += 1
    elif s == "d" and "choku" in dic_dic:
        dic_dic["word"] += s
        dic_dic["count"] += 1
    elif s == "a" and "chokud" in dic_dic:
        dic_dic["word"] += s
        dic_dic["count"] += 1
    elif s == "i" and "chokuda" in dic_dic:
        dic_dic["word"] += s
        dic_dic["count"] += 1

print(dic_dic)