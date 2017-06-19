simbolos_simples = ["(", ")", "*", "/", "+", "-", ">", "<", "$", ";", ":", ","]
simbolos_duplos = ["<>", ">=", "<=", ":="]
palavras_reservadas = ["if", "then", "while", "do", "write", "read", "else", "begin", "end", "ident", "numero_int",
                       "numero_real", "program"]

arquivo = open("teste.txt", "r")

linha_atual = 0
token = ''
c = 0

def read_char():
    return arquivo.read(1)

def unread_char():
    arquivo.seek(arquivo.tell() -1 , 0)

def is_char(c):
    return 'a' <= c <= 'z' or 'A' <= c <= 'Z'

def is_number(c):
    return '0' <= c <= '9' or c == '.'


while True:

    if not read_char():
        break
    else:
        unread_char()

    token = read_char() # Lê o próximo caracter.

    while token == ' ':
        token = read_char()
        if token != ' ':
            unread_char()
            break

    if read_char() == '\n':
        linha_atual += 1
    else:
        unread_char()

    if is_char(token): # Identificando se é palavra reservada ou identificador.
        c = token
        while is_char(c) or is_number(c):
            c = read_char()
            if is_char(c) or is_number(c):
                token += c
            else:
                print("Caracter inválido {} na linha {}".format(repr(c), linha_atual))
        # fixme: Adicionar token em tabela de tokens.
        if token in palavras_reservadas:
            print("Palavra reservada: '{}', linha: {}".format(token, linha_atual))
        else:
            print("Identificador: '{}', linha: {}".format(token, linha_atual))
        token = ''
    # elif is_number(token): # Identifica se é um número (inteiro, real)
    #     c = token
    #     real = False
    #     while is_number(c):
    #         cursor += 1
    #         if cursor > tamanho_fonte - 1:
    #             break
    #         c = arquivo_fonte[cursor]
    #         while is_number(c):
    #             token += c
    #             cursor += 1
    #             c = arquivo_fonte[cursor]
    #             if c == '.':
    #                 real = True
    #                 cursor += 1
    #                 token += '.'
    #                 while is_number(c):
    #                     token += c
    #                     c = arquivo_fonte[cursor]
    #                     cursor += 1
    #                     if cursor > tamanho_fonte - 1:
    #                         break
    #     if real:
    #         print(token, ": numero_real/ linha_atual: ", linha_atual)
    #     else:
    #         print(token, ": numero_inteiro/ linha_atual: ", linha_atual)
    #
    #     token = ''
    # ### Identifica comentários
    # elif token == "{":
    #     c = token
    #     while c != "}":
    #         cursor += 1
    #         if cursor > tamanho_fonte - 1:
    #             break
    #         c = arquivo_fonte[cursor - 1]
    #         token += c
    #     if "}" in token:
    #         print(token, ': comentário/ linha_atual: ', linha_atual)
    #     else:
    #         print('erro/ linha_atual: ', linha_atual)
    #     token = ''
    #     cursor += 1
    # elif token == "/":
    #     t = token
    #     cursor += 1
    #     c = arquivo_fonte[cursor - 1]
    #     token += c
    #     if c == "*":
    #         flag = False
    #         while flag == False:
    #             cursor += 1
    #             if cursor > tamanho_fonte:
    #                 break
    #             c = arquivo_fonte[cursor - 1]
    #             token += c
    #             if c == "*":
    #                 cursor += 1
    #                 c = arquivo_fonte[cursor - 1]
    #                 if c == "/":
    #                     token += c
    #                     print(token, ': comentário/ linha_atual: ', linha_atual)
    #                     flag = True
    #     else:
    #         print(t, ": símbolo simples/ linha_atual: ", linha_atual)
    #         cursor -= 1
    #     token = ''
    #     c = ''
    #     cursor += 1
    # elif token in simbolos_simples: # Identifica se é símbolo simples ou duplo
    #     if token == "/":
    #         break
    #     duplo = False
    #     c = token
    #     while c in simbolos_simples:
    #         if c == "<":
    #             cursor += 1
    #             if cursor > tamanho_fonte - 1:
    #                 break
    #             c = arquivo_fonte[cursor - 1]
    #             if c == ">" or c == "=":
    #                 token += c
    #                 print(token, " : símbolo_duplo/ linha_atual: ", linha_atual)
    #             else:
    #                 print(token, ": símbolo_simples/ linha_atual: ", linha_atual)
    #                 cursor -= 1
    #
    #         elif c == ">" or c == ":":
    #             cursor += 1
    #             if cursor > tamanho_fonte - 1:
    #                 break
    #             c = arquivo_fonte[cursor - 1]
    #             if c == "=":
    #                 token += c
    #                 print(token, " : símbolo_duplo/ linha_atual: ", linha_atual)
    #             else:
    #                 print(token, ": símbolo_simples/ linha_atual: ", linha_atual)
    #                 cursor -= 1
    #         else:
    #             print(token, ": simbolo simples/ linha_atual: ", linha_atual)
    #         token = ''
    #         c = ''
    #         cursor += 1