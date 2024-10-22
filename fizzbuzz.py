def calculate_string(num: int):
    """ Return input if not modication would be made, returns string otherwise """
    multipleOf3 = num % 3 == 0
    multipleOf5 = num % 5 == 0
    match num:
        #the first condition checks if num is multiple of both 3 and 5 before checking individually
        case _ if multipleOf3 and multipleOf5:
            return "FizzBuzz"
        case _ if multipleOf3:
            return "Fizz"
        case _ if multipleOf5:
            return "Buzz" 
        case _:
            return num