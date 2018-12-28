import random
import StrategyFactory
import RollGetter
import constants

class Game():
    def __init__(self,a_strategy):
        #shuffle the array to randomize the turn order each game
        random.shuffle(a_strategy)
        self.a_strategy = a_strategy
        self.gameOver = False
        self.a_score = {}
        self.a_StrategyClass = {}
        self.a_hadLastTurn = {}
        self.onLastRound = False
        self.round = 0

        SF = StrategyFactory.StrategyFactory()
        for player in self.a_strategy:
            self.a_score[player] = 0
            self.a_StrategyClass[player] = SF.getStrategyClass(player)
            self.a_hadLastTurn[player] = False

    def run(self):
        while(not self.gameOver):
            someoneHasATurn = False
            for player, StratClass in self.a_StrategyClass.items():
                if(self.a_hadLastTurn[player]):
                    continue
                someoneHasATurn = True
                self.runTurn(player)
            
            if(not someoneHasATurn):
                self.gameOver = True
            
            self.round += 1
            if(self.round > 100):
                self.gameOver = True
        # print(self.a_score)
        return self.a_score
            
    def runTurn(self,player):
        self.printTurnStarted(player)
        curDiceToBeRolled = 10
        turnScore = 0
        turnGoing = True
        while(turnGoing):
            shouldRoll = self.a_StrategyClass[player].shouldIRollBase(
                self.a_score,
                turnScore,
                curDiceToBeRolled
            )
            if(shouldRoll):
                a_roll = RollGetter.getRoll(curDiceToBeRolled)
                if(not RollGetter.rolePassed(a_roll)):
                    turnScore = 0
                    turnGoing = False
                rollScore = RollGetter.rollScore(a_roll)
                turnScore += rollScore
                curDiceToBeRolled -= rollScore
                if(curDiceToBeRolled <= 0):
                    curDiceToBeRolled = 10
            else:
                turnGoing = False
        self.printTurnEnded(player,turnScore)

        self.a_score[player] += turnScore
        if(self.a_score[player] >= 100):
            self.onLastRound = True

        if(self.onLastRound):
            self.a_hadLastTurn[player] = True

    def printTurnStarted(self,player):
        if(constants.DEBUG_ON):
            print('PLAYER ' + player + ' STARTED TURN')

    def printTurnEnded(self,player,turnScore):
        if(constants.DEBUG_ON):
            print('PLAYER ' + player + ' ENDED TURN SCORE ' + str(turnScore))
            print('')
            print('//////////////')
            print('')