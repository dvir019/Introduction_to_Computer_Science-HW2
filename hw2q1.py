def main():
    """
    The program gets from the user a positive number with a whole square root,
    and a squared matrix of numbers representing a sudoku board,
    checks whether or not this is a valid solution, and prints the result.
    """
    board_size = get_board_size()
    board = get_board(board_size)
    is_valid = is_board_valid(board)
    print_results(is_valid)


def get_board_size():
    """
    Gets the size of the board from the user, and returns it.

    :return: The size of the board
    :rtype: int
    """
    print("Please enter the side of the board:")
    board_size = int(input())
    return board_size


def get_board(board_size):
    """
    Gets the sudoku board from the user, and returns it as a 2D list.

    *** The user enters the board line by line, and the numbers in every line
        are separated by a space.

    :param board_size: The size of the board
    :type board_size: int

    :return: The board, as a 2D list
    :rtype: list[list[int]]
    """
    board = []
    print("Please enter a solution:")
    for row in range(board_size):
        row_string = input()
        row_list = row_string.split(' ')
        row_list = [int(str_number) for str_number in row_list]
        board.append(row_list)
    return board


def is_board_valid(board):
    """
    Checks if the whole sudoku board is valid - represents a real solution.

    :param board: The sudoku board, as a 2D list
    :type board: list[list[int]]

    :return: Whether or not the board is valid
    :rtype: bool
    """
    rows_valid = is_rows_valid(board)
    columns_valid = is_columns_valid(board)
    squares_valid = is_squares_valid(board)

    return rows_valid and columns_valid and squares_valid


def is_rows_valid(board):
    """
    Checks if all of the rows of the board are valid.

    :param board: The sudoku board, as a 2D list
    :type board: list[list[int]]

    :return: Whether or not the rows are valid
    :rtype: bool
    """
    for row_index in range(len(board)):
        if not check_row(board, row_index):
            return False
    return True


def is_columns_valid(board):
    """
    Checks if all of the columns of the board are valid.

    :param board: The sudoku board, as a 2D list
    :type board: list[list[int]]

    :return: Whether or not the columns are valid
    :rtype: bool
    """
    for column_index in range(len(board)):
        if not check_column(board, column_index):
            return False
    return True


def is_squares_valid(board):
    """
    Checks if all of the inner squares of the board are valid.

    :param board: The sudoku board, as a 2D list
    :type board: list[list[int]]

    :return: Whether or not the inner squares are valid
    :rtype: bool
    """
    board_size = len(board)
    square_size = int(board_size ** 0.5)
    for top_index in range(0, board_size, square_size):
        for left_index in range(0, board_size, square_size):
            if not check_square(board, top_index, left_index):
                return False
    return True


def check_row(board, row_to_check):
    """
    Checks if a certain row in the board is valid.

    :param board: The sudoku board, as a 2D list
    :type board: list[list[int]]
    :param row_to_check: The row to check
    :type row_to_check: int

    :return: Whether or not the row is valid
    :rtype: bool
    """
    lst = board[row_to_check]
    return check_list(lst)


def check_column(board, column_to_check):
    """
    Checks if a certain column in the board is valid.
    The method creates a list that contains the numbers of that column,
    and than checks if that list is valid.

    :param board: The sudoku board, as a 2D list
    :type board: list[list[int]]
    :param column_to_check: The row to check
    :type column_to_check: int

    :return: Whether or not the column is valid
    :rtype: bool
    """
    lst = []  # List of the numbers in the column
    for row in range(len(board)):
        number = board[row][column_to_check]
        lst.append(number)

    return check_list(lst)


def check_square(board, top_index, left_index):
    """
    Checks if a certain square in the board is valid.
    The method creates a list that contains the numbers of that square,
    and than checks if that list is valid.

    *** By using the terms "top index" and "left index",
        the 2D list is being considered as a matrix.

    :param board: The sudoku board, as a 2D list
    :type board: list[list[int]]
    :param top_index: The top index of the square
    :type top_index: int
    :param left_index: The left index of the square
    :type left_index: int

    :return: Whether or not the square is valid
    :rtype: bool
    """
    square_size = int(len(board) ** 0.5)
    lst = []  # List of the numbers in the square
    for row in range(top_index, top_index + square_size):
        for column in range(left_index, left_index + square_size):
            lst.append(board[row][column])
    return check_list(lst)


def check_list(lst):
    """
    Checks if a given list of numbers is valid.

    *** A valid list means that all of the numbers from one up to the
        length of the list (inclusive) are in the list, and each numbers
        appears only once.

    :param lst: The list of numbers
    :type lst: list[int]

    :return: Whether or not the list is valid
    :rtype: bool
    """
    list_length = len(lst)
    counters_list = generate_counters_list(list_length)
    for number in lst:
        if (number < 1) or (number > list_length):  # The number not in the interval [1, len(lst)]
            return False
        counters_list[number - 1] += 1

    return is_counters_list_valid(counters_list)


def generate_counters_list(length):
    """
    Generates a list of zeros in a certain length, and returns it.

    :param length: The length of the list
    :type length: int

    :return: The list of zeros
    :rtype: list[int]
    """
    counters_list = [0 for item in range(length)]
    return counters_list


def is_counters_list_valid(counters_list):
    """
    Checks if the counters list is valid - it contains only ones.

    :param counters_list: The counters list
    :type counters_list: list[int]

    :return: Whether or not the counters list is valid
    :rtype: bool
    """
    for counter in counters_list:
        if counter != 1:  # The number didn't appear exactly once
            return False
    return True


def print_results(is_valid):
    """
    Prints the results.

    :param is_valid: Whether or not the whole board is valid
    :type is_valid: bool
    """
    message_to_print = "Valid Solution!"  # Assume the solution is valid
    if not is_valid:  # The solution is invalid
        message_to_print = "Invalid Solution"

    print(message_to_print)


if __name__ == '__main__':
    main()
