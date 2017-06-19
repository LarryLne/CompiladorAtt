letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
          "x", "w", "y", "z"]
numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]

simbolos_simples = ["(", ")", "*", "/", "+", "-", ">", "<", "$", ";", ":", ","]
simbolos_duplos = ["<>", ">=", "<=", ":="]
palavras_reservadas = ["if", "then", "while", "do", "write", "read", "else", "begin", "end", "ident", "numero_int",
                       "numero_real", "program"]

# comentarios = ["{","}","/*","*/"]
arquivo = open("teste.txt", "r")
arquivo_fonte = arquivo.read()
tamanho_fonte = len(arquivo_fonte)

cursor = 0
linha = 0
token = ''
c = 0


while True:
    if cursor >= tamanho_fonte - 1:
        print("fim do programa!")
        break


    token += arquivo_fonte[cursor]

    while token == ' ':
        cursor += 1
        token = ''

    if c == "\n":
        linha += 1

    # while token == '\n':
    #     cursor += 1
    #     token = ''

    # print(token)
    #### Identificando se é palavra reservada ou identificador.
    if token in letras:
        c = token

        while c in letras or c in numeros:
            cursor += 1

            if cursor > tamanho_fonte - 1:
                break

            c = arquivo_fonte[cursor]

            if c in letras or c in numeros:
                token += c


        if token in palavras_reservadas:
            print(token, ': palavra_reservada/ linha: ', linha)
            # print('linha: ',linha)


        else:
            print(token, ': identificador/ linha: ', linha)
        token = ''

    #### Identifica se é um número inteiro ou real.
    if token in numeros:
        c = token
        real = False
        while c in numeros:
            cursor += 1

            if cursor > tamanho_fonte - 1:
                break
            c = arquivo_fonte[cursor]
            # print(c)
            while c in numeros:

                token += c
                cursor += 1
                c = arquivo_fonte[cursor]
                # print(c)
                if c == '.':
                    real = True
                    cursor += 1
                    token += '.'

                    while c in numeros:

                        token += c
                        c = arquivo_fonte[cursor]
                        cursor += 1
                        # print(c)
                        if cursor > tamanho_fonte - 1:
                            break
                            ##            if c in numeros:
                            ##                token += c
                            ##            elif c == '.':
                            ##                cursor += 1
                            ##                real = True
                            ##                if cursor > tamanho_fonte - 1:
                            ##                   break
                            ##                token += '.'
                            ##
                            ##                #c = arquivo_fonte[cursor]
                            ##                while c in numeros:
                            ##                    token += c
                            ##                    c = arquivo_fonte[cursor]
                            ##                    cursor += 1
                            ##                    print(c)
                            ##                    if cursor > tamanho_fonte - 1:
                            ##                       break
        if real:
            print(token, ": numero_real/ linha: ", linha)
        else:
            print(token, ": numero_inteiro/ linha: ", linha)

        token = ''

    cursor += 1

    ### Identifica comentários
    if token == "{":
        ##print(c, endl='')
        c = token
        while c != "}":

            cursor += 1
            if cursor > tamanho_fonte - 1:
                break
            c = arquivo_fonte[cursor - 1]
            token += c

        if "}" in token:
            print(token, ': comentário/ linha: ', linha)

        else:
            print('erro/ linha: ', linha)

        token = ''
        cursor += 1

    if token == "/":

        t = token
        cursor += 1
        c = arquivo_fonte[cursor - 1]
        # print(c)
        token += c

        if c == "*":
            flag = False

            while flag == False:
                cursor += 1

                if cursor > tamanho_fonte:
                    break

                c = arquivo_fonte[cursor - 1]
                token += c

                if c == "*":
                    cursor += 1
                    c = arquivo_fonte[cursor - 1]

                    if c == "/":
                        token += c
                        print(token, ': comentário/ linha: ', linha)
                        flag = True
        else:
            print(t, ": símbolo simples/ linha: ", linha)
            cursor -= 1

        token = ''
        c = ''
        cursor += 1
        # c = arquivo_fonte[cursor-1]

        ### Identifica se é símbolo simples ou duplo
    if token in simbolos_simples:
        if token == "/":
            break
        duplo = False
        c = token
        while c in simbolos_simples:

            if c == "<":
                cursor += 1

                if cursor > tamanho_fonte - 1:
                    break
                c = arquivo_fonte[cursor - 1]
                # print("casa",c)
                if c == ">" or c == "=":
                    token += c
                    # duplo=True

                    print(token, " : símbolo_duplo/ linha: ", linha)

                else:
                    print(token, ": símbolo_simples/ linha: ", linha)
                    cursor -= 1

            elif c == ">" or c == ":":
                cursor += 1
                if cursor > tamanho_fonte - 1:
                    break
                c = arquivo_fonte[cursor - 1]
                # print("oi", c)
                if c == "=":
                    token += c
                    # duplo  = True
                    print(token, " : símbolo_duplo/ linha: ", linha)
                else:
                    print(token, ": símbolo_simples/ linha: ", linha)
                    cursor -= 1
            else:
                print(token, ": simbolo simples/ linha: ", linha)

            # print(c)

            # print(token)

            token = ''
            c = ''
            cursor += 1





##
##for x in letra:
##    if k == x:
##        print ("true")
##        list = [k]
##    else:
##        print("false")
##
##print ("oi")
##print(list)
####print f.read(1)
