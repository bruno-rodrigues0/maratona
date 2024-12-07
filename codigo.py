n = int(input())
string = input()

string = "".join(string.split())
# lista = list(map(int, input().split()))
count = 0

for _ in range(len(string)):
    pos = string.find("100")

    if pos != -1:
        count += 1
        string = string[pos + 3:]   
    
    else:
        continue

print(count)
