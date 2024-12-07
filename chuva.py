(l, c) = map(int, input().split())
vec = []
for _ in range(l):
  linha = input()
  vlinha = list(linha)
  vec.append(vlinha)
for i in range(0, len(vec)):
  j = 0
  while j < len(vec[0]):
      if vec[i][j] == ".":
          try:
            if (vec[i - 1][j] == "o") or (vec[i][j - 1] == "o" and vec[i + 1][j - 1] == "#") or (vec[i][j + 1] == "o" and vec[i + 1][j + 1] == "#"):
              vec[i][j] = "o"
              j -= 1
              continue
          except:
              pass
      j += 1  
for l in vec:
  l = "".join(l).strip()
  print(l)
