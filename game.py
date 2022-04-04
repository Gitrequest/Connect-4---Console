game_state = True
board = [[0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0]]

col_list = ["1","2","3","4","5","6","7"]

player1 = 1
player2 = 2

player_count = 1


def check_horizontal(board, player):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == player and board[i][j+1] == player and board[i][j+2] == player and board[i][j+3] == player:
                return True
def check_vertikal(board, player):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == player and board[i+1][j] == player and board[i+2][j] == player and board[i+3][j] == player:
                return True
def check_diagonal(board, player):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == player and board[i+1][j+1] == player and board[i+2][j+2] == player and board[i+3][j+3] == player:
                return True

def check_win(board, player):
    if check_horizontal(board, player) == True or check_vertikal(board, player) == True or check_diagonal(board, player) == True:
        print("Player "  + str(player) + " wins!")
        game_state = False


def print_board(board):
    for i in board:
        print(i)


def check_valid(board, usr_input, col_list, player):
    for index, c in enumerate(board[0]):
        if c == 0 and usr_input == col_list[index]:
            if board[5][index] == 0:
                board[5][index] = player
            elif board[4][index] == 0:
                board[4][index] = player
            elif board[3][index] == 0:
                board[3][index] = player
            elif board[2][index] == 0:
                board[2][index] = player
            elif board[1][index] == 0:
                board[1][index] = player
            elif board[0][index] == 0:
                board[0][index] = player
            return 
        
    print("Invalid selection! Column " + usr_input + " is full!")
    check_valid(board, usr_input, col_list, player)

while game_state:

    if player_count % 2 == 0:
        player = player2
    else:
        player = player1
    player_count +=1 

    usr_input = input("Player " + str(player) + ": Choose a column (1-7): \n")
    check_valid(board, usr_input, col_list, player)
    print_board(board)
    check_win(board, player)
