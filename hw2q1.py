def main():
    board_size = get_board_size()
    board = get_board(board_size)
    is_valid = is_board_valid(board)


def get_board_size():
    board_size = int(input("Please enter the side of the board:"))
    return board_size


def get_board(board_size):
    board = []
    for row in range(board_size):
        row_string = input()
        row_list = row_string.split(' ')
        row_list=[int(str_number) for str_number in row_list]
        board.append(row_list)

def check_row(board, row_to_check):
    row_length = len(board[row_to_check])
    counters_list = generate_counters_list(row_length)
    for number in board[row_to_check]:
        if number < 1 or number > row_length:
            break
        counters_list[number - 1] += 1
    else:
        return is_counters_list_valid(counters_list)
    return False


def generate_counters_list(length):
    counters_list = [0 for item in range(length)]
    return counters_list


def is_counters_list_valid(counters_list):
    for counter in counters_list:
        if counter != 1:
            return False
    return True


if __name__ == '__main__':
    main()
