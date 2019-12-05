from random import randrange
import random
import time 

class board:
	player1 = ''
	player2 = ''
	turn = ''
	pawn = ['x', 'o']
	board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
	index = -1
	flag = 2
	positions = ['0', '1', '2', '3', '4', '5', '6', '7', '8'] 

	def printBoard(self):
		print('    |    |')
		print(b.board[0], '  |', b.board[1], ' |' ,b.board[2])
		print('    |    |')
		print('-----------------')
		print('    |    |')
		print(b.board[3], '  |' , b.board[4], ' |' ,b.board[5])
		print('    |    |')
		print('-----------------')
		print('    |    |')
		print(b.board[6], '  |', b.board[7] , ' |' ,b.board[8])
		print('    |    |')

	def clearBoard(self):
		board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

	def checkBoard(self):
		if(b.board[b.index] == ' '):
	
			if(b.flag == 2):
				b.board[b.index] = b.player1
				b.flag = 1
				return 1
	
			if(b.flag == 1):
				b.board[b.index] = b.player2
				b.flag = 2
				return 1

		elif(b.board[b.index] != ''):
			print('\nPosition already occupied.')
			return 0


	def checkMove(self):
		if(b.checkBoard()):
			print('\nBoard updated sucessfully.')
			return 1

		else:
			print('\nTry again with different position.')
			return 0

	def setPawn(self):
		b.player1 = b.turn
	
		if(b.pawn.index(b.turn) == 0):
			b.player2 = b.pawn[1] 
	
		else:
			b.player2 = b.pawn[0]

	def winGame(self):
		if((b.board[0] == b.board[1] == b.board[2] == 'x') or (b.board[0] == b.board[1] == b.board[2] == '0')):
			return True
	
		if((b.board[3] == b.board[4] == b.board[5] == 'x') or (b.board[3] == b.board[4] == b.board[5] == 'o')):
			return True
	
		if((b.board[6] == b.board[7] == b.board[8] == 'x') or (b.board[6] == b.board[7] == b.board[8] == 'o')):
			return True
	
		if((b.board[2] == b.board[5] == b.board[8] == 'x') or (b.board[2] == b.board[5] == b.board[8] == 'o')):
			return False
	
		if((b.board[1] == b.board[4] == b.board[7] == 'x') or (b.board[1] == b.board[4] == b.board[7] == 'o')):
			return True
	
		if((b.board[0] == b.board[3] == b.board[6] == 'x') or (b.board[0] == b.board[3] == b.board[6] == 'o')):
			return True
	
		if((b.board[0] == b.board[4] == b.board[8] == 'x') or (b.board[0] == b.board[4] == b.board[8] == 'o')):
			return True
	
		if((b.board[2] == b.board[4] == b.board[6] == 'x') or (b.board[2] == b.board[4] == b.board[6] == 'o')):
			return True
	
		else:
			return False

	def drawGame(self):
		if(' ' in b.board):
			return False

		else:
			return True



def main(b):	
	b.player1 = 'x'
	b.player2 = 'o'

	while (b.winGame() == False):
		while (b.flag == 2):
			b.index = str(random.randint(0,8))
			if(b.index not in b.positions):
				print('\nSelect valid position.')
				continue
			b.index = int(b.index)
			b.checkMove()
			b.printBoard()

			if(b.winGame() == True):
				print('Player 1 has won!')
				return 0
			
		while (b.flag == 1):
			if(b.drawGame() == True):
				b.flag = 0
				print('The game ended in a draw!')
				return 0

			b.index = str(random.randint(0,8))
			if(b.index not in b.positions):
				print('\nSelect valid position.')
				continue
			b.index = int(b.index)
			b.checkMove()
			b.printBoard()
	
			if(b.winGame() == True):
				print('Player 2 has won!')
				return 0


if __name__ == '__main__':
	b = board()
	start = time.time()
	main(b)
	elapsed = (time.time() - start)
	print('Run time: ',elapsed)
	# with open('Serial.txt', 'a') as filehandle:
	with open('Parallel.txt', 'a') as filehandle:
		filehandle.writelines("%s" % item for item in b.board)
		filehandle.writelines("\t\t%s" % str(b.flag))
		filehandle.writelines("\n")