def display_game(the_game):
  print("|".join(the_game[0]))
  print("-+-+-")
  print("|".join(the_game[1]))
  print("-+-+-")
  print("|".join(the_game[2]))

def read_board():
  #read board from file here assume three rows of three characters (space is ok)
  #replace this line with the file contents
  return [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

the_game = read_board()
display_game(the_game)

def write_board(the_game):
  #write board to file here
  #write three rows of three characters
  print("wrote board")

#This is some logic if you want to take this game all the way
#returns 0 when game tied, winning value when winner or 1 when game incomplete
def evaluate_game_state(the_game, neutral_square_value):
  winning_lines = [
    [[0,0], [0,1], [0,2]], 
    [[1,0], [1,1], [1,2]], 
    [[2,0], [2,1], [2,2]],
    [[0,0], [1,0], [2,0]], 
    [[0,1], [1,1], [2,1]], 
    [[0,2], [1,2], [2,2]], 
    [[0,0], [1,1], [2,2]], 
    [[0,2], [1,1], [2,0]]
  ]
  isFull = True
  for line in winning_lines:
    line_value = 0
    winner = 1
    count = 0
    for space in line:
      space_value = the_game[space[0]][space[1]]
      if space_value == 0:
        isFull = False
        break
      count += 1
      if line_value == neutral_square_value:
        line_value = space_value
      else:
        if line_value != space_value:
          winner = 0
      if count == 3:
        if winner == 1:
          return line_value
  if isFull:
    return 0
  return 1