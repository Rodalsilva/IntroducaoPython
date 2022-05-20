velocidade = float(input("Digite sua velocidade em Km/h: "))
if velocidade < 80:
    print("Tu não vive não?")
if velocidade > 80:
    multa = 5*(velocidade - 80)
    print("Você foi multado")
    print(f"Valor da multa: R$ {multa:5.2f}")
    
    
