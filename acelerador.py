km = int(input())

km = km - 3
voltas = km // 8
km = km - (voltas * 8)

if km == 3:
    print(1)
elif km == 4:
    print(2)
elif km == 5:
    print(3)