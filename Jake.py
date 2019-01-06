from StrategyBase import StrategyBase


class Jake(StrategyBase):
    SAFE_LEAD = 38
    WINNING_SCORE = 100

    def __init(self):
        pass

    def shouldIRoll(self, a_score, turn_score, dice_to_roll, round_number):
        self._a_score = a_score
        self._turn_score = turn_score
        self._dice_to_roll = dice_to_roll
        self._round_number = round_number
        self._my_score = self.getMyScore(self._a_score)
        self._running_total = self._my_score + self._turn_score
        self._max_score = self.getMaxScore(self._a_score)
        self._is_last_turn = self.isThisMyLastTurn(self._a_score)

        if self._is_last_turn and self._im_not_winning():
            return True

        if self._roll_could_break_hundred():
            return self._follow_safe_logic() if self._my_score >= 90 else False

        if not self._is_last_turn and self._my_score >= 100 and not self._in_comfortable_lead():
            return True

        return self._follow_safe_logic()

    def _follow_safe_logic(self):
        if self._dice_to_roll >= 5:
            return True
        if self._dice_to_roll >= 4 and self._turn_score < 36:
            return True
        if self._turn_score < 27:
            return True

        return False

    def _im_winning(self):
        return  self._my_score + self._turn_score > self._max_score

    def _im_not_winning(self):
        return not self._im_winning()

    def _roll_could_break_hundred(self):
        return self._running_total < 100  and self._running_total + self._dice_to_roll >= 100

    def _in_comfortable_lead(self):
        return self._running_total > self._max_score + self.SAFE_LEAD
