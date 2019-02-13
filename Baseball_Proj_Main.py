from baseball_functions import *

# Need overall clean up to conform with PEP 8   TODO

# Variables & Data structures

# Variables for bases & home plate

hit_g = base1_g = base2_g = base3_g = home_plate_g = 0

bb_diamond = {'h_g': 0,
              'b1_g': 0,
              'b2_g': 0,
              'b3_g': 0,
              }     # Possible alternate to track who is on base

# Player positions stored in a tuple

players_tuple = ("Pitcher",
                 "Catcher",
                 "First Base",
                 "Second Base",
                 "Third Base",
                 "Shortstop",
                 "Left Field",
                 "Center Field",
                 "Right Field",)

# Teams Roster with lists that for each player stores team, inning, hits, RBI's
#
# List index key:
#   [0]: Team (0 - Visitors, 1 - Home)
#   [1]: Player Position
#   [2]: Inning (0 - 8 for 1st through 9th Inning)
#   [3]: Hits (Cumulative for a player within an inning)
#   [4]: Runs Scored
#   [5]: RBI (Run(s) Batted In; will ignore errors since they are not being tracked)

teams_roster = {player: [] for player in players_tuple}

# print("Teams Roster: \n {}".format(teams_roster))   # TODO For testing

# Use to flag which team is at bat Team (0 - Visitors, 1 - Home)

team_at_bat = 0

teams_description = ('VISITORS', 'HOME')

# Innings

innings_name = ["1st Inning",
                "2nd Inning",
                "3rd Inning",
                "4th Inning",
                "5th Inning",
                "6th Inning",
                "7th Inning",
                "8th Inning",
                "9th Inning", ]

# Ball count variables

outs_count = strikes_count = ball_count = foul_count = 0

# Pitch Result tuple

pitch_result_tuple = (('strike', 10),
                      ('ball', 11),
                      ('foul ball', 12),
                      ('foul out', 13),
                      ('out - defense', 14),
                      ('hit - single', 1),
                      ('hit - double', 2),
                      ('hit - triple', 3),
                      ('hit - home run', 4),)

# Innings tracker list by list comprehension

innings_tracker = [x for x in range(0, 9)]

# Home team & Visitors score tracking

score_tracking_by_inning = [0 for init_inning in range(9)]

score_list = [list(score_tracking_by_inning),
              list(score_tracking_by_inning), ]

# ***** MAIN SECTION *****

if __name__ == "__main__":

    print()
    print("*** MAIN SECTION _ START ***")
    # print("+" * 80)  TODO REMOVE

    print()
    print("=" * 70)
    print()

    # Set up batting order for a working list and copy to keep for starting at the top of the line up
    print("Set up batting order")

    batting_lineup = [list(batting_order()), list(batting_order())]

    batting_lineup_keep = tuple(tuple(x) for x in batting_lineup)

    # print("vistors batting order: {}".format(batting_lineup[0]))     # TODO clean up
    # print("home batting order: {}".format(batting_lineup[1]))       # TODO clean up
    #
    # print("vistors batting order (copy): {}".format(batting_lineup_keep[0]))    # TODO clean up
    # print("home batting order (copy): {}".format(batting_lineup_keep[1]))       # TODO clean up

    print()
    print("=" * 70)
    print()

    print("+" * 80)

    print()
    print("*** Start Game! ***")
    print()

    # Innings Loop
    for game_inning in innings_tracker:
        print("-" * 50)
        # score_list[0][game_inning] = game_inning  # TODO - Remove - this tests score storage for visitors
        # score_list[1][game_inning] = game_inning  # TODO - Remove - this tests score storage for home

        print(innings_name[game_inning], "*** BEGIN ***")

        print("Top of the Inning: Visitors at bat")

        team_at_bat = 0
        outs_m = 0
        balls_m = 0
        strikes_m = 0

        while outs_m < 3:
            print("Out count: {}".format(outs_m))
            print("Strikes count: {}".format(strikes_m))
            print("Balls count: {}".format(balls_m))

            print()

            print("len of line up list before get next batter: {}".format(len(batting_lineup[team_at_bat]))) # TODO Remove
            print("len(batting_lineup_f[team_f]) != 0 : {}".format((batting_lineup[team_at_bat]) != 0))
            print("^^^")

            team_at_bat, batting_lineup, batter_up_m = next_batter(team_at_bat, batting_lineup, batting_lineup_keep)

            print("Batter up: {}".format(players_tuple[batter_up_m]))

            print()
            print("Strikes: {}, Outs: {}".format(strikes_m, outs_m))

            print("len of line up list AFTER get next batter: {}".format(len(batting_lineup[team_at_bat]))) # TODO Remove

            print("^^^")

            while strikes_m < 3:
                strikes_m += 1
            else:
                strikes_m = 0
                outs_m += 1
                print("OUT!")

            ball_count_print(outs_m, strikes_m, balls_m)

            # v_outs += 1

        print("Last Out Count: {}".format(outs_m))
        print(">>>>>>>>>>")

        print("Bottom of the Inning: Home at bat")

        team_at_bat = 1
        outs_m = 0
        balls_m = 0
        strikes_m = 0

        while outs_m < 3:
            print("Out count: {}".format(outs_m))
            outs_m += 1

        print("Last Out Count: {}".format(outs_m))

        print(innings_name[game_inning], "*** END ***")

        print("-" * 50)
        print()

    # Need to add check after innings if the score is tied. Need to continue game one inning at a time until one team
    # has a score greater than the other.  TODO  Add check for Tie at end of nine innings

    print('*** After nine innings need to check if the score is tied. If true, continue game one inning at a time'
          ' until tie is broken ***')
    print()
    print("*** END OF GAME ***")
    print()

    print("+" * 80)
    print("*** MAIN SECTION - END ***")
    print()

    # ***** MAIN SECTION *****

    # This section tests the scorebox   TODO Remove Section below after testing
    # print("Scorebox test:")
    # print_scorebox(score_list[0], score_list[1])
    #
    # print()

    # This section tests the the bases dictionary   TODO Remove Section below after testing

    # print("Bases in a dictionary: {}".format(bb_diamond))
    # print("First Base: {}".format(bb_diamond.get('b1_g')))
    # print("*" * 30)
    # print()
