def calculate_initial_guests(yells):
    """
    Calculate the initial number of guests based on the number of yells.

    Args:
    yells (int): The number of times the board member yells.

    Returns:
    int: The initial number of guests.
    """
    # Start with 0 guests and reverse the process
    guests = 0

    # Reverse the process for each yell
    for _ in range(yells):
        # Before the last yell, the number of guests was twice the number after the yell plus one
        guests = 2 * (guests + 0.5)

    return int(guests)

n = int(input())
for i in range(n):
    yells = int(input())
    print(calculate_initial_guests(yells))