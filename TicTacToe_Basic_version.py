#board list
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

#game still going
game_still_going = True

#check winner
winner = None

#whos turn is it
current_player = "X"


#display board function
def display_board():
  print(board[0] + " | " + board[1] + " | " + board[2])
  print(board[3] + " | " + board[4] + " | " + board[5])
  print(board[6] + " | " + board[7] + " | " + board[8])


#main def in which all game will be played
def play_game():
  #calling board to display
  display_board()

  #will continuously run until win lose or tie
  while game_still_going:

    #handle a singlr turn of a player
    handle_turn(current_player)

    #checking if game over or not
    check_if_game_over()

    #change turn of a player
    flip_player()

  #the gme has ended
  if winner == "X" or winner == "O":
    print("Winner is " + winner)
  elif winner == None:
    print("Tie.")


#handle a single turn of a player
def handle_turn(player):

  print(player + "'s turn'")
  position = input("Choose a number from 1-9: ")

  valid = False
  while not valid:

    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
      position = input("Invalid Input. Choose a number from 1-9: ")

    position = int(position) - 1

    if board[position] == "-":
      valid = True
    else:
      print("You can't go there. Go again.")

  board[position] = player
  display_board()


#checking if game is over
def check_if_game_over():
  check_for_winner()
  check_if_tie()


def check_for_winner():
  #set up the global variables
  global winner

  #check rows
  row_winner = check_rows()
  #check colums
  column_winner = check_columns()
  #check diagonals
  diagonal_winner = check_diagonals()

  #check for the winner
  if row_winner:
    winner = row_winner
  elif column_winner:
    winner = column_winner
  elif diagonal_winner:
    winner = diagonal_winner
  else:
    winner = None
  return


def check_rows():
  #set up global variable
  global game_still_going
  row_1 = board[0] == board[1] == board[2] != "-"
  row_2 = board[3] == board[4] == board[5] != "-"
  row_3 = board[6] == board[7] == board[8] != "-"

  #if any row does match, flag that there is a win
  if row_1 or row_2 or row_3:
    game_still_going = False
  #returns the winner x or o
  if row_1:
    return board[0]
  elif row_2:
    return board[3]
  elif row_3:
    return board[6]
  return


def check_columns():
  #set up global variable
  global game_still_going
  column_1 = board[0] == board[3] == board[6] != "-"
  column_2 = board[1] == board[4] == board[7] != "-"
  column_3 = board[2] == board[5] == board[8] != "-"

  #if any column does match, flag that there is a win
  if column_1 or column_2 or column_3:
    game_still_going = False
  #returns the winner x or o
  if column_1:
    return board[0]
  elif column_2:
    return board[1]
  elif column_3:
    return board[2]
  return


def check_diagonals():
  #set up global variable
  global game_still_going

  diagonal_1 = board[0] == board[4] == board[8] != "-"
  diagonal_2 = board[2] == board[4] == board[6] != "-"

    #if any diagonal does match, flag that there is a win
  if diagonal_1 or diagonal_2:
    game_still_going = False
  #returns the winner x or o
  if diagonal_1:
    return board[0]
  elif diagonal_2:
    return board[2]
  return


#check if game is tied
def check_if_tie():
  #set up global variable
  global game_still_going

  #check if there is any empty "_" if not game tied
  if "-" not in board:
    game_still_going = False
  return


#flipping the turn of the player
def flip_player():
  #setting global variable
  global current_player
  #changes turns if x plays then next turn should be of o
  if current_player == "X":
    current_player = "O"
  elif current_player == "O":
    current_player = "X"
  return


play_game()

#board
#display-board
#play game
#handle turn
#check win
  #check rows
  #check colums
  #check diagonals
#check tie
