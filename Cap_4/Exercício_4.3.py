Num1 = int(input("Digite um número: "))
Num2 = int(input("Digite um número: "))
Num3 = int(input("Digite um número: "))

if Num1 > Num2 and Num1 > Num3:
    print(f"{Num1} é o maior dos três")
if Num2 > Num1 and Num2 > Num3:
    print(f"{Num2} é o maior dos três")
if Num3 > Num1 and Num3 > Num2:
    print(f"{Num3} é o maior dos três")

if Num1 < Num2 and Num1 < Num3:
    print(f"{Num1} é o menor dos três")
if Num2 < Num1 and Num2 < Num3:
    print(f"{Num2} é o menor dos três")
if Num3 < Num1 and Num3 < Num2:
    print(f"{Num3} é o menor dos três")
