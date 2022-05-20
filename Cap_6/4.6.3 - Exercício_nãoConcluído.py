primeira = []
while True:
    n = int(input("Digite um número (0 para sair):"))
    if n == 0:
       break
    primeira.append(n)
x = 0
while x < len(primeira):
    print(primeira[x])
    x += 1

segunda = []
while True:
    n = int(input("Digite um número (0 para sair):"))
    if n == 0:
       break
    segunda.append(n)
x = 0
while x < len(segunda):
    print(segunda[x])
    x += 1

terceira = []

P = primeira[:]
P.extend(segunda)

x = 0
while x < len(P):
    y = 0
    while y < len(terceira):
        if P[x] == terceira[y]:
            break
        y = y + 1
    if y == len(terceira):
        terceira.append(P[x])
    x = x + 1
x = 0
while x < len(terceira):
    print(f"{x}: {terceira[x]}")
    x = x + 1



    
            



