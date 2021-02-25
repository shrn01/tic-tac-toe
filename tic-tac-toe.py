import sys
import random
import pygame
from pygame.locals import *


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
	while board[ip-1] != '-':
		ip = random.randint(1,9)
	board[ip] = 'O'
	return

def get_input(is_x,pos):
	
	global board
	turn = 'X' if is_x else 'O'
	print('It\'s',turn,'turn')
	x, y = pygame.mouse.get_pos() 
	x = x // 100
	y = y // 100
	inp = (y * 3 + x + 1)
	z = int(inp) - 1
	board[z] = 'X' if is_x else 'O'
	return


def print_board(board):
	global screen
	global xtext
	global otext
	pygame.draw.line(screen,(0,0,0),(100,0),(100,300),7)
	pygame.draw.line(screen,(0,0,0),(200,0),(200,300),7)
	pygame.draw.line(screen,(0,0,0),(0,100),(300,100),7)
	pygame.draw.line(screen,(0,0,0),(0,200),(300,200),7)
	for i in range(len(board)):
		if board[i] == 'X':
			screen.blit(xtext,((i) % 3 * 100 + 25,(i) // 3 * 100 + 25))
		elif board[i] == 'O':
			screen.blit(otext,((i) % 3 * 100 + 25,(i) // 3 * 100 + 25))
	pygame.display.update()
	return


pygame.init()
screen = pygame.display.set_mode((300,300))
screen.fill((250,250,255))
pygame.font.init()
text = pygame.font.SysFont('Comic Sans MS', 30)
xtext = text.render('X',False,(0,0,0))
otext = text.render('O',False,(0,0,0))
x = text.render('X',True,(0,0,0))

board = ['-','-','-','-','-','-','-','-','-']
is_x = True
scores = {}
scores['X'] = 0
scores['O'] = 0
clock = pygame.time.Clock()

print_board(board)

while(True):
	for event in pygame.event.get(): 
		if event.type == QUIT: 
			pygame.quit() 
			sys.exit()
		if event.type == pygame.MOUSEBUTTONDOWN:
			is_x ^= 1
			get_input(is_x,pygame.mouse.get_pos())
			print_board(board)
			check()
	pygame.display.update()
	clock.tick(10)