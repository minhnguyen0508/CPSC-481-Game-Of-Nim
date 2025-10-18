from games import *

class GameOfNim(Game):
    """Play Game of Nim with first player 'MAX'.
    A state has the player to move, a cached utility, a list of moves in
    the form of a list of (x, y) positions, and a board, in the form of
    a list with number of objects in each row."""

    def __init__(self, board=[3,1]):
        self.board = board
        moves=[]
        for idx, move in enumerate(board):
            if move != 0:
                i = 1
                while i <= move:
                    moves.append((idx, i))
                    i+=1
        self.initial = GameState(to_move = 'MIN',utility = 0, board=board ,moves=moves) 

    def actions(self, state):
        """Legal moves are at least one object, all from the same row."""

        return state.moves

    def result(self, state, move):
        if move not in state.moves:
            return state
        board =state.board.copy()
        moves = list(state.moves)
        moves.remove(move)
        x = move[0]     #(1,3) ==> x =1
        y = move[1]     #y = 3
        board[x]-= y
        if(board[x] < 0):
            board[x] =0
        return GameState(to_move=('MIN' if state.to_move == 'MAX' else 'MAX'),
                         utility=0,
                         board=board, moves=moves)


    def utility(self, state, player):
        """Return the value to player; 1 for win, -1 for loss, 0 otherwise."""
        return state.utility if player == 'MAX' else -state.utility
    def terminal_test(self, state):
        """A state is terminal if there are no objects left"""
        return state.utility != 0 or len(state.moves) == 0
    

    def display(self, state):
        board = state.board
        print("board: ", board)


if __name__ == "__main__":
    nim = GameOfNim(board=[0, 5, 3, 1]) # Creating the game instance
    #nim = GameOfNim(board=[7, 5, 3, 1]) # a much larger tree to search
    print(nim.initial.board) # must be [0, 5, 3, 1]
    print(nim.initial.moves) # must be [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 2), (2, 3), (3, 1)]
    print(nim.result(nim.initial, (1,3) ))
    utility = nim.play_game(alpha_beta_player, query_player) # computer moves first 
    if (utility < 0):
        print("MIN won the game")
    else:
        print("MAX won the game")
