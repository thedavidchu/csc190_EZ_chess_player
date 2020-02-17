from A_move.GetPieceLegalMoves import *

from B_analyze.AnalyzePlayer import *
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

    if temp[move[1]]==10 and move[1]>55:
        temp[move[1]]=14
    elif temp[move[1]]==20 and move[1]<8:
        temp[move[1]]=24

    return temp

"""
Goal:
->Return Level-ordered Traversal of the tree

Verdict:
->Create for loop to make new list for each level
->Use depth to determine which bucket it goes into
        [level_0], [level_1], ...[level_N]
->Concatenate at the end

>>>Too complicated to implement

"""

def alphaBeta_general(B,player,max_depth,depth,alpha,beta):
    T=[] #T is potential moves
    N=[] #Level-ordered traversal
    moves=[]
    
    if depth==0:
        for i in AllLegalMoves(B,player):
            moves+=[AnalyzePlayer(SimulateBoard(B,i),player)]
        return [max(moves),[],[]] #BestMoves(moves) [N]

    elif player==10:
        value=-20000
        q=AnalyzePlayer(B,10)
        if q>-6000 and q<6000:
            for i in AllLegalMoves(B,10): #i is [initial,final]
                S=SimulateBoard(B,i)
            
                """q>-6000 and q<6000"""
                r=alphaBeta_general(S,20,max_depth,depth-1,-beta,-alpha) #Negative, switch and negate alpha/beta

                #val=-r[0]
                #next_tree=r[1]
                #pre_next_tree=r[2]

                T+=[[i,-r[0]]] #[ [ [i,f],[] ] ]
                
                N+=r[1]
                N+=r[2]
                
                value=max(value,-r[0])
                alpha=max(value,alpha)
                if alpha >= beta:
                    break
            
            #else:
            #value==q
            #T=[[],q,[]]
                

        return [value,T,N] #[ val, [ [i,],[i,r]...] ], [...]

    elif player==20:
        value=-20000
        q=AnalyzePlayer(B,20)
        if q>-6000 and q<6000:
            for i in AllLegalMoves(B,20): #i is [initial,final]
                S=SimulateBoard(B,i)
        
                r=alphaBeta_general(S,10,max_depth,depth-1,-beta,-alpha) #Negative?"""beta,alpha"""

                #val=-r[0]
                #next_tree=r[1]
                
                T+=[[i,-r[0],r[1]]] #[ [ [i,f],[] ] ]
                
                value=max(value,-r[0])
                alpha=max(value,alpha)
                if alpha >= beta:
                    break
            
        else:
            value==q
            T=[[],q,[]]

        return [value,T]


