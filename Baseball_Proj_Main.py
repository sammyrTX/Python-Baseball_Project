from baseball_functions import *

# Need overall clean up to conform with PEP 8   TODO

# Variables & Data structures

# Variables for bases & home plate

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
                "9th Inning",
                "10th Inning",
                "11th Inning",
                "12th Inning",
                "13th Inning",
                "14th Inning",
                "15th Inning",
                "16th Inning",
                "17th Inning",
                "18th Inning",
                "19th Inning",
                "20th Inning",
                "21st Inning",
                "22nd Inning",
                "23rd Inning",
                "24th Inning",
                "25th Inning",
                "26th Inning",
                "27th Inning",
                "28th Inning",
                "29th Inning",
                "30th Inning",
                "*** OUT OF RANGE ***",
                ]

innings_half = ['Top', 'Bottom']

# Pitch Result tuple

pitch_result_tuple = (('strike', 10, 'Strike!',),
                      ('ball', 11, 'Ball!',),
                      ('foul ball', 12, 'Foul Ball!',),
                      ('foul out', 13, 'Out!',),
                      ('out - defense', 14, 'Out!',),
                      ('hit - single', 1, 'Hit! A Single',),
                      ('hit - double', 2, 'Hit! A Double',),
                      ('hit - triple', 3, 'Hit! A Triple',),
                      ('hit - home run', 4, 'Home run!!!',),)

# Innings tracker list by list comprehension

innings_tracker = [x for x in range(0, 9)]  # 9)]    #  TODO Testing - Set innings to just 3

# Home team & Visitors score tracking

score_tracking_by_inning = [0 for init_inning in range(30)]  # Setting to max of 30 innings in extra innings

score_list = [list(score_tracking_by_inning),
              list(score_tracking_by_inning), ]

score_list_team_roster = [list(score_tracking_by_inning),
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

        # Original code in Main  TODO Remove this section once function is working
        # for team_at_bat in range(0, 2):
        #
        #     outs_m = 0
        #     balls_m = 0
        #     strikes_m = 0
        #     fouls_m = 0
        #
        #     bb_diamond = {base: 0 for base in bb_diamond}
        #
        #     print("{} of the Inning ({})".format(innings_half[team_at_bat],
        #                                          innings_name[current_inning],))
        #
        #     while outs_m < 3:
        #
        #         inning_data = [team_at_bat,
        #                        batting_lineup,
        #                        batting_lineup_keep,
        #                        outs_m,
        #                        strikes_m,
        #                        balls_m,
        #                        fouls_m,
        #                        bb_diamond,
        #                        team_roster,
        #                        current_inning,
        #                        score_list,
        #                        ]
        #
        #         (team_at_bat,
        #          batting_lineup,
        #          batting_lineup_keep,
        #          outs_m,
        #          strikes_m,
        #          balls_m,
        #          fouls_m,
        #          bb_diamond,
        #          team_roster,
        #          current_inning,
        #          score_list,) = at_bat(inning_data)

########################################################################################################################

    # Check for a tie game after completion of nine innings

    print('*** After nine innings need to check if the score is tied. If true, continue game one inning at a time'
          ' until tie is broken ***')

    print()
    
    print_scorebox(score_list[0], score_list[1])

    print()

    print('VISITOR: {} \t HOME: {}'.format(sum(score_list[0]), sum(score_list[1])))

    print()

    if True:
        score_list = [list(score_tracking_by_inning),
                      list(score_tracking_by_inning), ]
        print('score_list: {}'.format(score_list))

    # if sum(score_list[0]) == sum(score_list[1]):
        print('There is a tie after nine innings!')
        print('Going to extra innings...')

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
    print("*" * 80)

########################################################################################################################

    print()
    print("*** END OF GAME ***")
    print()

    print("+" * 80)
    print("*** MAIN SECTION - END ***")
    print()

    # ***** MAIN SECTION *****

    print()

    # This section tests the teams roster   TODO Remove Section below after testing

    team_roster_score_summ = [[[0], [0]] for x in range(0, 30)]

    # Code for testing aggregation of scores; keep in main for now, but comment out some of the processes
    # print(team_roster_score_summ)




    # for test_ in iter(team_roster_score_summ):
        # print(test_)

    for team_aggregate in range(0,2):
        # print('team idx:', team_aggregate)

        for roster_ in team_roster:
            # print('roster_player: ', roster_)
            for roster_2 in iter(team_roster[roster_]):

                # print('roster_2: {}'.format(roster_2))

                if roster_2[0] == team_aggregate:
                    # print('roster_2[0]: {}'.format(roster_2[0]))
                    # print('roster_2[2]: {}'.format(roster_2[2]))
                    # print('roster_2[4]: {}'.format(roster_2[4]))
                    team_roster_score_summ[roster_2[2]][roster_2[0]].append(roster_2[4])

    # print('team_roster_score_summ: {}'.format(team_roster_score_summ))

    # for chk in iter(team_roster_score_summ):
    #     print('chk: {}, sum(chk): {}'.format(chk, sum(chk[0])))
    # print('score_list_team_roster: {}'.format(score_list_team_roster))

    for team_value in range(0, 2):
        for chk in range(0, 9):
            # print('team: {} \tchk: {}, \tsum(chk): {}'.format(team_value, chk, sum(team_roster_score_summ[chk][team_value])))
            score_list_team_roster[team_value][chk] = sum(team_roster_score_summ[chk][team_value])

    # This section tests the scorebox   TODO Remove Section below after testing
    print("Score box test:")
    print_scorebox(score_list[0], score_list[1])

    # print(score_list)
    # print('score_list_team_roster: {}'.format(score_list_team_roster))
    print()
    print("Score box for score_list_team_roster:")
    print_scorebox(score_list_team_roster[0], score_list_team_roster[1])

    # print('Current data stored in team_roster: \n{}'.format(team_roster))



    # This section tests the the bases dictionary   TODO Remove Section below after testing

    # print("Bases in a dictionary: {}".format(bb_diamond))
    # print("First Base: {}".format(bb_diamond.get('b1_g')))
    # print("*" * 30)
    # print()
