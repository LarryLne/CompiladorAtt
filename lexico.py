class Lexer():
    def __init__(self, nome_arquivo_fonte):
        self.simbolos_simples = ["(", ")", "*", "/", "+", "-", ">", "<", "$", ";", ":", ","]
        self.simbolos_duplos = ["<>", ">=", "<=", ":="]
        self.palavras_reservadas = ["if", "then", "while", "do", "write", "read", "else",
                                    "begin", "end", "ident", "numero_int", "procedure", "numero_real", "program", "var",
                                    "real", "integer"]
        self.arquivo = open(nome_arquivo_fonte, "r")
        self.linha_atual = 1  # Toma conta de que em que linha estamos no arquivo.
        self.tabela_simbolos = []  # Dicionário para guardar a tabela de simbolos.

    def read_char(self):
        return self.arquivo.read(1)

    def unread_char(self):
        self.arquivo.seek(self.arquivo.tell() - 1, 0)

    def is_char(self, c):
        return 'a' <= c <= 'z' or 'A' <= c <= 'Z'

    def is_number(self, c):
        return '0' <= c <= '9'

    def is_newline(self, c):
        global linha_atual
        if c == '\n':
            self.linha_atual += 1
            return True
        return False

    def reservada_ou_id(self, token):
        c = token
        while self.is_char(c) or self.is_number(c):
            c = self.read_char()
            if c == ' ' or c == '\t':  # Pula espaços.
                continue
            if self.is_char(c) or self.is_number(c):
                token += c
            else:
                if c in self.simbolos_simples:
                    self.unread_char()
                elif c == '':
                    continue
                elif not self.is_newline(c):
                    print("Caracter inválido {} na linha {}".format(repr(c), self.linha_atual))

        if token in self.palavras_reservadas:
            self.tabela_simbolos.append({'Tipo': 'palavra_reservada', "Token": token, "Linha": self.linha_atual})
            print("Palavra reservada: '{}', linha: {}".format(token, self.linha_atual))
        else:
            self.tabela_simbolos.append({'Tipo': 'identificador', "Token": token, "Linha": self.linha_atual})
            print("Identificador: '{}', linha: {}".format(token, self.linha_atual))

    def inteiro_ou_real(self, token):
        c = token
        token = ''
        real = False
        valido = True
        if self.is_number(c):
            while self.is_number(c):
                token += c
                c = self.read_char()
                if c == ' ' or c == '\t':  # Pula espaços.
                    continue
            if c == '.':
                real = True
                token += c
                c = self.read_char()
                if not self.is_number(self, c):  # Erros do formato Numero.
                    real = False
                    valido = False
                    print("O número {} está num formato errado na linha {}".format(token, self.linha_atual))
                else:
                    while self.is_number(c):
                        token += c
                        c = self.read_char()
                        if c == ' ' or c == '\t':  # Pula espaços.
                            continue
            else:
                if not self.is_newline(c):
                    print("Caracter inválido {} na linha {}".format(repr(c), self.linha_atual))
        else:
            self.is_newline(c)

        if real :
            self.tabela_simbolos.append({'Tipo': 'numero_real', "Token": token, "Linha": self.linha_atual})
            print("Numero real: '{}', linha: {}".format(token, self.linha_atual))
        elif valido:
            self.tabela_simbolos.append({'Tipo': 'numero_inteiro', "Token": token, "Linha": self.linha_atual})
            print("Numero inteiro: '{}', linha: {}".format(token, self.linha_atual))

    def comentario1(self, token):
        c = token
        while c != "}":
            c = self.read_char()
            if c == ' ' or c == '\t':  # Pula espaços.
                continue
                self.is_newline(c)  # fixme: Não tenho certeza se é a melhor forma de checar isso.
            token += c
        if "}" in token:
            print("Comentário: '{}', linha: {}".format(token, self.linha_atual))
        else:
            # fixme: Olhar isso no futuro.
            print("Caracter inválido {} na linha {}".format(repr(c), self.linha_atual))
        token = ''

    def comentario2(self, token):
        t = token
        c = self.read_char()
        self.is_newline(c)  # fixme: Não tenho certeza se é a melhor forma de checar isso.
        token += c
        if c == "*":
            flag = False
            while flag == False:
                c = self.read_char()
                if c == ' ' or c == '\t':  # Pula espaços.
                    continue
                    self.is_newline(c)  # fixme: Não tenho certeza se é a melhor forma de checar isso.
                token += c
                if c == "*":
                    c = self.read_char()
                    self.is_newline(c)  # fixme: Não tenho certeza se é a melhor forma de checar isso.
                    if c == "/":
                        token += c
                        print("Comentário: '{}', linha: {}".format(token, self.linha_atual))
                        flag = True

    def simbolos(self, token):
        if token == "<" or token == ">" or token == ":":
            c = self.read_char()
            simb = token + c
            if simb in self.simbolos_duplos:
                token += c
                self.tabela_simbolos.append({'Tipo': 'simbolo_duplo', "Token": token, "Linha": self.linha_atual})
                print("Simbolo duplo: '{}', linha: {}".format(token, self.linha_atual))
            else:
                self.tabela_simbolos.append({'Tipo': 'simbolo_simples', "Token": token, "Linha": self.linha_atual})
                print("Simbolo simples: '{}', linha: {}".format(token, self.linha_atual))
        else:
            self.tabela_simbolos.append({'Tipo': 'simbolo_duplo', "Token": token, "Linha": self.linha_atual})
            print("Simbolo simples: '{}', linha: {}".format(token, self.linha_atual))

    def run(self):
        while True:

            if not self.read_char():
                break
            else:
                self.unread_char()

            token = self.read_char()  # Lê o próximo caracter.

            if not token:
                continue

            if self.is_newline(token):
                continue

            if token == ' ' or token == '\t':
                continue

            if self.is_char(token):  # Identificando se é palavra reservada ou identificador.
                self.reservada_ou_id(token)
            elif self.is_number(token):  # Identifica se é um Numero (inteiro, real)
                self.inteiro_ou_real(token)
            elif token == "{":  # Identifica comentários
                self.comentario1(token)
            elif token == "/" and ((self.read_char() == "*") or self.unread_char()):
                self.unread_char()
                self.comentario2(token)
            elif token in self.simbolos_simples:  # Identifica se é simbolo simples ou duplo
                self.simbolos(token)
            else:
                if token == ".":  # Erros do formato .999 por exemplo
                    c = self.read_char()
                    while self.is_number(c):
                        token += c
                        c = self.read_char()
                    print("O número {} está num formato errado na linha {}".format(repr(token), self.linha_atual))
                else:  # Erros de caracteres inválidos
                    print("Caracter inválido {} na linha {}".format(repr(token), self.linha_atual))
        return self.tabela_simbolos