from baseball_functions import *

# Need overall clean up to conform with PEP 8   TODO

# Variables & Data structures

# Variables for bases & home plate

hit_g = base1_g = base2_g = base3_g = home_plate_g = 0

bb_diamond = {'h_g': 0, 'b1_g': 0, 'b2_g': 0, 'b3_g':0}     # Possible alternate to track who is on base

# Player positions stored in a tuple

players_tuple = ("Pitcher", "Catcher", "First Base", "Second Base", "Third Base", "Shortstop", "Left Field"
                 , "Center Field", "Right Field")

# Teams Roster with lists that for each player stores team, inning, hits, RBI's
# List index key:
#   [0]: Team (0 - Visitors, 1 - Home)
#   [1]: Inning (0 - 8 for 1st through 9th Inning)
#   [2]: Hits (Cumulative for a player within an inning)
#   [3]: RBI (Run(s) Batted In; will ignore errors since they are not being tracked)

teams_roster = {player: [[0, 0, 0, 0]] for player in players_tuple}

# Use to flag which team is at bat Team (0 - Visitors, 1 - Home)

team_at_bat = 0

teams_description = ('VISITORS', 'HOME')

# Innings

innings_name = ["1st Inning", "2nd Inning", "3rd Inning", "4th Inning", "5th Inning", "6th Inning", "7th Inning",
                "8th Inning", "9th Inning"]

# Ball count variables

outs_count = strikes_count = ball_count = foul_count = 0

# Pitch Result tuple

pitch_result_tuple = (('strike', 10), ('ball', 11), ('foul ball', 12), ('foul out', 13), ('out - defense', 14)
                      , ('hit - single', 1), ('hit - double', 2), ('hit - triple', 3), ('hit - homerun', 4))

# Innings tracker list by list comprehension

innings_tracker = [x for x in range(0, 9)]

# Home team & Visitors score tracking

score_tracking_by_inning = [0 for init_inning in range(10)]

score_list = [list(score_tracking_by_inning), list(score_tracking_by_inning)]

# ***** MAIN SECTION *****

if __name__ == "__main__":

    print()
    print("*** MAIN SECTION _ START ***")
    print("+" * 80)

    print()
    print("=" * 70)
    print()

    # Set up batting order
    print("Set up batting order")

    batting_lineup = [list(batting_order()), list(batting_order())]

    # Store the lineup in a tuple in order start at top of the list
    batting_lineup_keep = tuple(batting_lineup)

    print("vistors batting order: {}".format(batting_lineup[0]))
    print("home batting order: {}".format(batting_lineup[1]))

    print("vistors batting order (copy): {}".format(batting_lineup_keep[0]))
    print("home batting order (copy): {}".format(batting_lineup_keep[1]))

    print()
    print("=" * 70)
    print()

    print("+" * 80)

    # Innings Loop
    for game_inning in innings_tracker:
        print("-" * 50)
        score_list[0][game_inning] = game_inning  # TODO - Remove - this tests score storage for visitors
        score_list[1][game_inning] = game_inning  # TODO - Remove - this tests score storage for home
        print(innings_name[game_inning], "*** BEGIN ***")

        # Adding steps to process pitch for Visitors; need to add steps to track player and hits  TODO
        # Add score tracking   TODO

        #  TODO Need to re-work the pitch result handling

        #    At Bat Loop - Visitors

        team_at_bat = 0

        print("{} at bat: ".format(teams_description[team_at_bat]))

        while outs_count < 3:

            # Get next batter from line up. If necessary reset line up list and start from the beginning

            team, batting_lineup, batter_up = next_batter(team_at_bat, batting_lineup, batting_lineup_keep)

            outs_count, strikes_count, ball_count, foul_count = process_pitch_result(pitch_result(), outs_count, strikes_count,
                                                                             ball_count, foul_count)
            print("Add process here to capture the results of the at bat and append to the team roster list")  # TODO
            print()

        print()
        #    At Bat Loop - Home

        team_at_bat = 1

        print("{} at bat: ".format(teams_description[team_at_bat]))

        while outs_count < 3:

            # Get next batter from line up. If necessary reset line up list and start from the beginning

            team, batting_lineup, batter_up = next_batter(team_at_bat, batting_lineup, batting_lineup_keep)

            outs_count, strikes_count, ball_count, foul_count = process_pitch_result(pitch_result(), outs_count, strikes_count,
                                                                                     ball_count, foul_count)

            print("Add process here to capture the results of the at bat and append to the team roster list")  # TODO
            print()

        print(innings_name[game_inning], "*** END ***")
        print("-" * 50)
        print()

    print()
    print("+" * 80)
    print("*** MAIN SECTION - END ***")
    print()

    print()

    print("Scorebox test:")
    print_scorebox(score_list[0], score_list[1])

    print()
    # ***** MAIN SECTION *****

    print("Bases in a dictionary: {}".format(bb_diamond))
    print("First Base: {}".format(bb_diamond.get('b1_g')))
    print("*" * 30)
    print()

    print("END")
    
