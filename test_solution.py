from main import calculate_string


def test_calculate_string_m5 ():
    assert calculate_string(5) == "Buzz"

def test_calculate_string_m3 ():
    assert calculate_string(3) == "Fizz"

def test_calculate_string_m3_5 ():
    assert calculate_string(15) == "FizzBuzz"