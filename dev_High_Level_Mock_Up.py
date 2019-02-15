
# TODO  Continue work on Scores section at bottom. Need to compare total score from teams_roster against score_list
#       and make sure/verify they tie

# Mock up to test bases updating, player actions storage, team score storage
# High level

from baseball_functions import *

# Using the dictionary as the main baseball diamond to populate each inning by each time when at bat

bb_diamond = {'h_g': 0,
              'b1_g': 0,
              'b2_g': 0,
              'b3_g': 0,
              }     # Possible alternate to track who is on base

print()
print(bb_diamond)

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


from baseball_functions import *

# Need overall clean up to conform with PEP 8   TODO

# Variables & Data structures

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

print("Teams Roster: \n {}".format(teams_roster))   # TODO For testing

# Print test for roster dictionary  # TODO  for testing
# for x, y in teams_roster.items():
#
#     print(x, ' : ', y)

# For team_at_bat description (0 - Visitors, 1 - Home)

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

print('score tracking: ', score_list)   # TODO Remove after testing
print()

######################################################################################################

# Test data to check handling of player data   # TODO Remove after testing

hits_check = 3  # index position 3

runs_check = 2  # index position 4

RBI_check = 7  # index position 5

######################################################################################################

######################################################################################################

# Set up batting order for a working list and copy to keep for starting at the top of the line up

print("Set up batting order")

batting_lineup = [list(batting_order()), list(batting_order())]

batting_lineup_keep = tuple(tuple(x) for x in batting_lineup)

print(batting_lineup)

print()

######################################################################################################

print()
print('*** START ***')
print()

# Innings loop through 9th Inning

for current_inning in innings_tracker:

    print('+' * 100)

    print('Inning Counter: {} > {}'.format(current_inning, innings_name[current_inning]))
    print()

    # Team at bat (Visitors at top of inning, Home at bottom)

    # Visitors

    # Use to flag which team is at bat Team (0 - Visitors, 1 - Home)

    team_at_bat = 0

    print('Top of Inning > Team at bat: {}'.format(teams_description[team_at_bat]))

    print('Grab next batter from line up for {}:'.format(teams_description[team_at_bat]))

    team_at_bat, batting_lineup, batter_up_m = next_batter(team_at_bat, batting_lineup, batting_lineup_keep)

    print('\t','At bat: {} > {}'.format(batter_up_m, players_tuple[batter_up_m]))

    # Pass player and results data to teams roster list

    teams_roster[players_tuple[batter_up_m]].append([team_at_bat,
                                                     batter_up_m,
                                                     current_inning,
                                                     hits_check,
                                                     runs_check,
                                                     RBI_check,])

    # Pass player runs to score_list

    score_list[team_at_bat][current_inning] += runs_check

    print('>' * 45)

    # Home

    team_at_bat = 1

    print('Bottom of Inning > Team at bat: {}'.format(teams_description[team_at_bat]))

    print('Grab next batter from line up for {}:'.format(teams_description[team_at_bat]))

    team_at_bat, batting_lineup, batter_up_m = next_batter(team_at_bat, batting_lineup, batting_lineup_keep)

    print('\t','At bat: {} > {}'.format(batter_up_m, players_tuple[batter_up_m]))

    # Pass player and results data to teams roster list

    teams_roster[players_tuple[batter_up_m]].append([team_at_bat,
                                                     batter_up_m,
                                                     current_inning,
                                                     hits_check,
                                                     (runs_check + 1),  # TODO  test value adjusted for Home
                                                     RBI_check,])

    # Pass player runs to score_list

    score_list[team_at_bat][current_inning] += (runs_check + 1)

    print()

    print('+' * 100)

# Add section to check for tie

print()
print('****** Check if there is a tie after the 9th inning; play another single inning until the tie is broken *******')

print()

print('Show contents of teams_roster dict after game is played through')
print(teams_roster)

print()
print('Print total score for each team:')
print('*** ADD PROCESS HERE FOR SCORE ***')
# generate total score based on data from teams_roster dict

teams_roster_total_score = [[],[]]

print('teams_roster_total_score: {}'.format(teams_roster_total_score))
print()

for teams in range(2):
    print(teams)

    for players in teams_roster:
        print(players)
        # for scores in teams_roster[players]:
        #     # print('stored data: {}'.format(teams_roster[players].values()))
        print('stored data: {}'.format(teams_roster[players]))
        print('+' * 50)

        for test_ in teams_roster[players]:
            print('   > {}'.format(test_))
            print('teams: {}; test_[0]: {}; test_[0] == teams : {}'.format(teams, test_[0], test_[0] == teams))
            print('test_[4]: {}'.format(test_[4] + 99))

            print('teams_roster_total_score: {}'.format(teams_roster_total_score))
            print()

            print('***')

            if test_[0] == teams:
                teams_roster_total_score[teams].append(test_[4])

            print('teams_roster_total_score[teams]: {}'.format(teams_roster_total_score[teams]))
        print()

print()

print(':' * 50)

print('teams_roster_total_score: {}'.format((teams_roster_total_score)))

print('teams_roster_total_score[0] total: {}'.format(sum(teams_roster_total_score[0])))

print('teams_roster_total_score[1] total: {}'.format(sum(teams_roster_total_score[1])))

print(':' * 50)

print()

print('Print score_list:')
print(score_list)
print(sum(score_list[0]))
print(sum(score_list[1]))

#############################################################################################################

print()
print('Compare teams roster total score against score list:')

print('Visitors:')
print('sum(teams_roster_total_score[0]): {}'.format(sum(teams_roster_total_score[0])))
print('sum(score_list[0]): {}'.format(sum(score_list[0])))
print('teams_roster_total_score[0] == score_list[0]? {}'.format(sum(teams_roster_total_score[0]) == sum(score_list[0])))

print()

print('Home:')
print('sum(teams_roster_total_score[1]): {}'.format(sum(teams_roster_total_score[1])))
print('sum(score_list[1]): {}'.format(sum(score_list[1])))
print('teams_roster_total_score[1] == score_list[1]? {}'.format(sum(teams_roster_total_score[1]) == sum(score_list[1])))

print()

#############################################################################################################

print('*** END ***')
print()