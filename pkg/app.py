###############################################################################

"""Baseball Game Simulator

   Python v3.7

   This is a simple simulator that runs through a baseball game. It shows
   the results of each at bat by team for each inning. Results at bat
   are determined at random. If there is a tie after nine innings, the
   game will go into extra innings.

   Primary goal is to use Python as the language and apply the appropriate
   data structures. Future features may be added.
   """

###############################################################################

# Functions

from .baseball_funcs.game_set_up import start_game

from .baseball_funcs.innings import innings_nine


# ***** MAIN SECTION *****

if __name__ == "__main__":
    # Set up batting order and start game
    batting_lineup, batting_lineup_keep = start_game()

    # Play nine innings
    innings_nine(batting_lineup, batting_lineup_keep)

    print("\n*** END OF GAME ***")
