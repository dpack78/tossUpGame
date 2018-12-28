import StrategyBase
class AlwaysTrue(StrategyBase.StrategyBase):
    def __init(self):
        pass

    def shouldIRoll(self, a_score,turnScore,diceToRoll,roundNumber):
        return True