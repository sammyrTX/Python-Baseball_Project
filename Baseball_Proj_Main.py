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

# Team Roster with lists that for each player stores team, inning, hits, RBI's
#
# List index key:
#   [0]: Team (0 - Visitors, 1 - Home)
#   [1]: Player Position
#   [2]: Inning (0 - 8 for 1st through 9th Inning)
#   [3]: Hits (Cumulative for a player within an inning)
#   [4]: Runs Scored
#   [5]: RBI (Run(s) Batted In; will ignore errors since they are not being tracked)

team_roster = {player: [] for player in players_tuple}

# print("Teams Roster: \n {}".format(teams_roster))   # TODO For testing

# Use to flag which team is at bat Team (0 - Visitors, 1 - Home)

team_at_bat = 0

team_description = ('VISITORS', 'HOME')

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

innings_tracker = [x for x in range(0, 2)]  # 9)]    #  TODO Testing - Set innings to just 3

# Home team & Visitors score tracking

score_tracking_by_inning = [0 for init_inning in range(9)]

score_list = [list(score_tracking_by_inning),
              list(score_tracking_by_inning), ]

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

    # print("vistors batting order: {}".format(batting_lineup[0]))     # TODO clean up
    # print("home batting order: {}".format(batting_lineup[1]))       # TODO clean up
    #
    # print("vistors batting order (copy): {}".format(batting_lineup_keep[0]))    # TODO clean up
    # print("home batting order (copy): {}".format(batting_lineup_keep[1]))       # TODO clean up

    print("=" * 70)
    print()

    print("+" * 80)

    print()
    print("*** Start Game! ***")
    print()

########################################################################################################################

    # Innings Loop
    for current_inning in innings_tracker:
        print("-" * 50)

        print(innings_name[current_inning], "*** BEGIN ***")

        team_at_bat = 0
        outs_m = 0
        balls_m = 0
        strikes_m = 0
        fouls_m = 0

        bb_diamond = {base: 0 for base in bb_diamond}

        print("Top of the Inning: {} at bat".format(team_description[team_at_bat]))

        while outs_m < 3:

            team_at_bat, batting_lineup, batter_up_m = next_batter(team_at_bat, batting_lineup, batting_lineup_keep)
            print('\t','* Up to bat for {}: {} *'.format(team_description[team_at_bat], players_tuple[batter_up_m]))

            while True:
                print('\t','At bat for {}: {}'.format(team_description[team_at_bat], players_tuple[batter_up_m]))

                print()

                # For this section, need the following:  TODO  Add the following processes
                #     - pitch result - DONE
                #     - process the result - DONE
                #     - Advance Runner  - DONE
                #     - Tally Strikes, Balls, Fouls, etc. - DONE
                #     - If a Hit, record bases status and tally runs batted in - In Progress
                #        * Focusing on Pitch Process, Advance Runner & Main to handle runner and any scoring batted in

                # This while loop is for testing  TODO Testing
                # while strikes_m < 3:
                #     strikes_m += 1
                # else:
                #     strikes_m = 0
                #     outs_m += 1
                #     print("OUT!")

                outs_pre = int(outs_m)  # TODO Keep if best method to catch outs and proceed to next batter
                pitch_result_m, outs_m, strikes_m, balls_m, fouls_m, bb_diamond = process_pitch_result(pitch_result(),
                                                                                                       outs_m,
                                                                                                       strikes_m,
                                                                                                       balls_m,
                                                                                                       fouls_m,
                                                                                                       bb_diamond,
                                                                                                       )
                if outs_m > outs_pre:

                    print('Batter is out...go to next batter')
                    print('Clear Ball Count')

                    strikes_m = 0
                    balls_m = 0
                    fouls_m = 0

                    bases_picture(bb_diamond)

                    break

                if pitch_result_m[0] in ('strike', 'ball', 'foul ball'):

                    if pitch_result_m[0] == 'ball' and pitch_result_m[1] == 44:
                        # Batter was walked, tally home_plate if there was a score, init and then break for next batter

                        team_roster[players_tuple[batter_up_m]].append([team_at_bat,
                                                                        batter_up_m,
                                                                        current_inning,
                                                                        0,
                                                                        bb_diamond['h_g'],
                                                                        bb_diamond['h_g']])

                        print('*** Batter is walked, init ball count, break and go to next batter')

                        print('Clear Ball Count')
                        strikes_m = 0
                        balls_m = 0
                        fouls_m = 0

                        bases_picture(bb_diamond)

                        break

                    print('Show batter count')
                    print()
                    ball_count_print(outs_m,
                                     strikes_m,
                                     balls_m,)
                    continue

                if pitch_result_m[1] in range(1, 5):

                    bases_picture(bb_diamond)

                    # Process hit if there is no run batted in  TODO Tally hit (no score) by team, player & inning
                    if bb_diamond['h_g'] == 0:
                        print('*** TEST *** (Hit, but no runs batted in: \n')

                        print([team_at_bat, batter_up_m, current_inning, 1, bb_diamond['h_g'], bb_diamond['h_g']])


                        team_roster[players_tuple[batter_up_m]].append([team_at_bat,
                                                                        batter_up_m,
                                                                        current_inning,
                                                                        22,    # reset to 1 after review
                                                                        bb_diamond['h_g'],
                                                                        bb_diamond['h_g']])

                    # Process any hits that resulted in a run batted in ***  TODO Tally score by team, player & inning
                    if bb_diamond['h_g'] != 0:
                        print('In main : If a run is batted or walked in, need to append to teams roster')
                        print('*** HERE IS WHERE A RUN IS SCORED >>> bb_diamond[h_g] = {}'.format(bb_diamond['h_g']))
                        print('*** Add Process here to tally score >>> bb_diamond[h_g] = {}'.format(bb_diamond['h_g']))

                        # Add runs to score list

                        score_list[team_at_bat][current_inning] += bb_diamond['h_g']

                    # Pass player and results data to teams roster list and any runs scored. Clear Home Plate after
                    # runs nd RBI's recorded

                        # Use function below to add data to teams roster

                        print('*** TEST ***: \n')

                        print([team_at_bat, batter_up_m, current_inning, 1, bb_diamond['h_g'], bb_diamond['h_g']])

                        print('team roster before append: {}'.format(team_roster[players_tuple[batter_up_m]]))

                        team_roster[players_tuple[batter_up_m]].append([team_at_bat,   # TODO Should be only append
                                                                        batter_up_m,
                                                                        current_inning,
                                                                        99,
                                                                        bb_diamond['h_g'],
                                                                        bb_diamond['h_g']])

                        print('team roster after append: {}'.format(team_roster[players_tuple[batter_up_m]]))

                        # Reset home plate
                        bb_diamond['h_g'] = 0

                        print('*** After runs recorded, clear home plate >>> bb_diamond[h_g] = {}'
                              .format(bb_diamond['h_g']))


                    print('Clear Ball Count')

                    strikes_m = 0
                    balls_m = 0
                    fouls_m = 0

                    print('Go to next batter')
                    break

                print('*** WHEN DOES THE FOLLOWING PRINT???***')
                ball_count_print(outs_m,
                                 strikes_m,
                                 balls_m,)

        print("Last Out Count: {}".format(outs_m))
        print(">>>>>>>>>>")

########################################################################################################################

        team_at_bat = 1
        outs_m = 0
        balls_m = 0
        strikes_m = 0

        bb_diamond = {base: 0 for base in bb_diamond}

        print("Bottom of the Inning: {} at bat".format(team_description[team_at_bat]))

        while outs_m < 3:
            print("Out count: {}".format(outs_m))
            outs_m += 1

        print("Last Out Count: {}".format(outs_m))

        print(innings_name[current_inning], "*** END ***")

        print()
        print('*** Home at bat to be updated after Visitors section is completed ***')
        print("-" * 50)
        print()

    # Need to add check after innings if the score is tied. Need to continue game one inning at a time until one team
    # has a score greater than the other.  TODO  Add check for Tie at end of nine innings

########################################################################################################################

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
    print("Scorebox test:")
    print_scorebox(score_list[0], score_list[1])

    print()

    # This section tests the teams roster   TODO Remove Section below after testing

    print('Visitors data team roster  *** PENDING ***')

    team_roster_score_summ = [[0], [0]]

    for team_aggregate in range(0,2):
        print('team idx:', team_aggregate)

        for roster_ in team_roster:
            print('roster_player: ', roster_)
            for roster_2 in iter(team_roster[roster_]):
                print('roster_2: {}'.format(roster_2))
                if roster_2[0] == team_aggregate:
                    print('roster_2[0]: {}'.format(roster_2[0]))
                    print('roster_2[4]: {}'.format(roster_2[4]))
                    team_roster_score_summ[team_aggregate].append(roster_2[4])

    print('team_roster_score_summ: {}'.format(team_roster_score_summ))
    for chk in iter(team_roster_score_summ):
        print('chk: {}, sum(chk): {}'.format(chk, sum(chk)))


    print('Current data stored in team_roster: \n{}'.format(team_roster))



    # This section tests the the bases dictionary   TODO Remove Section below after testing

    # print("Bases in a dictionary: {}".format(bb_diamond))
    # print("First Base: {}".format(bb_diamond.get('b1_g')))
    # print("*" * 30)
    # print()
