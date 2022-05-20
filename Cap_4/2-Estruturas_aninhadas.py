# Quando, devido à necessidade de processamento, agruparmos vários if's, i.e, várias seleções, vamos então obter uma 'estrutura aninhada' ou uma 'seleção encadeada'.
# Quando nao conseguimos identificar um padrão lógico de construção de uma seleção encadeada, a chamamos então de seleção encadeada heterogênea. Exemplo:

# Tipo de triângulo

A = int(input(" Digite um valor para A: "))
B = int(input(" Digite um valor para B: "))
C = int(input(" Digite um valor para C: "))
 
if A < B + C and B < A + C and C < A + B:
        if A == B and B == C:
            print ("Triângulo Equilátero")
        else:
            if A == B or A == C or B == C:
                print("Triângulo Isósceles")
            else:
                print("Triângulo Escaleno")
else:
    print("Estes valores nao formam um triângulo")
