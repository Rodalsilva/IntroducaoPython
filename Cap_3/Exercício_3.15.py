#Calculo da redução do tempo de vida de um fumante

cigarros = int(input("Digite a quantidade de cigarros fumados por dia: "))
anos = int(input("Digite a quntidade de anos de uso de cigarros: "))
perda_por_dia = cigarros*10
total_perdido_por_ano =(perda_por_dia)*365/1440
total_perdido = anos*(total_perdido_por_ano)
print(f"O tempo de vida em dias perdido com o consumo de cigarros é: {total_perdido: 5.2f}")
