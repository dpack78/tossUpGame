import StrategyBase
import random
class DaveFinal(StrategyBase.StrategyBase):
    def __init__(self):
        StrategyBase.StrategyBase.__init__(self)
        self.quittingNumber = 37
        self.highQuittingNumber = 57
        self.lowQuittingNumber = 27

    def shouldIRoll(self, a_score,turnScore,diceToRoll,roundNumber):
        lastTurn = self.isThisMyLastTurn(a_score)
        if(lastTurn):
            return self.lastTurn(a_score,turnScore,diceToRoll,roundNumber)
        if(self.stopCloseTo100(a_score,turnScore,diceToRoll)):
            return False 
        if(turnScore <= self.quittingNumber): 
            return True
        if(diceToRoll > 3):
            return True
        return False

    def lastTurn(self, a_score,turnScore,diceToRoll,roundNumber):
        maxScore = self.getMaxScore(a_score)
        myScore = self.getMyScore(a_score)
        myPotentialScore = myScore + turnScore
        if(myPotentialScore <= maxScore):
            return True
        potentialMax = self.getLastTurnBufferAmount(a_score,maxScore) 
        if(potentialMax > myPotentialScore):
            return True
        return False
    
    def getLastTurnBufferAmount(self,a_score,maxScore):
        myName = self.getPlayerName()
        otherMaxScore = 0
        # get the highest score that is not mine and is below 100
        # this person may have another turn
        for player, score in a_score.items():
            if(player == myName):
                continue
            if(score >= 100):
                continue
            otherMaxScore = score
        potentialScore = otherMaxScore + 36
        return potentialScore
    
    def stopCloseTo100(self,a_score,turnScore,diceToRoll):
        if(turnScore < 3):
            return False
        myScore = self.getMyScore(a_score)
        potentialScore = myScore + turnScore
        winningByAlot = self.getWinningByAlot(a_score,myScore)
        if(potentialScore < 100 and potentialScore > 94 and not winningByAlot):
            return True
        return False
    
    def getWinningByAlot(self,a_score,myScore):
        greatestScoreDiff = 0
        for player, score in a_score.items():
            scoreDiff = myScore - score
            if(scoreDiff > greatestScoreDiff):
                greatestScoreDiff = scoreDiff
        if(greatestScoreDiff > 57):
            return True
        return False