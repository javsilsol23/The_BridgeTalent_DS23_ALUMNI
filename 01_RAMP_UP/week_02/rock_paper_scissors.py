from random import choice


elementos = {
    '1': 'Piedra',
    '2': 'Papel',
    '3': 'Tijera'
}


def human_play():
    while 1:
        print()
        print('Humano, elige jugada')
        print('1.) Piedra')
        print('2.) Papel')
        print('3.) Tijera')
        jugada = input('...')

        if jugada in ['1', '2', '3']:
            print()
            return elementos[jugada]
        else:
            print()
            print(f'El valor {jugada} es incorrecto')


def computer_play():
    return elementos[choice(['1', '2', '3'])]


def eval_plays(humano, computer, human_score, computer_score):
    print(f'Humano: {humano}, Computer: {computer}')

    if humano == 'Piedra':
        if computer == 'Papel':
            print('Gana computer')
            computer_score += 1
        elif computer == 'Tijeras':
            print('Gana humano')
            human_score += 1
        else:
            print('Empate')

    elif humano == 'Papel':
        if computer == 'Tijeras':
            print('Gana computer')
            computer_score += 1
        elif computer == 'Piedra':
            print('Gana humano')
            human_score += 1
        else:
            print('Empate')

    else:
        if computer == 'Piedra':
            print('Gana computer')
            computer_score += 1
        elif computer == 'Papel':
            print('Gana humano')
            human_score += 1
        else:
            print('Empate')

    return human_score, computer_score


######################################################################
#           MAIN        MAIN        MAIN        MAIN
######################################################################

print()
print('------------------------------------------------')
print('Vamos a jugar Piedra, Papel o Tijeras')
print('------------------------------------------------')
print()

num_jugadas = int(input('Número de jugadas...'))
human_score = 0
computer_score = 0

for i in range(num_jugadas):
    humano = human_play()
    computer = computer_play()
    human_score, computer_score = eval_plays(
        humano, computer, human_score, computer_score)


print()
print('------------------------------------------------')
print()
print(f'Resultado final: Humano {human_score} - Computer {computer_score}')
print()
print()