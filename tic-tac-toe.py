import sys
import random


def check():
	global loop
	global board
	global is_x
	global scores

	win = wincheck(board)
	if win == False:
		return
	winner = 'X' if is_x else 'O'
	scores[winner] += 1
	print('*** ' + winner + ' WINS','***')
	print("Scoreboard",'X :',str(scores['X']),',O :',str(scores['O']))
	print('')
	print('NEXT ROUND')
	board = ['-','-','-','-','-','-','-','-','-']
	print('')
	print_board(board)
	return

def wincheck(board):
	if board[0] == board[1] == board[2] != '-':
		return True
	elif board[3] == board[4] == board[5] != '-':
		return True
	elif board[6] == board[7] == board[8] != '-':
		return True
	elif board[0] == board[3] == board[6] != '-':
		return True
	elif board[1] == board[4] == board[7] != '-':
		return True
	elif board[2] == board[5] == board[8] != '-':
		return True
	elif board[0] == board[4] == board[8] != '-':
		return True
	elif board[2] == board[4] == board[6] != '-':
		return True
	else:
		return False

def robo_input():
	global board
	ip = random.randint(1,9)
	while board[ip] != '-':
		ip = random.randint(1,9)
	board[ip] = 'O'
	return

def get_input(is_x):
	if not is_x:
		robo_input()
		return
	global board
	turn = 'X' if is_x else 'O'
	print('It\'s',turn,'turn')

	inp = input()
	if inp == 'e':
		sys.exit()
	try:
		z = int(inp) - 1
		while board[z] != '-':
			print('hey you cant conquer other\'s land')
			get_input(is_x)
			return
		board[z] = 'X' if is_x else 'O'
	except:
		print('enter valid index')
		get_input(is_x)
	return

def print_board(board):
	print('')
	print(''.join(board[:3]))
	print(''.join(board[3:6]))
	print(''.join(board[6:]))
	print('')
	return

board = ['-','-','-','-','-','-','-','-','-']
is_x = True
scores = {}
scores['X'] = 0
scores['O'] = 0
print('No of players?')
n = int(input())
if n is not in [1,2]:
	print('Not valid')
	sys.exit()
print_board(board)

while(True):
	get_input(is_x)
	print_board(board)
	check()
	is_x ^= 1