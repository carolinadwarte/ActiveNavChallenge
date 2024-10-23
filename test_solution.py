from FizzBuzzGame import FizzBuzzGame
from BangWhizGame import BangWhizGame


def test_calculate_string_m4():
    game = BangWhizGame()
    assert game.calculate_string(4) == "Bang"


def test_calculate_string_m6():
    game = BangWhizGame()
    assert game.calculate_string(6) == "Whiz"


def test_calculate_string_m4_6():
    game = BangWhizGame()
    assert game.calculate_string(12) == "BangWhiz"


def test_calculate_string_m5():
    game = FizzBuzzGame()
    assert game.calculate_string(5) == "Buzz"


def test_calculate_string_m3():
    game = FizzBuzzGame()
    assert game.calculate_string(3) == "Fizz"


def test_calculate_string_m3_5():
    game = FizzBuzzGame()
    assert game.calculate_string(15) == "FizzBuzz"
