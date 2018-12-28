This is a coding competition set up for Toss Up

The rules are here:
https://cdn.shptrn.com/media/mfg/1725/media_document/8976/TossUpRules2.pdf?1401294917

The game is played with 10 dice each having 3 green sides, 2 yellow sides and 1 red side.

The strategy of the game comes down to one decision: should I roll again?

For this competition you'll create a function that answers that question as follows:

To add your own strategy, add a python file with the name of your strategy. 
Create a class with the same name as the file. 
This class must extend StrategyBase.StrategyBase

This class must have a method defined shouldIRoll(self, a_score,turnScore,diceToRoll,roundNumber) that returns a boolean.

See "RandomDecision.py" for an example. This strategy randomly decides to roll again or not. Ideally your strategy can beat this one. 

You must also add this strategy name to the a_strategy array in constants.py

a_score is a dictionary with keys of each player name/strategy and values of their current score.

turnScore is the score you have built up from rolling on this turn. This is the score that will be added to your total score if you decide not to roll again.

diceToRoll is the current dice out of 10 that you will roll if you decide to roll again. 

roundNumber is the nth turn that you are on starting at 1. The game will quit after 1000 turns.

For the competition you'll only submit your python file with your strategy in it.
So any changes to the rest of the code will not be considered.

Note that because your strategy class extends StrategyBase you have several functions already available to you for your use.

Notice the constants file also has a debug mode that if true, will give a detailed printout of the game. 
You can also change the GAME_COUNT to run more that 1 game inside a simulation

Once you are ready run main.py to see the results!