import numpy as np
import random
# random.seed(1)
def create_board():
    return np.zeros((3, 3), dtype=int)

def place(board, player, position):
    if board[position[0],position[1]] == 0:
        board[position[0], position[1]] = player
    else:
        print("Field already taken")

def possibilities(board):
    indexes = np.where(board ==0)
    x = indexes[0] #numpy.ndarray
    y = indexes[1] #numpy.ndarray
    # print(x)
    # print(y)
    list = []
    i = 0
    while i < len(x):
            # print(x[i],y[i])
            free_cords = (x[i],y[i])
            list.append(free_cords)
            i +=1
    return list

def random_place(board, player):
    selection = possibilities(board)
    random_position = random.choice(selection)
    place(board, player, random_position)

def row_win(board, player):
    i = 0
    # print(board.shape[0])
    check_table = np.zeros((board.shape[0], board.shape[1]))
    while i < (board.shape[0]):
        # print("i:",i)
        counter = player
        j = 0
        while j < (board.shape[1]):
            if board[i,j] == player:
                # print("ROW value: ",board[i,j])
                check_table[i,j] = True
                counter = counter * counter
                # print("counter:",counter)
            else:
                # print("Zonk!")
                check_table[i, j] = False
            j = j + 1
        i = i + 1
    result = True
    for k in range(board.shape[0]):
        if check_table[k] = False:
            result = False
        else:
            print("No no")
    return result

random.seed(1)
board = create_board()
random_place(board, 1)
random_place(board, 2)
random_place(board, 1)
random_place(board, 2)
random_place(board, 1)
random_place(board, 2)
print(board)
print(row_win(board,1))