simbolos_simples = ["(", ")", "*", "/", "+", "-", ">", "<", "$", ";", ":", ","]
simbolos_duplos = ["<>", ">=", "<=", ":="]
palavras_reservadas = ["if", "then", "while", "do", "write", "read", "else", "begin", "end", "ident", "numero_int",
                       "numero_real", "program"]

arquivo = open("teste.txt", "r")
arquivo_fonte = arquivo.read()
arquivo.seek(0, 0)
tamanho_fonte = len(arquivo_fonte)

cursor = 0
linha = 0
token = ''
c = 0

def read_char():
    return arquivo.read(1)

def unread_char():
    arquivo.seek(arquivo.tell() -1 , 0)

def is_char(c):
    return 'a' <= c <= 'z' or 'A' <= c <= 'Z'

# todo: provavelmente eu vou deletar esse c == '.'
def is_number(c):
    return '0' <= c <= '9' or c == '.'


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

    if is_char(token):
        c = token

        while is_char(c) or is_number(c):
            cursor += 1

            if cursor > tamanho_fonte - 1:
                break

            c = arquivo_fonte[cursor]

            if is_char(c) or is_number(c):
                token += c

        if token in palavras_reservadas:
            print(token, ': palavra_reservada/ linha: ', linha)
            # print('linha: ',linha)


        else:
            print(token, ': identificador/ linha: ', linha)
        token = ''

    #### Identifica se é um número inteiro ou real.
    if is_number(token):
        c = token
        real = False
        while is_number(c):
            cursor += 1
            if cursor > tamanho_fonte - 1:
                break
            c = arquivo_fonte[cursor]
            while is_number(c):
                token += c
                cursor += 1
                c = arquivo_fonte[cursor]
                if c == '.':
                    real = True
                    cursor += 1
                    token += '.'
                    while is_number(c):
                        token += c
                        c = arquivo_fonte[cursor]
                        cursor += 1
                        if cursor > tamanho_fonte - 1:
                            break
        if real:
            print(token, ": numero_real/ linha: ", linha)
        else:
            print(token, ": numero_inteiro/ linha: ", linha)

        token = ''

    cursor += 1

    ### Identifica comentários
    if token == "{":
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
                if c == ">" or c == "=":
                    token += c
                    print(token, " : símbolo_duplo/ linha: ", linha)
                else:
                    print(token, ": símbolo_simples/ linha: ", linha)
                    cursor -= 1

            elif c == ">" or c == ":":
                cursor += 1
                if cursor > tamanho_fonte - 1:
                    break
                c = arquivo_fonte[cursor - 1]
                if c == "=":
                    token += c
                    print(token, " : símbolo_duplo/ linha: ", linha)
                else:
                    print(token, ": símbolo_simples/ linha: ", linha)
                    cursor -= 1
            else:
                print(token, ": simbolo simples/ linha: ", linha)
            token = ''
            c = ''
            cursor += 1