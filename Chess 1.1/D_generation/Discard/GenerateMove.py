from A_move.GetPieceLegalMoves import *
from B_analyze.GetPlayerPositions import *
from B_analyze.AnalyzePlayer import *

def GenerateMove(B,offset):
    legal=[]
    current=AnalyzePlayer(B,10)
    rated_moves=[]
    
    for i in range(0,63,1):
        if B[i]>=offset and B[i]<offset+6:
            legal+=GetPieceLegalMoves(B,i)
    for move in legal:
        tempBoard=list(B)
        tempBoard[move[1]]=tempBoard[move[0]]
        tempBoard[move[0]]=0
        rated_moves+=[move+[AnalyzePlayer(tempBoard,10)]]

    best_move=rated_moves[0]

    if offset==10:
        for move in rated_moves:
            if move[2]>best_move[2]:
                best_move=move
    if offset==20:
        for move in rated_moves:
            if move[2]<best_move[2]:
                best_move=move
        
    #create minimax solution!
    #Alpha-beta pruning
    return best_move

def GenerateTree(B,offset,max_level):
    """
    The purpose of GenerateTree is to look four moves ahead of each position and decide on the best move.
    
    Definitions.
        1. Player X is initial player
        2. Player O is the simulated player against X
        3. Use GetPieceLegalMoves

    Structure:
        a) Find all legal moves for Player X
            ->for positions in board, find legal moves for each X
            ->Rate each move
            ->How to decide if it goes forward?
                *Any loss of greater than 400 points is acceptable
            [initial_A, final_A, rating_A]

        b) For each of Player X's moves, find all legal moves for Player O
            ->for positions in board, find legal moves for each O
            ->Rate each move
            ->Same loss determination?
            [initial_A, final_A, rating_A, [initial_B, final_B, rating_B], [], ...]

        c) For each of O's moves, find all legal moves for Player X
            ->for positions in board, find legal moves for each X
    """

    legal=[]
    current=AnalyzePlayer(B,10)
    rated_moves=[] #[initial,final,next_score,predicted_score]
    
    for i in range(0,63,1):
        #Find all legal moves
        if B[i]>=offset and B[i]<offset+6:
            legal+=GetPieceLegalMoves(B,i)

    for move in legal:
        #Simulate and rate potential boards
        tempBoard=list(B)
        tempBoard[move[1]]=tempBoard[move[0]]
        tempBoard[move[0]]=0
        rated_moves+=[move+[AnalyzeBoard(tempBoard)]]

    best_move=rated_moves[0]

    if offset==10:
        for move in rated_moves:
            if move[2]>best_move[2]:
                best_move=move
    if offset==20:
        for move in rated_moves:
            if move[2]<best_move[2]:
                best_move=move
        
    #create minimax solution!
    #Alpha-beta pruning
    return best_move
    
        
        
            
