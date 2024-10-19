
def calculate_string(num: int):
    """ Return input if not modication would be made, returns string otherwise """
    match num % 10:
        case 0 | 5:
            return "Buzz"
        case _:
            return num


if __name__ == "__main__":
    """ Code inside this closure will only run if this file is called directly """
    print("Program start")

    for num in range(1, 101):
        print(calculate_string(num))
