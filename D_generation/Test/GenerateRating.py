from AnalyzePlayer import *
from GetPieceLegalMoves import *
from GetPlayerPositions import *

#***COPY BELOW
def alphaBeta_general(B,player,max_depth,depth,alpha,beta):
    #
    T=[] #T is potential moves
    move=0

    if depth==0: #Minimize score
        moves=[]
        for i in AllLegalMoves(B,player):
            moves+=[AnalyzePlayer(SimulateBoard(B,i),player)]
        return max(moves)

    elif player==10:
        value=-20000
        for i in AllLegalMoves(B,10): #i is [initial,final]
            T+=[[i,alphaBeta_general(SimulateBoard(B,i),20,3,depth-1,alpha,beta)]]

            value=max(value,alphaBeta_general(SimulateBoard(B,i),20,3,depth-1,beta,alpha))
            alpha=max(value,alpha)
            if alpha >= beta:
                break

        if depth==max_depth:
            #print(T)
            #return T #DEL
            maxm=[T[0]]
            for i in T:
                if i[1]>maxm[0][1]:
                    maxm=[i]
                elif maxm[0][1]==i[1]:
                    maxm+=i
            return maxm
        else:
            max_num=T[0][1]
            for i in T:
                if i[1]>max_num:
                    max_num=i[1]
            return max_num
        
    elif player==20:
        for i in AllLegalMoves(B,20): #i is [initial,final]
            T+=[[i,-GenerateTree_Four(SimulateBoard(B,i),10,depth-1)]]

        if depth==max_depth:
            print(T)
            #return T #DEL
            maxm=[T[0]]
            for i in T:
                if i[1]>maxm[0][1]:
                    maxm=[i]
                elif maxm[0][1]==i[1]:
                    maxm+=i
            return maxm
        else:
            max_num=T[0][1]
            for i in T:
                if i[1]>max_num:
                    max_num=i[1]
            return max_num


def SimulateBoard(B,move): #[board,move]->[new_board]
    temp=list(B)
    temp[move[1]]=temp[move[0]]
    temp[move[0]]=0

    if temp[move[1]]==10 and move[1]<8:
        temp[move[1]]=14
    elif temp[move[1]]==20 and move[1]>55:
        temp[move[1]]=24

    return temp
