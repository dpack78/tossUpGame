import constants
import threading
import multiprocessing
class SafeGlobals():
    def __init__(self,a_strategy):
        self.gameCount = constants.GAME_COUNT
        # self.lock = threading.Lock()
        self.lock = multiprocessing.Lock()
        # self.lockGameCount = threading.Lock()
        self.lockGameCount = multiprocessing.Lock()
        self.a_gamesWon = {}
        self.a_totalScore = {}
        with self.lockGameCount:
            for player in a_strategy:
                self.a_gamesWon[player] = 0
                self.a_totalScore[player] = 0
    
    def getGameCount(self):
        gameCountReturn = 0
        with self.lock:
            gameCountReturn = self.gameCount
            self.gameCount -= 1
        return gameCountReturn
    
    def proccessFinalScore(self,a_finalScore):
        with self.lockGameCount:
            curMax = 0
            winningPlayer = 'error'
            for player, score in a_finalScore.items(): 
                if(score >= curMax):
                    curMax = score
                    winningPlayer = player
                self.a_totalScore[player] += score
            self.a_gamesWon[winningPlayer] += 1
            print(self.a_gamesWon)

