import copy 
import game
from math import inf as infinity

def minimax(state, depth, alpha, beta, player):

    val, winner = game.alignement(state)
    if depth == 0 or val:
        if winner == "O":
            return 10, state
        elif winner == "X":
            return -10, state
        return 0, state
    if game.gridFull(state):
        return 0, state
        
    if player == "O":
        # best = -infinity
        best_cell = None
        games = game.empty_cells(state)
        for cell in games:
            state[cell[0]][cell[1]] = player
            v, move = minimax(state, depth-1, alpha, beta, "X")
            state[cell[0]][cell[1]] = None
            if v > alpha:
                best_cell = cell
                alpha = v
            if alpha >= beta:
                break
        # print(best_cell)
        return alpha, best_cell

    best_cell = None
    games = game.empty_cells(state)
    for cell in games:
        state[cell[0]][cell[1]] = player
        v, move = minimax(state, depth-1,alpha, beta, "O")
        state[cell[0]][cell[1]] = None
        if v <= beta:
            best_cell = cell
            beta = v
        if alpha >= beta:
            break
    # print(best_cell)
    return beta, best_cell
    