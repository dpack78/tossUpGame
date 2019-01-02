import StrategyBase
class AlwaysTrue(StrategyBase.StrategyBase):
    def __init__(self):
        StrategyBase.StrategyBase.__init__(self)

    def shouldIRoll(self, a_score,turnScore,diceToRoll,roundNumber):
        return True