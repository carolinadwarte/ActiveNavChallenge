from FizzBuzzGame import FizzBuzzGame

def test_calculate_string_m5 ():
    game = FizzBuzzGame()
    assert game.calculate_string(5) == "Buzz"

def test_calculate_string_m3 ():
    game = FizzBuzzGame()
    assert game.calculate_string(3) == "Fizz"

def test_calculate_string_m3_5 ():
    game = FizzBuzzGame()
    assert game.calculate_string(15) == "FizzBuzz"