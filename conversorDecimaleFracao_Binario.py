def Bin(elemento):
    if (elemento == 0):
        return 0;
    elif(elemento == 1):
        return 1
    binario = ''
    while elemento != 0:
        binario = binario + str(elemento % 2)
        elemento = int(elemento / 2)
    return binario[::-1]

def BinFrac(elemento):
    elemento = str(elemento)
    elemento = str('0.'+ elemento)
    elemento = float(elemento)
    # faz o inteiro ser fração

    binarioFracao = '' # cria uma string
    listaElemento = [] # Cria uma lista

    while (elemento != 0.00):
        elemento = elemento * 2
        auxiliar = elemento
        auxiliar = int(auxiliar) # Usa apenas a parte inteira da iteração
        binarioFracao += str(auxiliar) # Adiciona aparte inteira na string
        elemento = round(elemento - auxiliar,2) # Faz arredondamento das casas decimais

        if (elemento in listaElemento):# Sabe se o elemento começa a se repetir
            break

        listaElemento.append(elemento) # adiciona os elementos em uma lista
    return binarioFracao
   

x = str(input("Valor: "))

if '.' in x:
    decimal, fracao = x.split('.')
    decimal = int(decimal)
    fracao = int(fracao)
    decimal = Bin(decimal)

    fracao =  BinFrac(fracao)
    print("Binario: {}.{}".format(decimal,fracao))
else:
    decimal = int(x)
    decimal = Bin(decimal)
    print("Binario: {}".format(decimal))
