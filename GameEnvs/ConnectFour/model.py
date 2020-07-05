from keras.models import Sequential 
from keras.initializers import RandomNormal
from keras.layers import Dense
from keras.layers import BatchNormalization
from keras.layers import Dropout
from sys import argv
import numpy as np

from time import time
from itertools import cycle
from C4Board import C4Board


def loadData(inpDataFile, outDataFile):
	xInpTrainArray = np.loadtxt('__data__/' + inpDataFile, dtype=int)
	xOutTrainArray = np.loadtxt('__data__/' + outDataFile, dtype=int)
	inpDim = xInpTrainArray.shape[1]
	outDim = xOutTrainArray.shape[1]
	return xInpTrainArray, xOutTrainArray, inpDim, outDim


def modelInit(inpDim, outDim):
	model = Sequential()
	model.add(Dense(units=1024, activation='relu', input_dim=inpDim, kernel_initializer=RandomNormal(mean=0.0, stddev=0.062, seed=None)))
	model.add(Dropout(0.25))
	model.add(Dense(units=512, activation='relu'))
	model.add(Dropout(0.125))
	model.add(Dense(units=256, activation='relu'))
	model.add(Dropout(0.025))
	model.add(Dense(units=128, activation='relu'))
	# model.add(Dropout(0.0025))
	model.add(Dense(units=64, activation='relu'))
	model.add(Dense(units=outDim, activation='softmax'))
	print(model.summary())
	return model

def modelCompile(model):
	model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
	return model

def modelTrain(model, inpDataArray, outDataArray):
	model.fit(inpDataArray, outDataArray, batch_size=1024, epochs=10, verbose=1)
	return model

def predictNextMove(model, board):
	inputList = board.tolist()
	outputArray = model.predict(np.array([inputList]))
	outputList = list(outputArray[0])
	# print(outputList)
	position = outputList.index(max(outputList)) 
	print("Player X: ",position)
	while not b.makeMove(cPNum, position):
		outputList[position] = 0
		print(outputList)
		position = outputList.index(max(outputList))
		print("Player X: ",position)	
	return True


if __name__ == '__main__':
	if len(argv) != 3:
		print("\nProvide the training data files.\nUsage: python TTT_HvNN.py inpTrain.txt outTrain.txt\n")
	else:
		# Train the model
		xInpTrainArray, xOutTrainArray, inpDim, outDim = loadData(argv[1], argv[2])
		model = modelInit(inpDim, outDim)
		model = modelCompile(model)
		model = modelTrain(model, xInpTrainArray, xOutTrainArray)
		model.save('saved_model/C4Model')
		b = C4Board()
		b.printInfo()

		for i in range(42):
			emptyPosition = b.board.tolist()
			playerCharToggler = cycle(['X', 'O'])
			playerNumToggler = cycle([3, -2])

			while b.count < 42:
				# emptyPosition = b.board.tolist()
				
				# print("emptyPosition: \n", emptyPosition)

				if b.count > 6:
					status, wSindex = b.checkWin()
					if status == 0:
						print(f"Game Draw! {b.getwStateSum()}\n")
						break
					elif status == 1:
						print(f"Player X Wins! (wState[{wSindex}]: {b.wState[wSindex]}) {b.getwStateSum()}\n")
						break
					elif status == 2:
						print(f"Player O Wins! (wState[{wSindex}]: {b.wState[wSindex]}) {b.getwStateSum()}\n")
						break

				cPChar = next(playerCharToggler)
				cPNum = next(playerNumToggler)

				if(cPNum == 3):
					# position = predictNextMove(model, b.board, emptyPosition)
					while not predictNextMove(model, b.board):
						# position = predictNextMove(model, b.board, emptyPosition) 
						# b.makeMove(cPNum, position)
						print("Already Occuipied or Invalid Position", end='')
						# print(f"\nPlayer {cPChar}: ", end='', flush=True)
						# break
					b.printBoard()

				elif(cPNum == -2):
					# print(f"\nPlayer {cPChar}: ", end='', flush=True)
					while not b.makeMove(cPNum, int(input("Player 0: "))):
						# position = int(input())
						# b.makeMove(cPNum, position)
						print("Already Occuipied or Invalid Position", end='')
						# print(f"\nPlayer {cPChar}: ", end='', flush=True)
						# break					
					b.printBoard()

			b.resetBoard()