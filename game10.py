n = int(input())
d = int(input())
a = int(input())

count = 0
while a != d:
    if a < n:
        a += 1
    elif a == n:
        a = 1

    count += 1

print(count)
