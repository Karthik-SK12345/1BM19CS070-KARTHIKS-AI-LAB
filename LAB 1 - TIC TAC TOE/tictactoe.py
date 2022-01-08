import random
board = [' ' for i in range(9)]


def genBoard():
    print("\n")
    print(20 * "*")
    print("\n")
    print("    |   |")
    print("  " + board[0] + " | " + board[1] + " | " + board[2])
    print("    |   |")
    print("-------------")
    print("    |   |")
    print("  " + board[3] + " | " + board[4] + " | " + board[5])
    print("    |   |")
    print("-------------")
    print("    |   |")
    print("  " + board[6] + " | " + board[7] + " | " + board[8])
    print("    |   |")


def playMove(board):
    move = int(input("Enter a position between 1 to 9:"))
    if move not in range(1, 10):
        print("Move outside permitted range!!")
        playMove(board)
    if not isOccupied(board, move - 1):
        board[move - 1] = 'X'
    else:
        print("Sorry the given cell is occupied")
        playMove(board)
    return


def selectRandom(optimum):
    ln = len(optimum)
    r = random.randrange(0, ln)  # generating a random index
    return optimum[r]


def compMove(board):
    # move = random.randint(1, 9)  # inclusive of limit 1 and 9
    # if not isOccupied(board, move - 1):
    #     board[move - 1] = 'O'
    # else:
    #     compMove(board)
    # return
    # checking all possible moves
    possibleMoves = [index for index,
                     trial in enumerate(board) if trial == ' ']
    move = 0
    # checking for chance of winning in current move
    for alpha in ['O', 'X']:  # cuz if x is able to win in next that should be our next movc
        for i in possibleMoves:
            # creating a copy of the board
            board_copy = board[:]
            board_copy[i] = alpha
            if checkForWinner(board_copy, alpha):
                move = i
                return move

    # checking for chance of winning in next moves
    # check corners first
    cornersOpen = []
    for i in possibleMoves:
        if i in [0, 2, 6, 8]:
            cornersOpen.append(i)
    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move
    # next centre
    for i in possibleMoves:
        if i == 5:
            move = i

            return move

      # else edges
    edgesOpen = []
    for i in possibleMoves:
        if i in [1, 3, 5, 7]:
            edgesOpen.append(i)
    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)

        return move

    return move


def checkForWinner(board, alpha):
    if(
        # rows
      (board[0] == alpha and board[1] == alpha and board[2] == alpha) or
      (board[3] == alpha and board[4] == alpha and board[5] == alpha) or
      (board[6] == alpha and board[7] == alpha and board[8] == alpha) or
        # cols
      (board[0] == alpha and board[3] == alpha and board[6] == alpha) or
      (board[1] == alpha and board[4] == alpha and board[7] == alpha) or
      (board[2] == alpha and board[5] == alpha and board[8] == alpha) or
        # diagonals
      (board[0] == alpha and board[4] == alpha and board[8] == alpha) or
      (board[2] == alpha and board[4] == alpha and board[6] == alpha)):
        return True
    else:
        return False


def isOccupied(board, move):
    if board[move] == ' ':
        return False
    else:
        return True


def isFull(board):
    if ' ' not in board:
        return True
    else:
        return False


def main():

    print("Welcome to TIC TAC TOE!\n")
    print("Opponent is O and you are X:\n")
    while not isFull(board):
        genBoard()
        if not checkForWinner(board, 'O'):
            playMove(board)

            genBoard()
        else:
            print("Player O won!")
            quit()
        if not checkForWinner(board, 'X'):

            move = compMove(board)
            if move == None:
                break
            else:
                board[move] = 'O'
            if(isFull(board)):
                break
            genBoard()
        else:
            print("Player X won!")
            quit()

    if (isFull(board)):
        print("The game is a Tie")


main()
