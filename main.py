import lexico


def main():
    tabela_de_simbolos = lexico.Lexer("teste.txt").run()
    print(tabela_de_simbolos)

if __name__ == '__main__':
    main()
