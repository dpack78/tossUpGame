import StrategyBase
import random
class LBP27(StrategyBase.StrategyBase):
    def __init__(self):
        StrategyBase.StrategyBase.__init__(self)

    def shouldIRoll(self, a_score,turnScore,diceToRoll,roundNumber):
        if(turnScore<27):
            return True
        return False

