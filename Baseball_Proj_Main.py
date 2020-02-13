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

from baseball_funcs.game_set_up import(batting_order,
                                       innings_tracker,
                                       bb_diamond,
                                       innings_half,
                                       innings_name,
                                       team_roster,
                                       score_list,
                                       start_game,
                                       )

from baseball_funcs.innings import(innings_nine,
                                   inning_process,
                                   )

from baseball_funcs.scorebox import print_scorebox


# ***** MAIN SECTION *****

if __name__ == "__main__":

    # Set up batting order and start game
    batting_lineup, batting_lineup_keep = start_game()

    # Play nine innings
    innings_nine(batting_lineup, batting_lineup_keep)

###############################################################################

    # Innings Loop - Process Nine Innings

    for current_inning in innings_tracker:

        print("-" * 50, '\n')

        inning_process_data = [current_inning,
                               bb_diamond,
                               innings_half,
                               innings_name,
                               batting_lineup,
                               batting_lineup_keep,
                               team_roster,
                               score_list,
                               ]
        (current_inning,
         bb_diamond,
         innings_half,
         innings_name,
         batting_lineup,
         batting_lineup_keep,
         team_roster,
         score_list,
         ) = inning_process(inning_process_data)

        print("-" * 50, '\n')

###############################################################################

    # Check for a tie game after completion of nine innings

    print('*** After nine innings need to check if the score is tied. If true, continue game one inning at a time'
          ' until tie is broken ***')

    print()

    print_scorebox(current_inning, score_list[0], score_list[1])

    print()

    print(f'VISITOR: {sum(score_list[0])} \t HOME: {sum(score_list[1])}', '\n')

    if sum(score_list[0]) == sum(score_list[1]):
        print('There is a tie after nine innings!')
        print('Going to extra innings...')
        print()

        # Run extra innings

        while sum(score_list[0]) == sum(score_list[1]):

            current_inning += 1
            if innings_name[current_inning] != '*** OUT OF RANGE ***':

                print(innings_name[current_inning], "*** EXTRA INNINGS BEGIN ***")

                inning_process_data = [current_inning,
                                       bb_diamond,
                                       innings_half,
                                       innings_name,
                                       batting_lineup,
                                       batting_lineup_keep,
                                       team_roster,
                                       score_list,
                                       ]
                (current_inning,
                 bb_diamond,
                 innings_half,
                 innings_name,
                 batting_lineup,
                 batting_lineup_keep,
                 team_roster,
                 score_list,
                 ) = inning_process(inning_process_data)

    print()

    print('Final Score:\n')

    print_scorebox(current_inning, score_list[0], score_list[1])

    print("*" * 50)

###############################################################################

    print("\n*** END OF GAME ***")
