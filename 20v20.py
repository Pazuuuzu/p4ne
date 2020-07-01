i = 1

while i <= 20:
    j = 1
    while j <= 20:
        print("%5d"  % (i * j), end="|")
        j=j+1
    print("")
    i = i + 1