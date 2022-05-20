# A função 'input' é utilizada para solicitar dados do usuário, recebendo como parâmetro a mensagem a ser exibida e retornando o valor digitado pelo usuário.

nome = input("Digite seu nome:")  # A função input sempre retorna valores do tipo string.
anos = int(input("Anos de serviço:")) # A função 'int' converte o valor retornado em um valor inteiro.
valor_por_ano = float(input("Valor por ano:")) # A função float converte o valor retornado em número decimal ou de ponto flutuante.
bônus = anos*valor_por_ano
print(f"{nome} receberá bônus de R$ {bônus:5.2f}")
