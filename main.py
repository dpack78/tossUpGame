import GameSet as GameSet
import constants
import time

def main():
    start = time.time()
    Main = GameSet.GameSet(constants.GAME_COUNT,constants.a_strategy)
    Main.run()
    end = time.time()
    print('run time: ')
    print(end-start)
    print('')

if __name__ == '__main__':
    main()