import StrategyBase
import random
class RandomDecision(StrategyBase.StrategyBase):
    def __init(self):
        pass

    def shouldIRoll(self, a_score,turnScore,diceToRoll,roundNumber):
        return random.choice([True, False])