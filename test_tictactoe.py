import pytest
from tictactoe import TicTacToe

test_game_1 = TicTacToe(3)

def test_is_legal():
    assert test_game_1.is_legal(0, 0) == True