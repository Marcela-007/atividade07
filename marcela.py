# Digite um valor e veja quantos dolares voce poderá comprar: R$
valor = float(input("Insira o valor em reais "))
dolar = float(input("Insira a cotação do dólar atualmente "))
conversao = (valor / dolar)
print("O valor insirido em dólar é " , conversao)