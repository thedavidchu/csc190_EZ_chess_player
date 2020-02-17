from A_move.GetPieceLegalMoves import *
from B_analyze.GetPlayerPositions import *
from B_analyze.AnalyzePlayer import *
from C_play.PrintBoard import *
from C_play.HumanPlayer import *
from C_play.UpdateBoard import *


def main():
    B=InitBoard()
    #B=InitMate()
    while True:

        B=HumanPlayer(B,10)
        if AnalyzePlayer(B,10)>9000:
             print("WHITE VICTORY")
             return 1

        B=HumanPlayer(B,20)
        if AnalyzePlayer(B,20)>9000:
            print("BLACK VICTORY")
            return 2


main()
