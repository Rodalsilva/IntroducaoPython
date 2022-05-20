# Programa que leia um valor e que imprima a quantidade de cédulas necessárias para pagar esse mesmo valor
# Contagem de cédulas

valor = int(input("Digite o valor a pagar:"))
cédulas = 0
atual = 50
apagar = valor
while True:
    if atual <= apagar:  # se valor a pagar for maior ou igual ao atual (=50) então subtraímos atual de apagar até que a condição atual <= apagar não mais se verifique:
        apagar -= atual  # apagar = apagar - atual até que apagar seja menor que atual
        cédulas += 1     # para cada valor atual subtraído de apagar acrescenta-se uma cédula

    else:                # se atual > apagar
        print(f"{cédulas} cédula(s) de R${atual}")
        if apagar == 0:
                break
        if atual == 50:     # se apagar for menor que 50 então atual recebe 20
            atual = 20
        elif atual == 20:   # se apagar for menor que 20 então atual recebe 10
            atual = 10
        elif atual == 10:   # se apagar for menor que 10 então atual recebe 5
            atual = 5
        elif atual == 5:    # se apagar for menor que 5 então atual recebe 1
            atual = 1
        cédulas = 0

        # Exemplo: (i) se apagar = 189 então será feito 189 - 50 = 139, 139 - 50 = 89, 89 - 50 = 39, ou seja, foi subtraído 3 valores de atual 50 de 189. Segue-se que temos 3 cédulas de 50.
        # (ii) Como o valor apagar = 39 é menor que atual = 50, a variável atual recebe 20 e seguimos a equação apagar -= atual, i.e, 39 - 20 = 19 e temos 1 cédula de 20.
        # (iii) 19 < 20 então atual recebe 10 e temos 9 = 19 - 10, ou seja, 1 cédula de 10.
        # (iv) 9 < 10 então atual recebe 5 e temos 1 cédula de 5 (4 = 9 - 5).
        # (v) 4 < 5 então atual recebe 1 e temos 4 cédulas de 1.
            

            
