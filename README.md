# RLonASG

## Description
   This project comprises of abstract-strategy games which are to be played by a Machine Learning Agent, against itself and against a human player. Our approach involves the use and application of reinforcement machine learning where, the agent is supposed to gradually learn and play the game on its own without any prior knowledge of the game. 

## Algorithms
* Temporal Difference (TD) Learning
   Temporal difference learning refers to a class of model-free reinforcement learning methods which learn by bootstrapping from the current estimate of the value function. These methods sample from the environment, like Monte Carlo methods, and perform updates based on current estimates, like dynamic programming methods.

* Q-Learning
   Q-learning is a model-free reinforcement learning algorithm to learn a policy telling an agent what action to take under what circumstances. It does not require a model of the environment, and it can handle problems with stochastic transitions and rewards, without requiring adaptations.

## Requirements

* Python 3.4 or higher
* TensorFlow Library
* A Modern CPU capable of Running TensorFlow
* An NVIDIA GPU card with CUDA Compute Capability of 3.5 or higher.


## Usage
* TTT_3x3_SC
	* python Demo_TTT_HvH.py
	  > Here, two humans play against each other.
	* python Demo_TTT_RCvRC.py
	  > Here, computer play against itself by making random choices for a single instance.
	* python Demo_TTT_RCvRC_MultipleGames.py
	  > Here, computer play against itself by making random choices for multiple instances.
	* python TTT_GenerateData.py <no_of_games> <dataGenFlag (1|2)> <inpTrainFilename> <outTrainFilename>
	  >    Generate the data for the Neural Network to train upon dataGenFlag: 1 for recording X's win, 2 for recording O's win.
	* python TTT_HvNN.py <inpTrainFilename> <outTrainFilename>
	  > Here, human plays against the Neural Network which has been trained upon the generated data from previous step.

* TTT_3x3_VF
	* python TTT_HvVF.py
	  > Here, the Varible function agent plays against a human player.
 	* python TTT_RCvVF.py
 	  > Here, the Random Computer(random choices) plays against Variable function agent. 
 	* python TTT_VFvVF.py
 	  > Here, two Variable function agents play against eacg other.

## Screenshots
```
![alt text](/pathToImage/icon48.png "Img Name")
```

## External References
* Sutton, Richard S. __“Learning to Predict by the Methods of Temporal Differences.”__ 
*    Rajarshi Das, Armonk, Gerald J. Tesauro, Croton-on-Hudson, Kilian Q. Weinberger. "__Method and Apparatus for improved Reward-Based Learning Using Nonlinear Dimensionality Reduction.__"

## License
The entire codebase is under __MIT License__
