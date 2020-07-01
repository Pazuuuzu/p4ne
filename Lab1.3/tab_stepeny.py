def classify(i):
    if not (i % 2):
        return ""
    elif not (i % 3):
        return "45"
    elif not (i % 5):
        return "46"
    else:
        return "42"
i = 1

while i <= 20:
    j = 1
    while j <= 20:
       # print("%5d"  % (i * j), end="|")
       print("\x1b[%sm%4d\x1b[39m" %(classify(i * j), i * j), end="")
       j = j + 1
    print("")
    i = i + 1