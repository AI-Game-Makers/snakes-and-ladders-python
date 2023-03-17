import pytest
from src.board import Board

def test_board_initialization():
    board = Board(size=6, num_snakes=3, num_ladders=3)

    assert board.size == 6
    assert len(board.snakes) == 3
    assert len(board.ladders) == 3

def test_board_move():
    board = Board(size=6, num_snakes=0, num_ladders=0, snakes={5: 3}, ladders={2: 4})

    assert board.move(1, 1) == 2
    assert board.move(2, 2) == 4
    assert board.move(4, 1) == 5
    assert board.move(5, 1) == 3


def test_board_is_winning_position():
    board = Board(size=6, num_snakes=0, num_ladders=0)

    assert board.is_winning_position(36) is True
    assert board.is_winning_position(35) is False
