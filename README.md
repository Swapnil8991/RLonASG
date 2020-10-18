# RLonASG

## Description
   This project comprises of abstract-strategy games which are to be played by a Machine Learning Agent, against itself and against a human player. Our approach involves the use and application of reinforcement machine learning where, the agent is supposed to gradually learn and play the game on its own without any prior knowledge of the game. 

## Algorithms
* __Temporal Difference (TD) Learning__
   Temporal difference learning refers to a class of model-free reinforcement learning methods which learn by bootstrapping from the current estimate of the value function. These methods sample from the environment, like Monte Carlo methods, and perform updates based on current estimates, like dynamic programming methods.

* __Q-Learning__
   Q-learning is a model-free reinforcement learning algorithm to learn a policy telling an agent what action to take under what circumstances. It does not require a model of the environment, and it can handle problems with stochastic transitions and rewards, without requiring adaptations.

## Requirements

* Python 3.4 or higher
* TensorFlow Library
* A Modern CPU capable of Running TensorFlow
* An NVIDIA GPU card with CUDA Compute Capability of 3.5 or higher.


## Usage
* __TTT_3x3_SC__
	* __python Demo_TTT_HvH.py__
	  > Here, two humans play against each other.
	* __python Demo_TTT_RCvRC.py__
	  > Here, computer plays against itself by making random choices for a single instance.
	* __python Demo_TTT_RCvRC_MultipleGames.py__
	  > Here, computer plays against itself by making random choices for multiple instances.
	* __python TTT_GenerateData.py &nbsp; no_of_games &nbsp; dataGenFlag (1|2) &nbsp; inpTrainFilename &nbsp; outTrainFilename__
	  >    Generates the data for the Neural Network to train upon dataGenFlag: 1 for recording X's win, 2 for recording O's win.
	* __python TTT_HvNN.py &nbsp; inpTrainFilename &nbsp; outTrainFilename__
	  > Here, human plays against the Neural Network which has been trained upon the generated data from previous step.

* __TTT_3x3_VF__
	* __python TTT_HvVF.py__
	  > Here, the Varible function agent plays against a human player.
 	* __python TTT_RCvVF.py__
 	  > Here, the Random Computer(random choices) plays against Variable function agent. 
 	* __python TTT_VFvVF.py__
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
