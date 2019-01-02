import Game
import operator
class GameSet():
    def __init__(self,gameCount,a_strategy):
        self.gameCount = gameCount
        self.a_strategy = a_strategy
        self.a_gamesWon = {}
        self.a_totalScore = {}
        for player in self.a_strategy:
            self.a_gamesWon[player] = 0
            self.a_totalScore[player] = 0

    def run(self):
        for i in range(self.gameCount):
            SingleGame = Game.Game(self.a_strategy)
            a_finalScore = SingleGame.run()
            self.proccessFinalScore(a_finalScore)
        self.printResults()

    def proccessFinalScore(self,a_finalScore):
        curMax = 0
        winningPlayer = 'error'
        for player, score in a_finalScore.items(): 
            if(score >= curMax):
                curMax = score
                winningPlayer = player
            self.a_totalScore[player] += score
        self.a_gamesWon[winningPlayer] += 1

    def printResults(self):
        print('')
        print('Total scores: ')
        print(self.a_totalScore)
        print('')
        print('Games won')
        print(sorted(self.a_gamesWon.items(), key=operator.itemgetter(1)))
        print('')