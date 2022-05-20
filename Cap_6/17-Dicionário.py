# Obtenção de preço com um dicionário

tabela = {"Alface": 0.45,
          "Batata": 1.20,
          "Tomate": 2.30, 
          "Feijão": 1.50}

# A estrutura acima é exemplo de um dicionário, uma estrutura de dados que é similar a uma lista, mas com propriedades de acesso diferentes.
# Um dicionário é composto é composto de um conjunto de chaves e valores. Cada elemento de um dicionário é uma combinação de chave e valor.

while True:
    produto = input("Digite o nome do produto, fim para terminar:")
    if produto == "fim":
        break
    if produto in tabela:
        print(f"Preço {tabela[produto]: 5.2f}")
    else:
        print("Produto não encontrado")

