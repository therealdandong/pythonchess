
@params : None
@return list:ans_list ,2 dimensional list of the chessboard. which contain all the chess pieces.
draw the chessboard 
"""

def draw():
	chess_list_1 = ['K','Q','R','N','B','P','-']
	chess_list_2 = ['k','q','r','n','b','p']
	ans_list = []
	# dont exit until there are at least 8 list inside the ans_list
	while len(ans_list) <8:
		flag = True
		row = input("enter your line {}.".format(len(ans_list)+1))
		#if the length of user input is less than 8 dont append the row
		if len(row) != 8:
			print("please enter 8 character")
			flag = False
		# loop throught each character and if one of the character is not one of the character in the chess_list then dont append the row
		for num in range(len(row)):
			if row[num] not in chess_list_1 and row[num] not in chess_list_2:
				print("please dont enter invalid character")
				flag = False
				break
		# if there were no error happening above then we can append the row
		if flag:
			ans_list.append([row])
	return ans_list
"""
@params : [chessboard] (2d list) as a old chessboard
@return : [chessboard] (2d list) as a new chessboard

asking user for x and y value of the piece that needed to be move, then withdraw that row from the chessboard and pop that specify element base on x value and store it using a temp_element insert a '-' into the x value position.
asking user for x and y value of the location that pieces need to be placed, then withdraw that row from the chessboard and pop that specify element base on the x value and insert temp_element into the x value position.
then return the chessboard
"""

def move(chessboard):
	chess_list_1 = ['K','Q','R','N','B','P']
	chess_list_2 = ['k','q','r','n','b','p']
	# user is expected to enter value between 1 and 8 otherwise needed to ask again.
	while True:
		player_y = int(input("enter y value"))-1
		player_x = int(input("enter x value"))-1
		final_y = int(input("enter y final value"))-1
		final_x = int(input("enter x final value"))-1
		if 0 <= player_x <=7 and 0 <= player_y <= 7 and 0 <= final_y <=7 and 0 <= final_x <= 7:
			break
		else:
			print("you have enter a invalid number, please try again.")
	# change the string to list and copy that over to change_list
	change_list_remove = list_(chessboard[player_y][0])
	# using pop function to remove element and store it as temp element
	temp_piece = change_list_remove.pop(player_x)
	# insert '-' element in the list and store that change_list into chessboard.
	change_list_remove.insert(player_x,'-')
	chessboard[player_y].pop()
	chessboard[player_y].append(combine(change_list_remove))
	# change the string to list and copy that over to change_list
	change_list_add = list_(chessboard[final_y][0])
	# using pop function to remove element in final_x position
	change_list_add.pop(final_x)
	# using insert element in final_X position
	change_list_add.insert(final_x,temp_piece)
	# insert temp_piece element in the add_list and store that change_list into chessboard.
	chessboard[final_y].pop()
	chessboard[final_y].append(combine(change_list_add))
	

	return chessboard
"""
@param string: called arg
@return a list of character that compose the original string.
"""

def list_(arg):
	ans = []
	for num in range(len(arg)):
		ans.append(arg[num])
	return ans
"""
@param list: a list of element called list_
@return a string: that append all the element together.
"""
def combine(list_):
	ans = ""
	for num in range(len(list_)):
		ans += str(list_[num])
	return ans

"""
@param  a 2d list: chessboard
@return None
draw the chessboard to terminal,black and white score and who is winning.
"""

def display(chessboard):
	
	for x in range(len(chessboard)):
		output = ""
		for y in range(len(chessboard[x][0])):
			output += str(chessboard[x][0][y]) + " \t"
		print(output)
	white_player_score,black_player_score = calculate_score(chessboard)
	print("white player score : {}, black player score : {}".format(white_player_score,black_player_score))
	# display who is winning
	display_win(white_player_score,black_player_score)

"""
@param integer:white score, 	 integer:black score.
@return none
print who ever is bigger.


"""


def display_win(white,black):
	if black > white:
		print("black is winning")
	elif white > black:
		print("white is winning")
	else:
		print("they have the same score")
"""
@param None
@return None


display instruction 
"""

def display_instruction():
	print("at the beginning of the game you need to enter a series of string as the row of the chessboard. you must enter exactly 8 character. and only contain King as K,Queen as Q,Rook as R,Knight as n ,Bishop as B, Pawn as P, Empty as -, after you draw the board you will see a score for black and white. black is represent by upper case letter, white is represent by lower case letter. after that you can either quit the game, draw a new chessboard or move a pieces. in order to move a piece you need to provide a y and x value of current pieces(range from 1 to 8), and provide a final position for the piece. after that the program will ask you the samething until you choose to quit the program.")

"""
@param 2d list: chessboard
@return integer:black_score,	integer:white_score 
calculate the score base on the chessboard provided and return black_score and white_score 
"""


def calculate_score(list_):

	chess_list_upper = ['K','Q','R','N','B','P']
	chess_list_lower = ['k','q','r','n','b','p']
	value_list = [0,10,5,3.5,3,1]
	black_score = 0
	white_score = 0
	# using nested for loop to loop through all element in the chessboard, if there is element in chess_list_upper black_score plus one, if there is element in chess_list_lower then white_score plus one.
	for r_num in range(len(list_)):
		for c_num in range(len(list_[r_num][0])):
			if list_[r_num][0][c_num] in chess_list_upper:
				for index in range(len(chess_list_upper)):
					if chess_list_upper[index] == list_[r_num][0][c_num]:
						black_score += value_list[index]
			elif list_[r_num][0][c_num] in chess_list_lower:
				for index in range(len(chess_list_lower)):
					if chess_list_lower[index] == list_[r_num][0][c_num]:
						white_score += value_list[index]
				 
	return black_score, white_score
""""
@param None
@return None

"""
def main():
	# first display instruction and using pre define function to draw the chessboard.
	display_instruction()
	chess_board = draw()
	display(chess_board)
	
	# unless user select to quit otherwise we will remain in the while loop
	while True:
		decision = int(input("\t please enter one of the following: \n \t1.quit the program\n \t 2. draw a new chess board\n \t3. move a piece"))
		# quit the program if user select 1
		if decision == 1:
			break
		# if user select 2 draw a chessboard from scratch 
		elif decision  == 2:
			#draw the chessboard
			chess_board = draw()
			# display chessboard,score and who is winning
			display(chess_board)
		# move a piece if user select 3
		elif decision == 3:
			# using pre define move function to move a chess board
			move(chess_board)
			# display chessboard,score and who is winning
			display(chess_board)
		else:
			print("please dont enter anything other than 1,2,3")
			


main()
