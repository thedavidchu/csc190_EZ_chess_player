from B_analyze.AnalyzePlayer import *
from A_move.GetPieceLegalMoves import *
from B_analyze.GetPlayerPositions import *

def BestNum(moves):
    best=moves[0][1]
    
    for i in moves:
        if i[1]>best:
            best=i[1]
    return best

def SimulateBoard(B,move): #[board,move]->[new_board]
    temp=list(B)
    temp[move[1]]=temp[move[0]]
    temp[move[0]]=0

    if temp[move[1]]==10 and move[1]<8:
        temp[move[1]]=14
    elif temp[move[1]]==20 and move[1]>55:
        temp[move[1]]=24

    return temp

def alphaBeta_EndgameA(B,player,max_depth,depth,alpha,beta):
    T=[] #T is potential moves
    moves=[]
    
    if depth==0:
        for i in AllLegalMoves(B,player):
            moves+=[AnalyzePlayer(SimulateBoard(B,i),player)]
        return [max(moves),[]] #BestMoves(moves) [N]

    elif player==10:
        value=-20000
        for i in AllLegalMoves(B,10): #i is [initial,final]
            S=SimulateBoard(B,i)
            q=AnalyzePlayer(S,10)
            if q>-6000 and q<6000:
                r=alphaBeta_general(S,20,max_depth,depth-1,-beta,-alpha) #Negative, switch and negate alpha/beta

                #val=-r[0]
                #next_tree=r[1]
                
                T+=[[i,-r[0],r[1]]] #[ [ [i,f],[] ] ]
                
                value=max(value,-r[0])
                alpha=max(value,alpha)
                if alpha >= beta:
                    break

        return [value,T] #[N,[i,[...]],[i,r]...]

    elif player==20:
        value=-20000
        for i in AllLegalMoves(B,20): #i is [initial,final]
            S=SimulateBoard(B,i)
            q=AnalyzePlayer(S,20)
            if q>-6000 and q<6000:
                r=alphaBeta_general(S,10,max_depth,depth-1,-beta,-alpha) #Negative?"""beta,alpha"""

                #val=-r[0]
                #next_tree=r[1]
                
                T+=[[i,-r[0],r[1]]] #[ [ [i,f],[] ] ]
                
                value=max(value,-r[0])
                alpha=max(value,alpha)
                if alpha >= beta:
                    break

        return [value,T] #[[i,r],[i,r]...]


