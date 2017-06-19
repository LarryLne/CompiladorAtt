from logging import Logger as log

simbolos_simples = ["(", ")", "*", "/", "+", "-", ">", "<", "$", ";", ":", ","]
simbolos_duplos = ["<>", ">=", "<=", ":="]
palavras_reservadas = ["if", "then", "while", "do", "write", "read", "else", "begin", "end", "ident", "numero_int",
                       "numero_real", "program"]

arquivo = open("teste.txt", "r")

linha_atual = 1 # Toma conta de que em que linha estamos no arquivo, não funciona 100%
token = ''
c = ''

def read_char():
    return arquivo.read(1)

def unread_char():
    arquivo.seek(arquivo.tell() -1 , 0)

def is_char(c):
    return 'a' <= c <= 'z' or 'A' <= c <= 'Z'

def is_number(c):
    return '0' <= c <= '9'

def is_newline(c):
    global linha_atual
    if c == '\n':
        linha_atual += 1
        return True
    return False

while True:

    if not read_char():
        break
    else:
        unread_char()

    token = read_char() # Lê o próximo caracter.

    if is_char(token): # Identificando se é palavra reservada ou identificador.
        c = token
        while is_char(c) or is_number(c):
            c = read_char()
            if is_char(c) or is_number(c):
                token += c
            else:
                if not is_newline(c):
                    print("Caracter inválido {} na linha {}".format(repr(c), linha_atual))
        # todo: Adicionar token em tabela de tokens.
        if token in palavras_reservadas:
            print("Palavra reservada: '{}', linha: {}".format(token, linha_atual))
        else:
            print("Identificador: '{}', linha: {}".format(token, linha_atual))
        token = ''
    elif is_number(token): # Identifica se é um número (inteiro, real)
        c = token
        token = ''
        real = False
        if is_number(c):
            while is_number(c):
                token += c
                c = read_char()
            if c == '.':
                real = True
                token += c
                c = read_char()
                while is_number(c):
                    token += c
                    c = read_char()
            else:
                if not is_newline(c):
                    print("Caracter inválido {} na linha {}".format(repr(c), linha_atual))
        # todo: Adicionar token em tabela de tokens.
        if real:
            print("Número real: '{}', linha: {}".format(token, linha_atual))
        else:
            print("Número inteiro: '{}', linha: {}".format(token, linha_atual))
    # Identifica comentários
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