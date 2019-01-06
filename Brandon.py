import StrategyBase
class Brandon(StrategyBase.StrategyBase):
    def __init__(self):
        StrategyBase.StrategyBase.__init__(self)

    def shouldIRoll(self, a_score,turnScore,diceToRoll,roundNumber):
        #not last turn
        if not self.isThisMyLastTurn(a_score):

            #cumulative score is < 100
            if self.getMyScore(a_score) + turnScore < 100:
                if turnScore <= 27:
                    rollAgain = True
                else:
                    rollAgain = False

            #cumulative score is > 100
            else:
                if self.getMyScore(a_score) + turnScore < self.getMaxScore(a_score) + 27:
                    rollAgain = True
                else:
                    rollAgain = False
        #last turn
        else:
            if self.getMyScore(a_score) + turnScore < self.getMaxScore(a_score):
                rollAgain = True
            else:
                rollAgain = False
        return rollAgain
