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
        row_list = [int(str_number) for str_number in row_list]
        board.append(row_list)
    return board


def check_row(board, row_to_check):
    return check_list(board[row_to_check])


def check_column(board, column_to_check):
    lst = []
    for row in range(len(board)):
        number = board[row][column_to_check]
        lst.append(number)

    return check_list(lst)


def check_square(board, top_index, left_index):
    square_size = int(len(board) ** 0.5)
    lst = []
    for row in range(top_index, top_index + square_size):
        for column in range(left_index, left_index + square_size):
            lst.append(board[row][column])
    return check_list(lst)


def check_list(lst):
    list_length = len(lst)
    counters_list = generate_counters_list(list_length)
    for number in lst:
        if number < 1 or number > list_length:
            return False
        counters_list[number - 1] += 1

    return is_counters_list_valid(counters_list)


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
