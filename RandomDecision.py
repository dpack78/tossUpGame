import StrategyBase
import random
class RandomDecision(StrategyBase.StrategyBase):
    def __init__(self):
        StrategyBase.StrategyBase.__init__(self)

    def shouldIRoll(self, a_score,turnScore,diceToRoll,roundNumber):
        return random.choice([True, False])