from A_move.GetPieceLegalMoves import *

from B_analyze.GetPlayerPositions import *
from B_analyze.AnalyzePlayer import *
from B_analyze.TotalMaterial import *
from B_analyze.BestMoves import *
"""
from C_play.PrintBoard import *
from C_play.HumanPlayer import *
from C_play.UpdateBoard import *
"""
#from D_generation.GenerateMove import *
from D_generation.GenerateAlphaBeta_2 import * #1 works
from D_generation.GenerateAlphaBeta_Endgame import *

def chessPlayer(B,player):

    try:
        t=TotalMaterial(B)
        
        if t>1000:
            moves=alphaBeta_general(B,player,3,3,-20000,20000)[1]
        elif t>500:
            moves=alphaBeta_general(B,player,5,5,-20000,20000)[1]
        else:
            moves=alphaBeta_general(B,player,6,6,-20000,20000)[1]

        #Extract i!
        best=BestMove_Single(B,moves,player)[0]
        #print(best, moves[0])

        #CandidateMoves!

        cand=[]
        for i in moves:
            cand+=[i[0:2]]
            
        print(cand)

        #Level-Order Evaluation tree
        evalTree=EvaluationTree(moves)
        
        return [True,best,cand,evalTree]#[status,move,candidateMoves,evalTree]
    except:
        return False

def EvaluationTree(moves):
    primary=[]
    secondary=[]
    tertiary=[]
    
    for i in moves:
        if moves[2][0]!=[]:
            primary+=[i[0:2]]
        if len(i)==3:
            for j in i[2]:
                secondary+=[j[0:2]]
                if len(j)==3:
                    for k in j[2]:
                        tertiary+=[k[0:2]]
                
    return primary + secondary + tertiary
