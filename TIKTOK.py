def play_1():
    p = player_choice()
    (v1,v2) = p
    position1 =''
    while position1 not in range(1,9):
        position1 = input(f'Enter the area where Player 1 need to put the {v1} :')
        if position1.isdigit() ==False or position1== '0' :
            print('Please enter a valid Digit !')
        else:
            break
    return int(position1)
def play_2():
    p = player_choice()
    (v1,v2) = p
    position2 =''
    while position2 not in range(1,9):
        position2 = input(f'Enter the area where Player 2 need to put the {v2} :')
        if position2.isdigit() ==False or position2== '0' :
            print('Please enter a valid Digit !')
        else:
            break
    return int(position2)
def player_choice():   
    player_1 = 'X'
    player_2 = 'O'    
    value_1 = player_1
    value_2 = player_2
    return (value_1,value_2) 
def default_board(place):
    board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    print(place[7]+' | '+place[8] +' | '+place[9])
    print(place[4]+' | '+place[5] +' | '+place[6])
    print(place[1]+' | '+place[2] +' | '+place[3])
def game1():
    board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    default_board(board)
    life = True
    life_2 = ''
    while life:
        life_3 =True
        p1 = play_1()
        board[p1] = 'X'
        default_board(board)
        if board[1]==board[2]==board[3]== 'X' or  board[4]==board[5]==board[6]== 'X' or  board[7]==board[8]==board[9]== 'X' or board[1]==board[4]==board[7]== 'X' or board[2]==board[5]==board[8]== 'X' or board[3]==board[6]==board[9]== 'X' or board[1]==board[5]==board[9]== 'X' or board[3]==board[5]==board[7]== 'X': 
            print('Congrats!, Player 1 Wins the game')
            life = False
            print('Game Over!')
            break
        elif (board[1]=='X'or board[1]=='O') and (board[2]=='X'or board[2]=='O') and (board[3]=='X'or board[3]=='O') and (board[4]=='X'or board[4]=='O')and (board[5]=='X'or board[5]=='O') and (board[6]=='X'or board[6]=='O') and (board[7]=='X'or board[7]=='O') and (board[8]=='X'or board[8]=='O')and (board[9]=='X'or board[9]=='O'):
            print('The Match is draw !!')
            choice =''
            while choice != ('yes' or 'Yes') and choice!= ('No' or 'no'):
                choice = input("\ndo you wanna start the play ? : Yes or No ")
                if choice not in ('yes','Yes','No','no'):
                    print('Please enter a valid input !')
                elif choice in ('No','no'):
                    print('Thank You!, Play again if you want :)')
                    life_2 = 'done'
                    life = False
                    break
                else:
                    life = True
                    life_3 = False
                    board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']            
        if life_2 =='' and life_3 == True:            
            p2 = play_2()
            board[p2] = 'O'
            default_board(board)
            if board[1]==board[2]==board[3]== 'O' or board[4]==board[5]==board[6]== 'O' or board[7]==board[8]==board[9]== 'O' or board[1]==board[4]==board[7]== 'O' or board[2]==board[5]==board[8]== 'O' or board[3]==board[6]==board[9]== 'O' or board[1]==board[5]==board[9]== 'O' or board[3]==board[5]==board[7]== 'O':
                print('Congrats!, Player 2 Wins the game')
                life = False
                print('Game Over!')   
game1()