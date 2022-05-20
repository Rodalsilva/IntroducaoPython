# Exemplo de estrutura de seleção encadeada homogênea se-senão-se:

categoria = int(input("Digite a categoria do produto: "))
if categoria == 1:
    preço = 10
elif categoria == 2:
    preço = 18
elif categoria == 3:
    preço = 23
elif categoria == 4:
    preço = 26
elif categoria == 5:
    preço = 31
else:
    print("Cateoria inválida, digite um valor entre 1 a 5!")
    preço = 0
print(f"O preço do produto é: R${preço:6.2f}")

# A cláusula elif substitui o par else if, evitando problemas de deslocamentos desnecessários à direita que ocorre com múltiplos if's aninhados. (Ver livro, páginas 80-83)
