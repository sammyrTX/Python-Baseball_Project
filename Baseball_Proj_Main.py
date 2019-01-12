from baseball_functions import *

# Need overall clean up to conform with PEP 8   TODO

# Variables & Data structures

# Variables for bases & home plate

hit_g = base1_g = base2_g = base3_g = home_plate_g = 0

bb_diamond = {'h_g': 0, 'b1_g': 0, 'b2_g': 0, 'b3_g':0}     # Possible alternate to track who is on base

# Player positions stored in a tuple

players_tuple = ("Pitcher", "Catcher", "First Base", "Second Base", "Third Base", "Shortstop", "Left Field"
                 , "Center Field", "Right Field")

# Team Roster with lists that for each player store inning, hits, RBI's

home_roster = {player: [[0, 0, 0]] for player in players_tuple}

visitor = {player: [[0, 0, 0]] for player in players_tuple}

# Innings

innings_name = ["1st Inning", "2nd Inning", "3rd Inning", "4th Inning", "5th Inning", "6th Inning", "7th Inning",
                "8th Inning", "9th Inning"]

# Pitch Result tuple

pitch_result_tuple = (('strike', 10), ('ball', 11), ('foul ball', 12), ('foul out', 13), ('out - defense', 14)
                      , ('hit - single', 1), ('hit - double', 2), ('hit - triple', 3), ('hit - homerun', 4))

# Innings tracker list by list comprehension

innings_tracker = [x for x in range(0, 9)]
# print(innings_tracker)

# Home team & Visitors score tracking

home_team_list = [0 for init_home in range(10)]

visitors_list = [0 for init_visitor in range(10)]

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

    visitors_batting_lineup = batting_order()
    hometeam_batting_lineup = batting_order()

    visitors_batting_lineup_keep = tuple(visitors_batting_lineup)
    hometeam_batting_lineup_keep = tuple(hometeam_batting_lineup)

    print("vistors batting order: {}".format(visitors_batting_lineup))
    print("home team batting order: {}".format(hometeam_batting_lineup))

    print("vistors batting order (copy): {}".format(visitors_batting_lineup_keep))
    print("home team batting order (copy): {}".format(hometeam_batting_lineup_keep))


    print()
    print("=" * 70)
    print()

    print("+" * 80)
    print("Check innings:")

    for game_inning in innings_tracker:
        print("-" * 50)
        home_team_list[game_inning] = game_inning
        visitors_list[game_inning] = game_inning
        print(innings_name[game_inning])

        # Adding steps to process pitch for Visitors; need to add steps to track player and hits  TODO
        # Add score tracking   TODO

        print()
        print("Visitors at bat:")

        outs_count = strikes_count = ball_count = foul_count = 0

        while outs_count < 3:

        # Get next batter from line up. If necessary reset line up list and start from the beginning

            if len(visitors_batting_lineup) != 0:
                batter_up = visitors_batting_lineup[0]
                visitors_batting_lineup.pop(0)
                print("At bat: {}".format(players_tuple[batter_up]))
            else:
                visitors_batting_lineup = list(visitors_batting_lineup_keep)
                batter_up = visitors_batting_lineup[0]
                visitors_batting_lineup.pop(0)
                print("At bat: {}".format(players_tuple[batter_up]))

            outs_count, strikes_count, ball_count, foul_count = process_pitch_result(pitch_result(), outs_count, strikes_count,
                                                                             ball_count, foul_count)
            print("Add process here to capture the results of the at bat and append to the team roster list")  # TODO
            print()

        print()
        print("Home at bat:")

        outs_count = strikes_count = ball_count = foul_count = 0

        while outs_count < 3:

            # Get next batter from line up. If necessary reset line up list and start from the beginning

            if len(hometeam_batting_lineup) != 0:
                batter_up = hometeam_batting_lineup[0]
                hometeam_batting_lineup.pop(0)
                print("At bat: {}".format(players_tuple[batter_up]))
            else:
                hometeam_batting_lineup = list(hometeam_batting_lineup_keep)
                batter_up = hometeam_batting_lineup[0]
                hometeam_batting_lineup.pop(0)
                print("At bat: {}".format(players_tuple[batter_up]))

            outs_count, strikes_count, ball_count, foul_count = process_pitch_result(pitch_result(), outs_count, strikes_count,
                                                                                     ball_count, foul_count)

            print("Add process here to capture the results of the at bat and append to the team roster list")  # TODO
            print()

        pass         #print_scorebox(home_team_list, visitors_list) TODO
        print("-" * 50)
        print()

    print()
    print("+" * 80)
    print("*** MAIN SECTION - END ***")
    print()

    print()

    print("Scorebox test:")
    print_scorebox(home_team_list, visitors_list)

    print()
    # ***** MAIN SECTION *****

    print("Bases in a dictionary: {}".format(bb_diamond))
    print("First Base: {}".format(bb_diamond.get('b1_g')))
    print("*" * 30)
    print()

    print("END")
    
