"""
Variables and data structures for game set up.

    bb_diamond : dict to track players on base during an inning.
                 0 - no one on base
                 1 - player on base

    team_description_func : stores team description
                            [0] - Visitors
                            [1] - Home

    players_tuple_-func : tuple of the player positions

    Team Roster with lists that for each player stores team, inning, hits, RBI's

    team_roster :

        List index key:
          [0]: Team (0 - Visitors, 1 - Home)
          [1]: Player Position
          [2]: Inning (0 - 8 for 1st through 9th Inning)
          [3]: Hits (Cumulative for a player within an inning)
          [4]: Runs Scored
          [5]: RBI (Run(s) Batted In; will ignore errors since they are
               not being tracked)

    innings_name : List of inning descriptions up to 30 innings max

    innings_half : List of descriptions for top and bottom of inning

    pitch_result_fa : List to store pitch result
                        [0] : ?????
                        [1] : ?????
                        [2] : ?????

    score_tracking_by_inning : list of innings using integer starting at 0
                               through 30.

    score_list : list of scores by team. 0/1, Visitors/Home respectively

    score_list_team_roster : list of scores by team. 0/1, Visitors/Home,
                             respectively. # Need to confirm usage

    batting_order : Generate a batting order of players at random

"""

import random

# bases & home plate

bb_diamond = {'h_g': 0,
              'b1_g': 0,
              'b2_g': 0,
              'b3_g': 0,
              }

# data for game play

team_description_func = ('VISITORS', 'HOME')

players_tuple_func = ("Pitcher",
                      "Catcher",
                      "First Base",
                      "Second Base",
                      "Third Base",
                      "Shortstop",
                      "Left Field",
                      "Center Field",
                      "Right Field",)

team_roster = {player: [] for player in players_tuple_func}

# Use to flag which team is at bat Team (0 - Visitors, 1 - Home)

team_description = ('VISITORS', 'HOME')  # POSSIBLE DUPLICATE <<<<<****

# Innings Descriptions (includes extra innings after standard nine (up to 30))

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

# List to store pitch result

pitch_result_fa = ['', 0, '']

# Innings tracker list by list comprehension

range_variable = 9  # Set number of innings to play

innings_tracker = [x for x in range(0, range_variable)]

# Home team & Visitors score tracking

# Setting to max of 30 innings in extra innings
score_tracking_by_inning = [0 for init_inning in range(30)]

score_list = [list(score_tracking_by_inning),
              list(score_tracking_by_inning), ]

score_list_team_roster = [list(score_tracking_by_inning),
                          list(score_tracking_by_inning),
                          ]


def batting_order():
    """Generate a batting order of players at random"""
    batting_lineup = []

    while len(batting_lineup) < 9:

        next_batter_f = random.randint(0, 8)
        if next_batter_f in batting_lineup:
            continue
        else:
            batting_lineup.append(next_batter_f)

    return batting_lineup
