def anti_cheat():
    print('* * * NO CHEATING * * * \n \n' * 10)
    # for i in range(1, 10):
    #     print('* * * NO CHEATING * * * ')
    #     print('* * * * * * * * * * * * ')


player_1_pick = input('Player 1 pick your choice').lower()

anti_cheat()

player_2_pick = input('Player 2 pick your choice').lower()

print('BATTLE')
if player_1_pick == player_2_pick:
    print('Draw!')
elif player_2_pick != 'rock' and player_2_pick != 'paper' and player_2_pick != 'scissors':
    print('Player 2: Something went wrong, try again...')
elif player_1_pick == 'rock':
    if player_2_pick == 'scissors':
        print('Player 1 wins!')
    elif player_2_pick == 'paper':
        print('Player 2 wins!')
elif player_1_pick == 'scissors':
    if player_2_pick == 'rock':
        print('Player 2 wins!')
    elif player_2_pick == 'paper':
        print('Player 1 wins!')
elif player_1_pick == 'paper':
    if player_2_pick == 'rock':
        print('Player 1 wins!')
    elif player_2_pick == 'scissors':
        print('Player 2 wins!')
else:
    print('Player 1: Something went wrong, try again...')
