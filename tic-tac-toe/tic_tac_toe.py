import os
import time

board = ['', '', '', '', '', '', '', '', '', '']
player = 1

## Win Flags ##
Win = 1
Draw = -1
Running = 0
stop = 1

##########
Game = Running
Mark = 'X'


# This function draws game board
def DrawBoard():
    print("  %s   |   %s   |   %s" % (board[1], board[2], board[3]))
    print("______|_______|______")
    print("  %s   |   %s   |   %s" % (board[4], board[5], board[6]))
    print("______|_______|______")
    print("  %s   |   %s   |   %s" % (board[7], board[8], board[9]))
    print()


# This function checks position is empty or not
def checkPosition(x):
    if board[x] == '':
        return True
    else:
        return False


# This function checks player has won or not
def CheckWin():
    global Game

    # Horizontal winning condition
    if board[1] == board[2] and board[2] == board[3] and board[1] != '':
        Game = Win

    elif board[4] == board[5] and board[5] == board[6] and board[4] != '':
        Game = Win

    elif board[7] == board[8] and board[8] == board[9] and board[7] != '':
        Game = Win

    # Vertical winning condition
    elif board[1] == board[4] and board[4] == board[7] and board[1] != '':
        Game = Win

    elif board[2] == board[5] and board[5] == board[8] and board[2] != '':
        Game = Win

    elif board[3] == board[6] and board[6] == board[9] and board[3] != '':
        Game = Win

    # Diagonal winning condition
    elif board[1] == board[5] and board[5] == board[9] and board[5] != '':
        Game = Win

    elif board[3] == board[5] and board[5] == board[7] and board[5] != '':
        Game = Win

    # Match Tie or Draw condition
    elif (
        board[1] != '' and
        board[2] != '' and
        board[3] != '' and
        board[4] != '' and
        board[5] != '' and
        board[6] != '' and
        board[7] != '' and
        board[8] != '' and
        board[9] != ''
    ):
        Game = Draw

    else:
        Game = Running


# ---------------------------------------------------------
# MINIMAX AI FUNCTIONS
# ---------------------------------------------------------

# Check if AI has won
def checkAIWin():
    winning_positions = [
        (1, 2, 3),
        (4, 5, 6),
        (7, 8, 9),
        (1, 4, 7),
        (2, 5, 8),
        (3, 6, 9),
        (1, 5, 9),
        (3, 5, 7)
    ]

    for a, b, c in winning_positions:
        if board[a] == board[b] == board[c] == 'O':
            return True

    return False


# Check if player has won
def checkPlayerWin():
    winning_positions = [
        (1, 2, 3),
        (4, 5, 6),
        (7, 8, 9),
        (1, 4, 7),
        (2, 5, 8),
        (3, 6, 9),
        (1, 5, 9),
        (3, 5, 7)
    ]

    for a, b, c in winning_positions:
        if board[a] == board[b] == board[c] == 'X':
            return True

    return False


# Check if board is full
def isBoardFull():
    for i in range(1, 10):
        if board[i] == '':
            return False

    return True


# Minimax Algorithm
def Minimax(depth, isMaximizing):

    # AI wins
    if checkAIWin():
        return 10 - depth

    # Player wins
    if checkPlayerWin():
        return depth - 10

    # Draw
    if isBoardFull():
        return 0

    # AI's turn - maximize score
    if isMaximizing:

        bestScore = -1000

        for i in range(1, 10):

            if board[i] == '':
                board[i] = 'O'

                score = Minimax(depth + 1, False)

                board[i] = ''

                if score > bestScore:
                    bestScore = score

        return bestScore

    # Player's turn - minimize score
    else:

        bestScore = 1000

        for i in range(1, 10):

            if board[i] == '':
                board[i] = 'X'

                score = Minimax(depth + 1, True)

                board[i] = ''

                if score < bestScore:
                    bestScore = score

        return bestScore


# Find the best move for AI
def FindBestMove():

    bestScore = -1000
    bestMove = -1

    for i in range(1, 10):

        if board[i] == '':

            board[i] = 'O'

            score = Minimax(0, False)

            board[i] = ''

            if score > bestScore:
                bestScore = score
                bestMove = i

    return bestMove


# ---------------------------------------------------------
# MAIN GAME
# ---------------------------------------------------------

print("====================================")
print("        TIC-TAC-TOE AI GAME")
print("====================================")
print()
print("Player [X] ---- AI [O]")
print()
print("The AI uses the Minimax Algorithm.")
print("You cannot defeat the AI if it plays optimally.")
print()
print("Please wait........")
time.sleep(1)


while Game == Running:

    os.system('cls')

    DrawBoard()

    # Player's turn
    if player % 2 != 0:

        print("Player's chance")
        Mark = 'X'

        while True:

            try:
                choice = int(
                    input(
                        "Enter the position between [1-9] "
                        "where you want to mark: "
                    )
                )

                if choice < 1 or choice > 9:
                    print("Please enter a number between 1 and 9.")
                    continue

                if checkPosition(choice):
                    board[choice] = Mark
                    player += 1
                    CheckWin()
                    break

                else:
                    print("That position is already occupied.")

            except ValueError:
                print("Please enter a valid number.")

    # AI's turn
    else:

        print("AI is thinking...")
        time.sleep(1)

        Mark = 'O'

        choice = FindBestMove()

        board[choice] = Mark

        player += 1

        CheckWin()


# ---------------------------------------------------------
# GAME RESULT
# ---------------------------------------------------------

os.system('cls')

DrawBoard()

print()

if Game == Draw:

    print("====================================")
    print("           GAME DRAW")
    print("====================================")

elif Game == Win:

    player -= 1

    if player % 2 != 0:

        print("====================================")
        print("          PLAYER 1 WON!")
        print("====================================")

    else:

        print("====================================")
        print("            AI WON!")
        print("====================================")

print()
print("Thank you for playing!")