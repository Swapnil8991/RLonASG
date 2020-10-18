# RLonASG

## Description
   This project comprises of abstract-strategy games which are to be played by a Machine Learning Agent, against itself and against a human player. Our approach involves the use and application of reinforcement machine learning where, the agent is supposed to gradually learn and play the game on its own without any prior knowledge of the game. 

## Algorithms
* Temporal Difference (TD) Learning
* Q-Learning


## Requirements

* Python 3.4 or higher
* TensorFlow Library
* A Modern CPU capable of Running TensorFlow
* An NVIDIA GPU card with CUDA Compute Capability of 3.5 or higher.


## Usage
* TTT_3x3_SC
	* python TTT_GenerateData.py <no_of_games> <dataGenFlag (1|2)> <NNInpFilename> <NNOutFilename>
	>    Generate the data for the Neural Network to train upon dataGenFlag: 1 for recording X's win and 2 for recording O's win.  	
* TTT_3x3_VF
	* python TTT_HvVF.py
	> A game where the Varible function agent plays against a human player.
 	* python TTT_RCvVF.py
 	> A game where Random Computer(random choices) plays against Variable function agent. 
 	* python TTT_VFvVF.py
 	>  A game where two Variable function agents play against eacg other.

## Screenshots
```
![alt text](/pathToImage/icon48.png "Img Name")
```

## External References
* Sutton, Richard S. __“Learning to Predict by the Methods of Temporal Differences.”__ 
*    Rajarshi Das, Armonk, Gerald J. Tesauro, Croton-on-Hudson, Kilian Q. Weinberger. "__Method and Apparatus for improved Reward-Based Learning Using Nonlinear Dimensionality Reduction.__"

## License
The entire codebase is under __MIT License__
