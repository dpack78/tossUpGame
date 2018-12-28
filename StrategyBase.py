import constants
class StrategyBase():
    def __init__(self):
        self.debugMode = constants.DEBUG_ON

    def getMyScore(self,a_score):
        playerName = self.getPlayerName()
        return a_score[playerName]

    def getMaxScore(self,a_score):
        return max(a_score.values())

    def isThisMyLastTurn(self,a_score):
        maxScore = self.getMaxScore(a_score)
        return maxScore >= 100

    def printTurn(self,a_score, turnScore, diceToRoll,shouldRoll):
        if(self.debugMode):
            print('')
            print('current score: ')
            print(a_score)
            print('Turn score: '+  str(turnScore))
            print('diceToRoll: '+ str(diceToRoll))
            if(shouldRoll):
                print('Decided to roll')
            else:
                print('Decided not to roll')
            print('')

    def getPlayerName(self):
       return self.__class__.__name__

    def shouldIRollBase(self,a_score,turnScore,diceToRoll):
        shouldRoll = self.shouldIRoll(a_score,turnScore,diceToRoll)
        self.printTurn(a_score,turnScore,diceToRoll,shouldRoll)
        return shouldRoll

    def shouldIRoll(self,a_score,turnScore,diceToRoll):
        raise NotImplementedError('Your strategy class must have a function shouldIRoll declared')

