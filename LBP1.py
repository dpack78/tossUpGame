import StrategyBase
import random
class LBP1(StrategyBase.StrategyBase):
    def __init__(self):
        StrategyBase.StrategyBase.__init__(self)
        self.stopScore=27

    def shouldIRoll(self, a_score,turnScore,diceToRoll,roundNumber):
        maxScore=self.getMaxScore(a_score)
        myScore=self.getMyScore(a_score)
        if self.isThisMyLastTurn(a_score):
            return self.lastTurnDecision(a_score,turnScore,diceToRoll,roundNumber)
        if(maxScore>60 and myScore<30):
            self.stopScore+=10
        if(maxScore>90 and myScore<60):
            self.stopScore+=20
        if(turnScore<self.stopScore):
            return True
        if(diceToRoll>3):
            return True
        return False

    def lastTurnDecision(self, a_score, turnScore, diceToRoll, roundNumber):
        maxScore=self.getMaxScore(a_score)
        myScore=self.getMyScore(a_score)
        if(myScore<maxScore):
            return True
        if (diceToRoll > 3):
            return True
        return False

