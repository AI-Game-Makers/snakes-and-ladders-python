import pytest
from src.player import Player

def test_player_initialization():
    player = Player("Alice")

    assert player.name == "Alice"
    assert player.get_position() == 1

def test_player_move():
    player = Player("Bob")

    player.move(3)
    assert player.get_position() == 4

def test_player_set_position():
    player = Player("Carol")

    player.set_position(10)
    assert player.get_position() == 10
