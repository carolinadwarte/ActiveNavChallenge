import pytest
from FizzBuzzGame import FizzBuzzGame
from BangWhizGame import BangWhizGame


@pytest.mark.parametrize(
    "test_input,expected", [(3, "Fizz"), (5, "Buzz"), (15, "FizzBuzz")]
)
def test_eval_FizzBuzzGame(test_input, expected):
    game = FizzBuzzGame()
    assert game.calculate_string(test_input) == expected


@pytest.mark.parametrize(
    "test_input,expected", [(4, "Bang"), (6, "Whiz"), (12, "BangWhiz")]
)
def test_eval_BangWhiz(test_input, expected):
    game = BangWhizGame()
    assert game.calculate_string(test_input) == expected


@pytest.mark.parametrize("test_input,expected", [(0, False), (101, False)])
def test_eval_rangeCheck(test_input, expected):
    game1 = BangWhizGame()
    game2 = FizzBuzzGame()
    assert game1.rangeCheck(test_input) == expected
    assert game2.rangeCheck(test_input) == expected


@pytest.mark.parametrize("test_input,expected", [(1, True), (100, True)])
def test_eval_inRangeCheck(test_input, expected):
    game1 = BangWhizGame()
    game2 = FizzBuzzGame()
    assert game1.rangeCheck(test_input) == expected
    assert game2.rangeCheck(test_input) == expected
