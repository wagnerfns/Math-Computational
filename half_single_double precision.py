    def half_precision(half):

        sign = half[0] #Pego o bit de sinal
        num_sign = int(sign) # Deixo em inteiro

        expoent = half[1:6]
        num_expoent = int(expoent,2) # Converto o expoente de binario para decimal

        fraction = half[6:]

        print("Sign[{}] - Expoent[{}] - Fraction[{}]".format(sign, expoent, fraction))

        # Condiciono para saber se e subnormal, inifinito e maximo
        
        if(expoent == "00000"): # Subnormal
            print("-> Subnormal number\n\n")
            #Verifica se toda string e zero, assim setando para zero o expoente

            if('0' in half):
                num_expoent = 0
            else:
                num_expoent = 2**(-14)

            num_sign = (-1)**num_sign
            num_fraction = 0

            # So soma o 2^-i se esse elemento for 1 se nao ele passa para o proximo
            for i in range(0, len(fraction)):
                var = 2**((i+1) * -1)
                if(fraction[i] == '1'):
                    num_fraction += var

            num_fraction = 0 + num_fraction 
            print("Precsion: ", num_sign * num_expoent * num_fraction)

        elif(expoent == "11111"): # Infinito
            print("Infinity")
        else:
            print("-> Maximun precision\n\n")

            num_sign = (-1)**num_sign
            num_expoent = 2**(num_expoent - 15)
            num_fraction = 0

            for i in range(0, len(fraction)):
                var = 2**((i+1) * -1)
                if(fraction[i] == '1'):
                    num_fraction += var

            num_fraction = 1 + num_fraction # Somo 1, como está na formula
            print("Precision: ",num_sign * num_expoent * num_fraction) # Ocorre a multiplicacao
  

    def single_precision(single):
        sign = single[0]
        num_sign = int(sign)

        expoent = single[1:9]
        num_expoent = int(expoent,2)

        fraction = single[9:]

        print("Sign[{}] - Expoent[{}] - Fraction[{}]".format(sign, expoent, fraction))

        if(expoent == "00000000"):

            print("-> Subnormal number\n\n")
            #Verifica se toda string e zero, assim setando para zero o expoente
            if('0' in single):
                num_expoent = 0
            else:
                num_expoent = 2**(-127) # Esse elemento muda pois expoencial vai ser 8 bits

            num_sign = (-1)**num_sign
            num_fraction = 0

            for i in range(0, len(fraction)):
                var = 2**((i+1)* -1)
                if(fraction[i] == '1'):
                    num_fraction += var

            num_fraction = 1 + num_fraction
            print("Precision: ",num_sign * num_expoent * num_fraction) 

        elif(expoent == "11111111"):
            print("-> Infinity\n\n")
        else:
            print("-> Maximun precision\n\n")

            num_sign = (-1)**num_sign
            num_expoent = 2**(num_expoent-127)
            num_fraction = 0

            for i in range(0, len(fraction)):
                var = 2**((i+1)* -1)
                if(fraction[i] == '1'):
                    num_fraction += var

            num_fraction = 1 + num_fraction
            print("Precision: ",num_sign * num_expoent * num_fraction)
  

    def double_precision(double):

        sign = double[0]
        num_sign = int(sign)

        expoent = double[1:12]
        num_expoent = int(expoent,2)

        fraction = double[12:]

        print("Sign[{}] - Expoent[{}] - Fraction[{}]".format(sign, expoent, fraction))

        if(expoent == "00000000000"):
            print("-> Subnormal number\n\n")
            #Verifica se toda string e zero, assim setando para zero o expoente

            contagem = 0

            for i in range(0, len(double)):
                if('0' == double[i]):
                    contagem +=1

            if(contagem == len(double)):
                num_expoent = 0
            else:
                num_expoent = 2**(-1023)

            num_sign = (-1)**num_sign
            num_fraction = 0

            for i in range(0, len(fraction)):
                var = 2**((i+1)* -1)
                if(fraction[i] == '1'):
                    num_fraction += var

            num_fraction =  1 + num_fraction

            print("Precision: ",num_sign * num_expoent * num_fraction) 

        elif(expoent == "11111111111"):
            print("-> Infinity\n\n")
        else:
            print("-> Maximun precision\n\n")
            num_sign = (-1)**num_sign
            num_expoent = 2**(num_expoent-1023) # Esse elemento muda pois expoencial vai ser 11 bits
            num_fraction = 0

            for i in range(0, len(fraction)):
                var = 2**((i+1)* -1)
                if(fraction[i] == '1'):
                    num_fraction += var

            num_fraction = 1 + num_fraction
            print("Precision: ",num_sign * num_expoent * num_fraction)



    elemento = str(input("Elemento: "))

    # Condiciono o tamanho da string para half, single e double
    if(len(elemento) == 16):
        print("\nHalf precision\n")
        half_precision(elemento)
    elif(len(elemento) == 32):
        print("\nSingle precision\n")
        single_precision(elemento)
    elif(len(elemento) == 64):
        print("\nDouble precision\n")
        double_precision(elemento)


