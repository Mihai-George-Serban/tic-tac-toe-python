game_still_going = True
winner = None
current_player = "X"
board = [[".", ".", "."],
         [".", ".", "."],
         [".", ".", "."]]

print('''
    -----------------------------------------
             Welcome to Tik Tak Toe!
    -----------------------------------------
    ''')
name1 = input("Please enter the name for the first player:")
print(name1 + " will play with X")
name2 = input("Please enter the name for the second player:")
print(name2 + " will play with O")

def print_result(winner):
    if winner == "X":
        print("Congratulations!" + "\n" + name1 + " won the game!")
    elif  winner == "O":
        print("Congratulations!"+ "\n"+ name2 + " won the game!")
    elif winner == None:
        print("The game is over - Draw! ")
    return winner
def tictactoe_game():

    print_board()
    while game_still_going:
        get_move(current_player)
        has_won()
        mark()
    print_result(winner)

def init_board():
    """Returns an empty 3-by-3 board (with .)."""
    board = [[".", ".", "."],
             [".", ".", "."],
             [".", ".", "."]]
    return board


def get_move(player):    #handle_turn(player):
    """Returns the coordinates of a valid move for player on board."""
    myDict = {
        "A1": [0, 0],
        "A2": [0, 1],
        "A3": [0, 2],
        "B1": [1, 0],
        "B2": [1, 1],
        "B3": [1, 2],
        "C1": [2, 0],
        "C2": [2, 1],
        "C3": [2, 2]
    }
    print(player + "'s turn.")
    position = input("Choose a position for your move: ")

    # Whatever the user inputs, make sure it is a valid input, and the spot is open
    valid = False
    while not valid:

        # Make sure the input is valid
        while position not in ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]:
            position = input("Choose a position for your move: ").upper()
            return position
        row, col = myDict[position][0], myDict[position][1]

        # Get correct index in our board list

        # Then also make sure the spot is available on the board
        if board[row][col] == ".":
            valid = True
        else:
            print("You can't go there. Go again.")

    # Put the game piece on the board
    board[row][col] = current_player
    print_board()

def get_ai_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    row, col = 0, 0
    return row, col


def mark():   # flip_player():
    # Global variables we need
    global current_player
    # If the current player was X, make it O
    if current_player == "X":
        current_player = "O"
    # Or if the current player was O, make it X
    elif current_player == "O":
        current_player = "X"


def has_won():
    check_for_winner()
    is_full(board)


def check_for_winner():
    # Set global variables
    global winner
    # Check if there was a winner anywhere
    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()
    # Get the winner
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
def check_rows():
    # Set global variables
    global game_still_going
    # Check if any of the rows have all the same value (and is not empty)
    row_1 = board[0][0] == board[0][1] == board[0][2] != "."
    row_2 = board[1][0] == board[1][1] == board[1][2] != "."
    row_3 = board[2][0] == board[2][1] == board[2][2] != "."
    # If any row does have a match, flag that there is a win
    if row_1 or row_2 or row_3:
        game_still_going = False
    # Return the winner
    if row_1:
        return board[0][0]
    elif row_2:
        return board[1][0]
    elif row_3:
        return board[2][0]
        # Or return None if there was no winner
    else:
        return None


# Check the columns for a win
def check_columns():
    # Set global variables
    global game_still_going
    # Check if any of the columns have all the same value (and is not empty)
    column_1 = board[0][0] == board[1][0] == board[2][0] != "."
    column_2 = board[0][1] == board[1][1] == board[2][1] != "."
    column_3 = board[0][2] == board[1][2] == board[2][2] != "."
    # If any row does have a match, flag that there is a win
    if column_1 or column_2 or column_3:
        game_still_going = False
    # Return the winner
    if column_1:
        return board[0][0]
    elif column_2:
        return board[0][1]
    elif column_3:
        return board[0][2]
        # Or return None if there was no winner
    else:
        return None


# Check the diagonals for a win
def check_diagonals():
    # Set global variables
    global game_still_going
    # Check if any of the columns have all the same value (and is not empty)
    diagonal_1 = board[0][0] == board[1][1] == board[2][2] != "."
    diagonal_2 = board[0][2] == board[1][1] == board[2][0] != "."
    # If any row does have a match, flag that there is a win
    if diagonal_1 or diagonal_2:
        game_still_going = False
    # Return the winner
    if diagonal_1:
        return board[0][0]
    elif diagonal_2:
        return board[0][2]
    # Or return None if there was no winner
    else:
        return None



def is_full(board): #check_for_tie()
    # Set global variables
    global game_still_going
    # If board is full
    if "." not in board[0] and "." not in board[1] and "." not in board[2]:
        game_still_going = False
        return True
    # Else there is no tie
    else:
        return False

def print_board():        #def display_board():
    c_1 = "1"
    c_2 = "2"
    c_3 = "3"
    r_1 = "A"
    r_2 = "B"
    r_3 = "C"
    print(3 * " " + c_1 + "   " + c_2 + "   " + c_3)
    print(r_1 + "  " + " | ".join(board[0][:3]))
    print(2 * " " + 3 * "-" + "+" + 3 * "-" + "+" + 3 * "-")
    print(r_2 + "  " + " | ".join(board[1][:3]))
    print(2 * " " + 3 * "-" + "+" + 3 * "-" + "+" + 3 * "-")
    print(r_3 + "  " + " | ".join(board[2][:3]))
    print("")

tictactoe_game()


