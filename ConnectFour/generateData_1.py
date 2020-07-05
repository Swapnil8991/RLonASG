import numpy as np

from C4Board import C4Board
from random import seed, choice
from os import urandom
from time import time
from itertools import cycle
from sys import argv

def getTrainingData(noOfGames, dataGenFlag, inpTrainFile, outTrainFile):
	turnFlag = 0
	gameEndState = False

	tempInpTrainList = []      #List to store input positions for discs i.e 0 - 6
	tempStateList = []         #List to store the current board state i.e 0 - 41

	inpTrainList = []          #List to store the input to the NN
	outTrainList = []          #List to store the output from the NN


	for i in range(noOfGames):
		tempStateList.append(b.board.tolist())
		emptyPositions = list(range(0, 7))

		while b.count < 42:
			if b.count > 7:
				status, wSindex = b.checkWin()
				if status == 0:
					print(f"Game Draw! {b.getwStateSum()}\n")
					break
				elif status == 1:
					print(f"Player X Wins! (wState[{wSindex}]: {b.wState[wSindex]}) {b.getwStateSum()}\n")
					gameEndState = True
					break
				elif status == 2:
					print(f"Player O Wins! (wState[{wSindex}]: {b.wState[wSindex]}) {b.getwStateSum()}\n")
					gameEndState = True
					break

			cPChar = next(playerCharToggler)
			cPNum = next(playerNumToggler)
			if turnFlag == 0 and cPChar == 'X':
				turnFlag = 1
			else:
				turnFlag = 2
			position = 0
			print(f"\nPlayer {cPChar}: ", end='', flush=True)
			while not b.makeMove(cPNum, tposition = choice(emptyPositions)):
				position = tposition
				print(f"\nPlayer {cPChar}: ", end='', flush=True)
			tempStateList.append(b.board.tolist())

			if gameEndState == False:
				zeroList = [0, 0, 0, 0, 0, 0, 0]
				zeroList[position] = 1
				tempInpTrainList.append(zeroList)
			# b.printBoard()
		b.resetBoard()

		print("\n\n Tempstatelist:\n", len(tempStateList))
		print("\n\n tempInpTrainList:\n", len(tempInpTrainList))

		if turnFlag == 1 and dataGenFlag == 1:
			for i in range(len(tempStateList)):
				if i % 2 == 0:
					inpTrainList.append(tempStateList[i])
					outTrainList.append(tempInpTrainList)
	print("\n\n Expected input of NN: \n", len(inpTrainList), inpTrainList)
	print("\n\n Expected input to NN: \n", len(outTrainList), outTrainList)

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


