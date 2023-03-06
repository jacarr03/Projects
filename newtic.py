test_board = ['#','X','O','X','O','X','O','X','O','X']




def display_board(board):
    print('\n'*100)

    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

display_board(test_board)

#output = (player 1 marker, player 2 marker)
def player_input():
    marker = ''
    while not (marker =='X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()
        if marker == 'X':
            return ('X','O')
        else:
            return ('O','X')
#player1_marker , player2_marker = player_input()


def place_marker(board,marker,position):
    board[position] = marker



def win_check(board,mark):

    return ((board[1] == mark and board[2] ==mark and board[3]) or
    (board[4]== mark and board[5]== mark and board[6]==mark)or
    (board[7] == mark and board[8] == mark and board[9] == mark) or
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal






import random 

def choose_first():
    flip = random.randint(0,1)
    if flip == 0:
        return 'Player1'
    else:
        return 'Player2'

def space_check(board,position):
    return board[position] == ' '


        
def full_board_check(board):
    for i in range(0,10):
        if space_check(board,i):
            return False

    return True

def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input('Choose a spot (1-9):'))
        return position

def replay():
    
    choice = input('play again? enter Yes or No')
    return choice =='Yes'




#while loop to run the game
#break out of the while loop on replay function

print('Welcome to tic tac toe')

while True:
    #play the game
    the_board = [' ']*10
    player1_marker,player2_marker = player_input()

    turn = choose_first()
    print(turn + 'will go first')

    play_game = input('Ready to play? y or n: ')

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False
    

    while game_on:
        if turn == 'Player 1':
            display_board(the_board)
            #choose a postion
            position = player_choice(the_board)
            #place marker on position
            place_marker(the_board,player1_marker,position)
            # check if they won or tie
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('player 1 won')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('tie game')
                    break
                else:
                    turn  = 'Player 2'

            #no tie or win? next player turn


        else:
                display_board(the_board)
                #choose a postion
                position = player_choice(the_board)
                #place marker on position
                place_marker(the_board,player2_marker,position)
                # check if they won or tie
                if win_check(the_board,player2_marker):
                    display_board(the_board)
                    print('player 2 won')
                    game_on = False
                else:
                    if full_board_check(the_board):
                        display_board(the_board)
                        print('tie game')
                        break
                    else:
                        turn  = 'Player 1'
                    
            #no tie or win? next player turn









    if not replay():
        break

