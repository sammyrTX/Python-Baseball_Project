from baseball_functions import *

# Need overall clean up to conform with PEP 8   TODO

########################################################################################################################
#
# Baseball Game Simulator
#
# Python v3.7
#
# This is a simple simulator that runs through a baseball game. It shows the results of each at bat by team by each
# inning. Results at bat are determined at random. If there is a tie after nine innings, the game will go into extra
# innings.
#
#
# Primary goal is to use Python as the language and apply the appropriate data structures. Future features may be added
# in the future
#
########################################################################################################################


########################################################################################################################

# ***** MAIN SECTION *****

if __name__ == "__main__":

    print()
    print("*** MAIN SECTION _ START ***")

    print()
    print("=" * 70)

    # Set up batting order for a working list and copy to keep for starting at the top of the line up

    print("Set up batting order...")

    batting_lineup = [list(batting_order()), list(batting_order())]

    batting_lineup_keep = tuple(tuple(x) for x in batting_lineup)

    print("Batting order set!")

    print("=" * 70)
    print()

    print("+" * 80)

    print()
    print("*** Play Ball! ***")
    print()

########################################################################################################################

    # Innings Loop

    for current_inning in innings_tracker:
        print("-" * 50)

        print(innings_name[current_inning], "*** BEGIN ***")

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

########################################################################################################################

    # Check for a tie game after completion of nine innings

    print('*** After nine innings need to check if the score is tied. If true, continue game one inning at a time'
          ' until tie is broken ***')

    print()
    
    print_scorebox(current_inning, score_list[0], score_list[1])

    print()

    score_list[0][0] += sum(score_list[1]) - sum(score_list[0])  # TODO Force a tie to test

    print('VISITOR: {} \t HOME: {}'.format(sum(score_list[0]), sum(score_list[1])))

    print()

    # if True:
    #     score_list = [list(score_tracking_by_inning),
    #                   list(score_tracking_by_inning), ]
    #     print('score_list: {}'.format(score_list))

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

    print()

    print_scorebox(current_inning, score_list[0], score_list[1])

    print()

    print("*" * 80)

########################################################################################################################

    print()
    print("*** END OF GAME ***")
