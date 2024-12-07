x = int(input())
n = int(input())
vec = []
sobra = 0

for _ in range(n):
    vec.append(int(input()))

for usado in vec:
    sobra = x - usado + sobra

print(sobra + x)
