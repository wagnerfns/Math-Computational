from decimal import Decimal 

def converteP(elemento):
    decimal, fracao = elemento.split('.')
 
    if(len(decimal) <= 4):
        print("\nNão deu Overflow\n")
        validade = 0
    else:
        print("\nDeu Overflow\n")
        print("--> {} * 10 ^ {}".format('0.'+decimal+fracao, len(decimal)))
        validade = 1

    trucado = decimal + fracao
    arredondado = str(round(float('0.'+trucado),4))

    if(validade == 0):
        print("Elemento: {}".format(elemento))
        print("\n--> {} * 10 ^ {}".format('0.'+decimal+fracao, len(decimal)))
        print("Elemento Trucado: {}".format('0.'+trucado[:4]))
        print("Elemento Arredondado: {}".format(arredondado[:6]))


def converteN(elemento, tamanho):
    decimal, fracao = elemento.split('.')
    if(0 >= (tamanho * -1) >= -4):
        print("\nNão deu underflow\n")
        validade = 0
    else:
        print("\nDeu underflow\n")
        print("--> {} * 10 ^ -{}".format('0.'+fracao[tamanho:], tamanho))
        validade = 1
    trucado = fracao
    arredondado = str(round(float('0.'+trucado[2:]),4))
    if(validade == 0):
        print("Elemento: {}".format(elemento))
        print("\n--> {} * 10 ^ -{}".format('0.'+fracao[tamanho:], tamanho))
        print("Elemento Trucado: {}".format('0.'+ trucado[tamanho:4]))
        print("Elemento Arredondado: {}".format(arredondado[:6]))


print("Tamanho de 4 digitos aceitos pela maquina para ocorrer arredondadmento ou truncamento")
valor = str(input("Digite o valor: "))

decimal, fracao = valor.split('.')

if(decimal == '0'):
    i = 2
    contador = 0
    while('0' == valor[i]):
        contador+=1
        i+=1
        converteN(valor, contador)
else:
    converteP(valor)
