import Game
import operator
import SafeGlobals
import threading
import multiprocessing
import constants
class GameSet():
    def __init__(self,gameCount,a_strategy):
        self.a_strategy = a_strategy
        self.Globals = SafeGlobals.SafeGlobals(a_strategy)

    def run(self):
        a_thread = []
        for i in range(constants.THREAD_COUNT):
            a_thread.append(
                # threading.Thread(target=self.threadAction, args=())
                multiprocessing.Process(target=self.threadAction, args=())
            )
            a_thread[-1].start()
        for t in a_thread:
            t.join()
        self.printResults()
    
    def threadAction(self):
        gameCount = self.Globals.getGameCount()
        while(gameCount > 0):
            SingleGame = Game.Game(self.a_strategy)
            a_finalScore = SingleGame.run()
            self.proccessFinalScore(a_finalScore)
            gameCount = self.Globals.getGameCount()

    def proccessFinalScore(self,a_finalScore):
        self.Globals.proccessFinalScore(a_finalScore)

    def printResults(self):
        print('')
        print('Total scores: ')
        print(self.Globals.a_totalScore)
        print('')
        print('Games won')
        print(sorted(self.Globals.a_gamesWon.items(), key=operator.itemgetter(1)))
        print('')