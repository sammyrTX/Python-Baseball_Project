"""Scorebox function - code to build the scorebox during the game.
"""


def print_scorebox(current_inning_f, visitors_list, home_list):
    """Generates a score box of nine innings along with the number of total
       runs for the game"""

    current_inning_f += 1

    # if less than nine innings show values for all nine innings
    if current_inning_f < 9:
        current_inning_f = 9

    print('INNING  ', end='')

    for inning_counter in range(0, current_inning_f):
        print(f'  {(inning_counter + 1):2}', end='')

    print('   R', end='')

    print()

    print('------  ', end='')

    for inning_counter in range(0, current_inning_f):
        print('  --', end='')

    print('  --', end='')

    print()

    print('VISITORS', end='')

    for inning_counter in range(0, current_inning_f):
        print(f'  {(visitors_list[inning_counter]):2}', end='')

    print(f'  {(sum(visitors_list)):2}', end='')

    print()

    print('HOME    ', end='')

    for inning_counter in range(0, current_inning_f):
        print(f'  {(home_list[inning_counter]):2}', end='')

    print(f'  {(sum(home_list)):2}', end='')

    print('\n\n')
