def findMinAndMax(L):
    Min = None
    Max = None
    for num in L :
        if Min == None or num < Min :
            Min = num
        if Max == None or num > Max :
            Max = num
    return (Min, Max)