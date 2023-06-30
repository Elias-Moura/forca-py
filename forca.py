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
        chute = input('Digite uma letra: ').lower().strip()[0]

        index = 0
        letras_acertadas = list()
        letras_erradas = list()
        for letra in palavra_secreta:
            if chute == letra:
                print(f'Encontrei a letra {letra} na posição {index}')
            else:
                print(f'A letra {chute} não está contida na palavra secreta.')
            index += 1


if __name__ == '__main__':
    jogar()
