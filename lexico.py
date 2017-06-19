import json

simbolos_simples = ["(", ")", "*", "/", "+", "-", ">", "<", "$", ";", ":", ","]
simbolos_duplos = ["<>", ">=", "<=", ":="]
palavras_reservadas = ["if", "then", "while", "do", "write", "read", "else", "begin", "end", "ident", "numero_int",
                       "numero_real", "program", "var"]

arquivo = open("teste.txt", "r")

linha_atual = 1  # Toma conta de que em que linha estamos no arquivo, não funciona 100%
token = ''
c = ''

tabela_simbolos = []  # Dicionário para guardar a tabela de símbolos.


def read_char():
    return arquivo.read(1)


def unread_char():
    arquivo.seek(arquivo.tell() - 1, 0)


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

# todo: Transformar cada etapa em funções !!!
while True:

    if not read_char():
        break
    else:
        unread_char()

    token = read_char()  # Lê o próximo caracter.

    if is_char(token):  # Identificando se é palavra reservada ou identificador.
        c = token
        while is_char(c) or is_number(c):
            c = read_char()
            if is_char(c) or is_number(c):
                token += c
            else:
                if not is_newline(c):
                    print("Caracter inválido {} na linha {}".format(repr(c), linha_atual))
        if token in palavras_reservadas:
            tabela_simbolos.append({'Tipo': 'palavra_reservada', "Token": token, "Linha": linha_atual})
            print("Palavra reservada: '{}', linha: {}".format(token, linha_atual))
        else:
            tabela_simbolos.append({'Tipo': 'identificador', "Token": token, "Linha": linha_atual})
            print("Identificador: '{}', linha: {}".format(token, linha_atual))
        token = ''
    elif is_number(token):  # Identifica se é um número (inteiro, real)
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
        if real:
            tabela_simbolos.append({'Tipo': 'número_real', "Token": token, "Linha": linha_atual})
            print("Número real: '{}', linha: {}".format(token, linha_atual))
        else:
            tabela_simbolos.append({'Tipo': 'número_inteiro', "Token": token, "Linha": linha_atual})
            print("Número inteiro: '{}', linha: {}".format(token, linha_atual))
    elif token == "{":  # Identifica comentários
        c = token
        while c != "}":
            c = read_char()
            token += c
        if "}" in token:
            print("Comentário: '{}', linha: {}".format(token, linha_atual))
        else:
            # fixme: Olhar isso no futuro.
            print("Caracter inválido {} na linha {}".format(repr(c), linha_atual))
        token = ''
    elif token == "/" and read_char() == "*":
        unread_char()
        t = token
        c = read_char()
        token += c
        if c == "*":
            flag = False
            while flag == False:
                c = read_char()
                token += c
                if c == "*":
                    c = read_char()
                    if c == "/":
                        token += c
                        print("Comentário: '{}', linha: {}".format(token, linha_atual))
                        flag = True
    # fixme: O Igor acha que aqui dá pra melhorar.
    elif token in simbolos_simples:  # Identifica se é símbolo simples ou duplo
        duplo = False
        c = token
        if c in simbolos_simples:
            if c == "<":
                c = read_char()
                if c == ">" or c == "=":
                    token += c
                    tabela_simbolos.append({'Tipo': 'símbolo_duplo', "Token": token, "Linha": linha_atual})
                    print("Símbolo duplo: '{}', linha: {}".format(token, linha_atual))
                else:
                    tabela_simbolos.append({'Tipo': 'símbolo_simples', "Token": token, "Linha": linha_atual})
                    print("Símbolo simples: '{}', linha: {}".format(token, linha_atual))
                    unread_char()
            elif c == ">" or c == ":":
                c = read_char()
                if c == "=":
                    token += c
                    tabela_simbolos.append({'Tipo': 'símbolo_duplo', "Token": token, "Linha": linha_atual})
                    print("Símbolo duplo: '{}', linha: {}".format(token, linha_atual))
                else:
                    tabela_simbolos.append({'Tipo': 'símbolo_simples', "Token": token, "Linha": linha_atual})
                    print("Símbolo simples: '{}', linha: {}".format(token, linha_atual))
                    unread_char()
            else:
                tabela_simbolos.append({'Tipo': 'símbolo_duplo', "Token": token, "Linha": linha_atual})
                print("Símbolo simples: '{}', linha: {}".format(token, linha_atual))

# Fecha o arquivo ; )
arquivo.close()

# Grava a tabela em um arquivo de texto.
tabela_simbolos_json = json.dumps(tabela_simbolos, sort_keys=True, indent=2)
tabela = open("tabela_simbolos.txt", "w")
tabela.write(tabela_simbolos_json)
tabela.close()
