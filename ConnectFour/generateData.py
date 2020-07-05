import numpy as np

from C4Board import C4Board
from random import seed, choice
from os import urandom
from time import time
from itertools import cycle
from sys import argv


def getTrainingData(noOfGames, dataGenFlag, inpTrainFile, outTrainFile):
	
	turnFlag = 0
	gameEndState = 0
	
	tempOutTrainList = [] # stores expected input position
	boardStates = []  # stores the board state at input

	inpTrainList = []
	outTrainList = [] 

	for i in range(noOfGames):
		boardStates.append(b.board.tolist())
		# print("\n First boardState: \n", boardStates)
		emptyPositions = list(range(0, 7))

		while b.count < 42:
			if b.count > 7:
				status, wSindex = b.checkWin()
				if status == 0:
					print(f"Game Draw! {b.getwStateSum()}\n")
					break
				elif status == 1 and dataGenFlag == 1 and turnFlag == 1:
					print(f"Player X Wins! (wState[{wSindex}]: {b.wState[wSindex]}) {b.getwStateSum()}\n")
					for i in range(len(tempOutTrainList)):
						if i % 2 == 0:
							outTrainList.append(tempOutTrainList[i])
					
							inpTrainList.append(boardStates[i])
					break
				elif status == 2:
					print(f"Player O Wins! (wState[{wSindex}]: {b.wState[wSindex]}) {b.getwStateSum()}\n")
					break

			cPChar = next(playerCharToggler)
			cPNum = next(playerNumToggler)
			if cPChar == 'X' and turnFlag == 0:
				turnFlag = 1
			elif cPChar == 'Y' and turnFlag == 0:
				turnFlag = 2
			position = choice(emptyPositions)
			# print(f"\nPlayer {cPChar}: {position}")
			# b.makeMove(cPNum, position)
			# print(f"\nPlayer {cPChar}: ", end='', flush=True)
			b.makeMove(cPNum, position )
			print(f"\nPlayer {cPChar}: ", end='', flush=True)
			boardStates.append(b.board.tolist())
			# print("\nboardStates: \n", boardStates)

			zeroList = [0, 0, 0, 0, 0, 0, 0]
			zeroList[position] = 1
			tempOutTrainList.append(zeroList)
			# print("\nExpected output by NN: \n", tempOutTrainList)
			b.printBoard()
		b.resetBoard()
		
	print("\n\n inpTrainList: \n", len(inpTrainList))
	print("\n\n outTrainList: \n", len(outTrainList))

	xOutArray = np.array(outTrainList)
	xInpArray = np.array(inpTrainList)
	np.savetxt('__data__/' + outTrainFile, xOutArray, fmt='%d')
	np.savetxt('__data__/' + inpTrainFile, xInpArray, fmt='%d')

	
if __name__ == '__main__':

	if len(argv) != 5:
		print("Provide no. of games, dataGenFlag (1|2), inpTrainFile, outTrainFile")
	else:
		startTime = time()

		b = C4Board()
		playerCharToggler = cycle(['X', 'O'])               # D-Char
		playerNumToggler = cycle([3, -2])                   # D-Val
		seed(urandom(128))

		getTrainingData(int(argv[1]), int(argv[2]), argv[3], argv[4])

		print(f"Time taken: {time() - startTime}s\n")