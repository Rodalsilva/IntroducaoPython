# Em Python, a estrutura de decisão é o 'if'. Seu formato segue um modelo de 'estrutura de seleção':

# if <condição>:
#    bloco verdadeiro

# Nas situações em que duas alternativas dependem de uma mesma condição, uma de a condição ser verdadeira e a outra de a condição ser falsa, usamos a estrutura de 'seleção composta'.
# A estrutura de seleção composta segue o modelo do exemplo abaixo:

idade = int(input("Digite a idade de seu carro:"))
if idade <= 3:
    print("Seu carro é novo")
else:
    print("Seu carro é velho")

# É importante notar que devemos escrever o else na mesma coluna do if. Assim, o interpretador reconhece que else se refere a um determinado if.


