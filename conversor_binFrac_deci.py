def conversor(elemento):
    inteiro, fracao = elemento.split('.')

    somaInteiro = 0
    print("Conversão da parte inteira: ")

    inteiro = inteiro[::-1]

    for i in range (0, len(inteiro)):
        valor = int(inteiro[i])
        print('\t\t\t\t',valor, ' * 2 ^', i, ' = ',  valor*2**i )
        valor = valor*2**i
        somaInteiro = somaInteiro + valor

    somaFracao = 0
    print("Conversão da parte fracionada: ")

    for i in range (0, len(fracao)):
        valor = int(fracao[i])
        print('\t\t\t\t', valor, ' * 2 ^', (i+1)*-1, ' = ', valor*2** ((i+1)*-1))
        valor = (valor * 2 ** ((i+1)*-1))
        somaFracao = somaFracao + valor

    print('Elemento na base 10: ', somaInteiro + somaFracao)

elemento = str(input("Digite o binario fracionado: "))

conversor(elemento)