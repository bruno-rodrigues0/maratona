letra = input()
frase = input()

array = frase.split()
count = 0

for palavra in array:
    if palavra.find(letra) != -1:
        count += 1

print(f"{(count / len(array)) * 100:.1f}")


