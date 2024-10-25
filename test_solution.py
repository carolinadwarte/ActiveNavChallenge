# Tests for the game objetcs.
import pytest
from FizzBuzzGame import FizzBuzzGame
from BangWhizGame import BangWhizGame


@pytest.mark.parametrize(
    "test_input,expected", [(3, "Fizz"), (5, "Buzz"), (15, "FizzBuzz")]
)
def test_eval_FizzBuzzGame(test_input, expected):
    assert FizzBuzzGame().calculate_string(test_input) == expected


@pytest.mark.parametrize(
    "test_input,expected", [(4, "Bang"), (6, "Whiz"), (12, "BangWhiz")]
)
def test_eval_BangWhizGame(test_input, expected):
    assert BangWhizGame().calculate_string(test_input) == expected


@pytest.mark.parametrize("test_input,expected", [(1, 1), (50, 50), (99, 99)])
def test_eval_BangWhizGame_nonMultiples(test_input, expected):
    assert BangWhizGame().calculate_string(test_input) == expected


@pytest.mark.parametrize("test_input,expected", [(1, 1), (41, 41), (97, 97)])
def test_eval_FizzBuzzGame_nonMultiples(test_input, expected):
    assert FizzBuzzGame().calculate_string(test_input) == expected
