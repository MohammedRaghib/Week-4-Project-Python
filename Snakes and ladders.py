import random

player_1 = 0
player_2 = 0
turn = True
ladders = [
{
    'pos': 1,
    'plus': 37
},
{
    'pos': 4,
    'plus': 10
},
{
    'pos': 9,
    'plus': 22
},
{
    'pos': 21,
    'plus': 21
},
{
    'pos': 28,
    'plus': 56
},
{
    'pos': 51,
    'plus': 16
},
{
    'pos': 80,
    'plus': 19
},
{
    'pos': 72,
    'plus': 19
}
]

snakes = [
{
    'pos': 17,
    'minus': 10
},
{
    'pos': 54,
    'minus': 20
},
{
    'pos': 62,
    'minus': 43
},
{
    'pos': 64,
    'minus': 4
},
{
    'pos': 87,
    'minus': 51
},
{
    'pos': 93,
    'minus': 20
},
{
    'pos': 95,
    'minus': 20
},
{
    'pos': 98,
    'minus': 19
}
]

def again():
    global turn, player_1, player_2
    player_1 = 0
    player_2 = 0
    play_again = input('Play again? yes or no? ')
    if play_again == 'yes':
        play()
    else:
        print('Bye bye')

def check():
    global turn, player_1, player_2

    for ladder in ladders:
            for snake in snakes:
                if player_1 == ladder['pos']:
                    player_1 += ladder['plus']
                    print(f'Player 1 found a ladder, player 1 is now at position {player_1}')
                    continue
                
                elif player_1 == snake['pos']:
                    player_1 -= snake['minus']
                    print(f'Player 1 found a snake, player 1 is now at position {player_1}')
                    continue

                elif player_2 == ladder['pos']:
                    player_2 += ladder['plus']
                    print(f'Player 2 found a ladder, player 2 is now at position {player_2}')
                    continue

                elif player_2 == snake['pos']:
                    player_2 -= snake['minus']
                    print(f'Player 2 found a ladder, player 2 is now at position {player_2}')
                    continue


def play():
    global turn, player_1, player_2

    player_input = input('Type start to start game: ')

    match player_input:
        case 'start':
            while player_1 < 100 and player_2 < 100:

                dice_roll = random.randint(1,6)

                if turn:
                    if (player_1 + dice_roll) > 100:
                        print('Player 1 Dice roll too high')

                    else:
                        player_1 += dice_roll
                        print(f'Dice roll was {dice_roll}, player 1 is at position {player_1}')
                        turn = not turn

                else:
                    if (player_2 + dice_roll) > 100:
                        print('Player 1 Dice roll too high')

                    else:
                        player_2 += dice_roll
                        print(f'Dice roll was {dice_roll}, player 2 is at position {player_2}')
                        turn = not turn

                check()
                roll = input('Type roll or press enter: ')

            else:
                if player_1 == 100 and player_2 == 100:
                    print('Tie!')
                    again()

                elif player_1 == 100:
                    print('Player 1 won!')
                    again()

                else:
                    print('Player 2 won!')
                    again()

        case _:
            print('Invalid input')
            print(player_input)
play()