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
#   [4]: RBI (Run(s) Batted In; will ignore errors since they are not being tracked)

teams_roster = {player: [[0, 0, 0, 0, 0]] for player in players_tuple}

print("Teams Roster: \n {}".format(teams_roster))   # TODO For testing

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

score_tracking_by_inning = [0 for init_inning in range(10)]

score_list = [list(score_tracking_by_inning),
              list(score_tracking_by_inning), ]

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

    print('>' * 45)

    # Home

    team_at_bat = 1

    print('Bottom of Inning > Team at bat: {}'.format(teams_description[team_at_bat]))

    print('Grab next batter from line up for {}:'.format(teams_description[team_at_bat]))

    team_at_bat, batting_lineup, batter_up_m = next_batter(team_at_bat, batting_lineup, batting_lineup_keep)

    print('\t','At bat: {} > {}'.format(batter_up_m, players_tuple[batter_up_m]))

    print()

    print('+' * 100)

# Add section to check for tie

print()
print('****** Check if there is a tie after the 9th inning; play another single inning until the tie is broken *******')

print()
print('*** END ***')
print()