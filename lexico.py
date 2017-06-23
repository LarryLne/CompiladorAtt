import json

simbolos_simples = ["(", ")", "*", "/", "+", "-", ">", "<", "$", ";", ":", ","]
simbolos_duplos = ["<>", ">=", "<=", ":="]
palavras_reservadas = ["if", "then", "while", "do", "write", "read", "else",
"begin", "end", "ident", "numero_int","procedure","numero_real", "program", "var","real","integer"]

arquivo = open("teste.txt", "r")

linha_atual = 1  # Toma conta de que em que linha estamos no arquivo, não funciona 100%
token = ''
c = ''

tabela_simbolos = []  # Dicionário para guardar a tabela de simbolos.


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

def reservada_ou_id (token):
    c = token
    while is_char(c) or is_number(c):
        c = read_char()
        if c == ' ' or c== '\t' : # Pula espaços.
            continue
        if is_char(c) or is_number(c):
            token += c
        else:
            if c in simbolos_simples:
                unread_char()
            elif c == '':
                continue
            elif not is_newline(c):
                print("Caracter inválido {} na linha {}".format(repr(c), linha_atual))

    if token in palavras_reservadas:
        tabela_simbolos.append({'Tipo': 'palavra_reservada', "Token": token, "Linha": linha_atual})
        print("Palavra reservada: '{}', linha: {}".format(token, linha_atual))
    else:
        tabela_simbolos.append({'Tipo': 'identificador', "Token": token, "Linha": linha_atual})
        print("Identificador: '{}', linha: {}".format(token, linha_atual))

def inteiro_ou_real (token):
    c = token
    token = ''
    real = False
    if is_number(c):
        while is_number(c):
            token += c
            c = read_char()
            if c == ' ' or c == '\t':  # Pula espaços.
                continue
        if c == '.':
            real = True
            token += c
            c = read_char()
            while is_number(c):
                token += c
                c = read_char()
                if c == ' ' or c == '\t':  # Pula espaços.
                    continue
        else:
            if not is_newline(c):
                print("Caracter inválido {} na linha {}".format(repr(c), linha_atual))
    else:
        is_newline(c)

    if real:
        tabela_simbolos.append({'Tipo': 'numero_real', "Token": token, "Linha": linha_atual})
        print("Numero real: '{}', linha: {}".format(token, linha_atual))
    else:
        tabela_simbolos.append({'Tipo': 'numero_inteiro', "Token": token, "Linha": linha_atual})
        print("Numero inteiro: '{}', linha: {}".format(token, linha_atual))

def comentario1 (token):
    c = token
    while c != "}":
        c = read_char()
        if c == ' ' or c== '\t' : # Pula espaços.
            continue
        is_newline(c)  # fixme: Não tenho certeza se é a melhor forma de checar isso.
        token += c
    if "}" in token:
        print("Comentário: '{}', linha: {}".format(token, linha_atual))
    else:
        # fixme: Olhar isso no futuro.
        print("Caracter inválido {} na linha {}".format(repr(c), linha_atual))
    token = ''

def comentario2 (token):
    t = token
    c = read_char()
    is_newline(c)  # fixme: Não tenho certeza se é a melhor forma de checar isso.
    token += c
    if c == "*":
        flag = False
        while flag == False:
            c = read_char()
            if c == ' ' or c == '\t':  # Pula espaços.
                continue
            is_newline(c)  # fixme: Não tenho certeza se é a melhor forma de checar isso.
            token += c
            if c == "*":
                c = read_char()
                is_newline(c)  # fixme: Não tenho certeza se é a melhor forma de checar isso.
                if c == "/":
                    token += c
                    print("Comentário: '{}', linha: {}".format(token, linha_atual))
                    flag = True

def simbolos(token):
    if token == "<" or token == ">" or token == ":":
        c = read_char()
        simb = token + c
        if simb in simbolos_duplos:
            token += c
            tabela_simbolos.append({'Tipo': 'simbolo_duplo', "Token": token, "Linha": linha_atual})
            print("Simbolo duplo: '{}', linha: {}".format(token, linha_atual))
        else:
            tabela_simbolos.append({'Tipo': 'simbolo_simples', "Token": token, "Linha": linha_atual})
            print("Simbolo simples: '{}', linha: {}".format(token, linha_atual))
    else:
        tabela_simbolos.append({'Tipo': 'simbolo_duplo', "Token": token, "Linha": linha_atual})
        print("Simbolo simples: '{}', linha: {}".format(token, linha_atual))

# todo: Transformar cada etapa em funções !!!
while True:

    if not read_char():
        break
    else:
        unread_char()

    token = read_char()
    # Lê o próximo caracter.

    if not token:
        continue

    if is_newline(token):
        continue

    if token == ' ' or token == '\t':
        continue

    if is_char(token):  # Identificando se é palavra reservada ou identificador.
        reservada_ou_id(token)
    elif is_number(token): # Identifica se é um Numero (inteiro, real)
        inteiro_ou_real(token)
    elif token == "{":  # Identifica comentários
        comentario1(token)
    elif token == "/" and ((read_char() == "*") or unread_char()):
        unread_char()
        comentario2(token)
    elif token in simbolos_simples:  # Identifica se é simbolo simples ou duplo
        simbolos(token)
    else:
         print("Caracter inválido {} na linha {}".format(repr(token), linha_atual))

# Fecha o arquivo ; )
arquivo.close()

# Grava a tabela em um arquivo de texto.
tabela_simbolos_json = json.dumps(tabela_simbolos, sort_keys=True, indent=2)
tabela = open("tabela_simbolos.txt", "w", encoding="utf-8")
tabela.write(tabela_simbolos_json)
tabela.close()
