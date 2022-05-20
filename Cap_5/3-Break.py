# Leitura de valores até que digitemos 0

s = 0
while True: # while será executado para sempre pois o valor de sua condição de parada, i.e, True, é constante
    v = int(input("Digite um número a somar ou 0 para sair:"))
    if v ==0:
        break
    s += v
    print(s)
