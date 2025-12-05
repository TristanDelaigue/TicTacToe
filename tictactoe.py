import numpy as np


class TicTacToe():
    
    def __init__(self, size):
        self.size = size
        self.board = np.array([[0 for _ in range(size)] for _ in range(size)])
        self.current_player = 1
        self.winner = 0
    
    def is_over(self):
        return self.winner > 0

    def is_legal(self, i, j):
        return self.board[i, j] == 0
    
    def check_victory(self, i, j):
        
        # vertical check
        tmp = True
        for k in range(self.size):
            if self.board[k, j] != self.current_player:
                tmp = False
                break
        if tmp:
            self.winner = self.current_player
            return True
        
        # horizontal check
        tmp = True
        for k in range(self.size):
            if self.board[i, k] != self.current_player:
                tmp = False
                break
        if tmp:
            self.winner = self.current_player
            return True
        
        # diagonal check
        if i == j or i == self.size - j - 1:
            
            # first diagonal
            tmp = True
            for k in range(self.size):
                if self.board[k, k] != self.current_player:
                    tmp = False
                    break
            if tmp:
                self.winner = self.current_player
                return True
            
            # second diagonal
            tmp = True
            for k in range(self.size):
                if self.board[k, k] != self.current_player:
                    tmp = False
                    break
            if tmp:
                self.winner = self.current_player
                return True
        
        return False


    def play_at(self, i, j):
        if self.is_legal(i, j):
            self.board[i, j] = self.current_player
            self.check_victory(i, j)
            self.current_player = 3 - self.current_player


if __name__ == "__main__":
    game = TicTacToe(3)
    game.play_at(0, 0)