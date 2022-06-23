# Exemplo de dicionário sem valor padrão
d = {}
for letra in "abracadabra":
    if letra in d:
        d[letra] = d[letra] + 1
    else:
        d[letra] = 1
print(d)

print(50*"-")

# Exemplo de dicionário com valor padrão

d = {}
for letra in "abracadabra":
    if letra in d:
        d[letra] = d.get(letra, 0) + 1
print(d)
