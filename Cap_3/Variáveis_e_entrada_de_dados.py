# Em Python, as letras "d","s" e "f" são usadas como marcadores de posição.
# Eles indicam que naquela posição do valor da variável estaremos colocando, respectivamente, uma variável do tipo inteiro, string ou decimal.
# Quando formatamos números decimais, podemos utilizar doi valores antes de finalizar com a letra f.
# O primeiro valor indica o tamanho total em caracteres a reservar; e o segundo, o número de casas decimais.
# Assim, 5.2f nos diz que estaremos imprimindo um número decimal utilizando 5 posições, sendo duas para a parte decimal.
# As variáveis do tipo string suportam algumas operações como a composição, que é uma combinação de tipos diferentes de variáveis para formar uma string.
# Uma forma de compor strings é utilizando o método 'format'.
# Exemplo de format: após a definição dos valores atribuidos a nome, idade, grana, escrevemos: "{} tem {} anos e R${} no bolso.".format(nome, idade, grana).

nome = "Rodrigo"  # Usa-se aspas duplas em variáveis do tipo string.
idade = 36
grana = 55.60
print("{} tem {} anos e R${} no bolso.".format(nome, idade, grana))

# Também temos a seguinte maneira de compor uma string, conhecida como f - string:

print(f"{nome} tem {idade} anos e R${grana} no bolso.")
