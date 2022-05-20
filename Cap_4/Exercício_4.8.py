a = int(input("Digite um primeiro valor: "))
b = int(input("Digite um segundo valor: "))

operação = input("Digite a operação que deseja executar (soma ou multiplicação): ")

if operação == "soma":
    print(a+b)
elif operação == "multiplicação":
    print(a*b)
else:
    print("Operação inválida")

