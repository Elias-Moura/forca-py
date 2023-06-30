from random import choice


def printa_bem_vindo():
    tamanho_print = 30
    print('*' * tamanho_print)
    print('Bem vindo ao jogo da forca.'.center(tamanho_print))
    print('*' * tamanho_print)


def escolhe_palavra_secreta():
    lista_de_palavras_secretas = ['abacaxi', 'banana', 'morango']
    return choice(lista_de_palavras_secretas)


def jogar():
    printa_bem_vindo()
    palavra_secreta = escolhe_palavra_secreta()
    print(palavra_secreta)

    enforcou, acertou = False, False

    while not enforcou and not acertou:
        print('inicio')

if __name__ == '__main__':
    jogar()
