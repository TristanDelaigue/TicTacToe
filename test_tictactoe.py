import pytest
from tictactoe import TicTacToe


def test_constructor():
    with pytest.raises(ValueError):
        TicTacToe(-1)

def test_is_legal():
    test_game = TicTacToe(3)
    assert test_game.is_legal(0, 0) == True
    test_game.play_at(1, 1)
    assert not test_game.is_legal(1, 1)

