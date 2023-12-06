import random
import time
def create_initial_board(p, q):
    """
    Create the initial board with a checkerboard pattern.
    
    :param p: Number of rows.
    :param q: Number of columns.
    :return: A 2D list representing the board.
    """
    return [['D' if (row + col) % 2 == 0 else 'W' for col in range(q)] for row in range(p)]

def calculate_happiness_with_board(board, player, break_off):
    """
    Calculate the happiness and new board after a player's move.

    :param board: A 2D list representing the current board.
    :param player: 'Erik' or 'Collin', indicating the current player.
    :param break_off: Number of columns/rows to break off.
    :return: A tuple containing the happiness score for the move and the new board.
    """
    p, q = len(board), len(board[0]) if board else 0
    happiness = 0
    new_board = [row.copy() for row in board]  # Copy the current board

    if player == 'Erik':
        # Erik breaks off columns from the west side
        for row in range(p):
            for col in range(break_off):
                happiness += 1 if board[row][col] == 'D' else -1
        new_board = [row[break_off:] for row in new_board]  # Remove the broken off columns
    elif player == 'Collin':
        # Collin breaks off rows from the south side
        for row in range(p - break_off, p):
            for col in range(q):
                happiness += 1 if board[row][col] == 'D' else -1
        new_board = new_board[:-break_off]  # Remove the broken off rows

    return happiness, new_board if new_board and new_board[0] else []

def minimax_with_board_and_happiness(board, is_erik_turn, current_happiness, alpha=-float('inf'), beta=float('inf')):
    """
    Implement the minimax algorithm with board state and happiness tracking.

    :param board: A 2D list representing the current board.
    :param is_erik_turn: A boolean indicating if it is Erik's turn.
    :param current_happiness: The current difference in happiness between Erik and Collin.
    :param alpha: Alpha value for alpha-beta pruning.
    :param beta: Beta value for alpha-beta pruning.
    :return: The best score that can be achieved from the current state.
    """
    p, q = len(board), len(board[0]) if board else 0

    # Base case: if the game is over (board size is 0x0)
    if p == 0 or q == 0:
        return current_happiness

    if is_erik_turn:
        max_eval = -float('inf')
        for break_off in range(1, q + 1):
            happiness, new_board = calculate_happiness_with_board(board, 'Erik', break_off)
            eval = minimax_with_board_and_happiness(new_board, False, current_happiness + happiness, alpha, beta)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for break_off in range(1, p + 1):
            happiness, new_board = calculate_happiness_with_board(board, 'Collin', break_off)
            eval = minimax_with_board_and_happiness(new_board, True, current_happiness - happiness, alpha, beta)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

def is_odd(n):
    return n % 2 == 1

def is_even(n):
    return n % 2 == 0

def manual(p, q):
    if is_odd(p) and is_odd(q):
        return 1
    if is_even(p) and (is_even(q) or is_odd(q)):
        return 0
    
    if p > q:
        return 0
    else:
        return 2

# # Testing the function with the provided sample inputs
# initial_board_1_9 = create_initial_board(5, 6)
# initial_board_2_4 = create_initial_board(2, 4)
# initial_board_7_10 = create_initial_board(7, 10)

# print("Sample Input 1 (1, 9):", minimax_with_board_and_happiness(initial_board_1_9, True, 0))
# print("Sample Input 2 (2, 4):", minimax_with_board_and_happiness(initial_board_2_4, True, 0))
# print("Sample Input 3 (7, 10):", minimax_with_board_and_happiness(initial_board_7_10, True, 0))
# print(minimax_with_board_and_happiness(initial_board_1_9, True, 0))
def generate_random_board(max_size=10):
    """
    Generate a random board with a maximum size.

    :param max_size: The maximum size for the board dimensions.
    :return: A 2D list representing a randomly generated board.
    """
    p = random.randint(1, max_size)
    q = random.randint(1, max_size)
    return create_initial_board(p, q), p, q

def test_runtime(max_size=10, num_tests=10):
    """
    Test the runtime of the minimax algorithm on randomly generated boards.

    :param max_size: The maximum size for the board dimensions in the test.
    :param num_tests: The number of tests to run.
    :return: None. Prints out the results of each test.
    """
    for _ in range(num_tests):
        board, p, q = generate_random_board(max_size)
        start_time = time.time()
        res = minimax_with_board_and_happiness(board, True, 0)
        end_time = time.time()
        runtime = end_time - start_time
        print(f"Board Size: {len(board)}x{len(board[0])}, Runtime: {runtime:.2f} seconds, Below 1 second: {'Yes' if runtime < 1 else 'No'}")
        # test whether res equals manual
        assert res == manual(p, q), f"p{p}, q{q}, res{res}, manual{manual(p, q)}"


        if runtime >= 1:
            break

# Run the test function
test_runtime(12, 10_000)
# initial_board_1_9 = create_initial_board(15, 15)
# print(minimax_with_board_and_happiness(initial_board_1_9, True, 0))
