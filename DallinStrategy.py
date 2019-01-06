import StrategyBase
import constants

class DallinStrategy(StrategyBase.StrategyBase):
    def __init__(self):
        self.debugMode = constants.DEBUG_ON
        self.StrategyBase = StrategyBase.StrategyBase

    def shouldIRoll(self, a_score, turnScore, diceToRoll, roundNumber):
        if diceToRoll > 3:
            return True
        elif diceToRoll == 3:
            if turnScore < 39:
                return True
            else:
                return False
        else:
            if turnScore < 29:
                return True
            else:
                return False