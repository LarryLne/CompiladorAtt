simbolos_simples = ["(", ")", "*", "/", "+", "-", ">", "<", "$", ";", ":", ","]
simbolos_duplos = ["<>", ">=", "<=", ":="]
palavras_reservadas = ["if", "then", "while", "do", "write", "read", "else", "begin", "end", "ident", "numero_int",
                       "numero_real", "program"]

arquivo = open("teste.txt", "r")
arquivo_fonte = arquivo.read()
arquivo.seek(0, 0)
tamanho_fonte = len(arquivo_fonte)

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
        linha += 1
    else:
        unread_char()

    if is_char(token): # Identificando se é palavra reservada ou identificador.
        c = token
        while is_char(c) or is_number(c):
            c = read_char()
            if is_char(c) or is_number(c):
                token += c
            else:
                print("Caracter inválido {} na linha {}".format(c, linha))

        # todo: Adicionar token em tabela de tokens.
        if token in palavras_reservadas:
            print('Palavra reservada: {}, Linha: {}'.format(token, linha))
        else:
            print('Identificador: {}, Linha: {}'.format(token, linha))
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
    #         print(token, ": numero_real/ linha: ", linha)
    #     else:
    #         print(token, ": numero_inteiro/ linha: ", linha)
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
    #         print(token, ': comentário/ linha: ', linha)
    #     else:
    #         print('erro/ linha: ', linha)
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
    #                     print(token, ': comentário/ linha: ', linha)
    #                     flag = True
    #     else:
    #         print(t, ": símbolo simples/ linha: ", linha)
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
    #                 print(token, " : símbolo_duplo/ linha: ", linha)
    #             else:
    #                 print(token, ": símbolo_simples/ linha: ", linha)
    #                 cursor -= 1
    #
    #         elif c == ">" or c == ":":
    #             cursor += 1
    #             if cursor > tamanho_fonte - 1:
    #                 break
    #             c = arquivo_fonte[cursor - 1]
    #             if c == "=":
    #                 token += c
    #                 print(token, " : símbolo_duplo/ linha: ", linha)
    #             else:
    #                 print(token, ": símbolo_simples/ linha: ", linha)
    #                 cursor -= 1
    #         else:
    #             print(token, ": simbolo simples/ linha: ", linha)
    #         token = ''
    #         c = ''
    #         cursor += 1