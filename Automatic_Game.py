
from A_move.GetPieceLegalMoves import *
"""
from B_analyze.GetPlayerPositions import *
from B_analyze.AnalyzePlayer import *
from B_analyze.TotalMaterial import *
from B_analyze.BestMoves import *
"""
from C_play.PrintBoard import *
from C_play.HumanPlayer import *
from C_play.UpdateBoard import *
"""
from D_generation.GenerateMove import *
from D_generation.GenerateAlphaBeta_2 import * #1 works
from D_generation.GenerateAlphaBeta_Endgame import *
"""
from chessPlayer import *

def main_3():
    B=InitBoard()
    PrintBoard(B)
    while True:
        white=chessPlayer(B,10)
        #PrintBoard(B)
        r=UpdateBoard(B,10,white[1])
        PrintBoard(B)
        if r==1:
            print("WHITE VICTORY")
            #PrintBoard(B)
            return 1
        
        black=chessPlayer(B,20)
        
        r=UpdateBoard(B,20,black[1]) #was [B,r]... int not iterable

        PrintBoard(B)
        if r==2:
            print("BLACK VICTORY")
            #PrintBoard(B)
            return 2
"""
def main_2(): #Use with GenerateAlphaBeta_2
    B=InitBoard()
    #B=InitMate()
    while True:
        t=TotalMaterial(B)
        
        if t>500:
            move=alphaBeta_general(B,10,3,3,-20000,20000)[1]
        else:
            move=alphaBeta_Endgame(B,10,8,8,-20000,20000)[1]

        
        #GenerateMove(B,10)#GenerateTree(B,10,3)[0][0]
        #print("White Best Move:", BestMove_Single(B,move,10))
        #print("Possible Moves:", move)
        PrintBoard(B)
        r=UpdateBoard(B,10,BestMove_Single(B,move,10)[0])
        if r==1:
            print("WHITE VICTORY")
            PrintBoard(B)
            return 1

        t=TotalMaterial(B)
        
        if t>500:
            move=alphaBeta_general(B,20,3,3,-20000,20000)[1]
        else:
            move=alphaBeta_Endgame(B,20,8,8,-20000,20000)[1]
            
        #GenerateMove(B,20)#GenerateTree(B,20,3)[0][0]
        #print("Black Best Move:",BestMove_Single(B,move,20))
        #print("Possible Moves:", move)
        PrintBoard(B)
        r=UpdateBoard(B,20,BestMove_Single(B,move,20)[0]) #was [B,r]... int not iterable
        if r==2:
            print("BLACK VICTORY")
            PrintBoard(B)
            return 2

"""
"""
def main():
    B=InitBoard()
    #B=InitMate()
    while True:
        t=TotalMaterial(B)
        
        if t>500:
            move=alphaBeta_general(B,10,3,3,-20000,20000)
        else:
            move=alphaBeta_Endgame(B,10,6,6,-20000,20000)

        
        #GenerateMove(B,10)#GenerateTree(B,10,3)[0][0]
        print("White Best Move:", BestMove_Single(B,move,10))
        print("Possible Moves:", move)
        PrintBoard(B)
        r=UpdateBoard(B,10,BestMove_Single(B,move,10)[0])
        if r==1:
            print("WHITE VICTORY")
            PrintBoard(B)
            return 1

        move=alphaBeta_general(B,20,3,3,-20000,20000)
        #GenerateMove(B,20)#GenerateTree(B,20,3)[0][0]
        print("Black Best Move:",BestMove_Single(B,move,20))
        print("Possible Moves:", move)
        PrintBoard(B)
        r=UpdateBoard(B,20,BestMove_Single(B,move,20)[0]) #was [B,r]... int not iterable
        if r==2:
            print("BLACK VICTORY")
            PrintBoard(B)
            return 2
"""
            
"""
def main_normal():
    B=InitBoard()
    #B=InitMate()
    while True:
        move=GenerateMove(B,10)#GenerateTree(B,10,3)[0][0]
        print("White Best Move:", move)
        PrintBoard(B)
        r=UpdateBoard(B,10,move)
        if r==1:
            print("WHITE VICTORY")
            PrintBoard(B)
            return 1

        move=GenerateMove(B,20)#GenerateTree(B,20,3)[0][0]
        print("Black Best Move:", move)
        PrintBoard(B)
        r=UpdateBoard(B,20,move) #was [B,r]... int not iterable
        if r==2:
            print("BLACK VICTORY")
            PrintBoard(B)
            return 2
"""

main_3()
