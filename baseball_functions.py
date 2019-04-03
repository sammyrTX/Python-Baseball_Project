import random

# Functions for baseball project:
# - advance base runners based on hit passed from __main__
# - print score box
# - generate batting order
# - generate pitch result
# - ball count print
# - process pitch result
# - next batter
# - walk batter
# - team at bat
# - inning_process

########################################################################################################################

# Variables & Data structures

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

# Team Roster with lists that for each player stores team, inning, hits, RBI's
#
# List index key:
#   [0]: Team (0 - Visitors, 1 - Home)
#   [1]: Player Position
#   [2]: Inning (0 - 8 for 1st through 9th Inning)
#   [3]: Hits (Cumulative for a player within an inning)
#   [4]: Runs Scored
#   [5]: RBI (Run(s) Batted In; will ignore errors since they are not being tracked)

team_roster = {player: [] for player in players_tuple_func}

# Use to flag which team is at bat Team (0 - Visitors, 1 - Home)

team_description = ('VISITORS', 'HOME')

# Innings Descriptions (includes extra innings after standard nine)

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

# Innings tracker list by list comprehension

innings_tracker = [x for x in range(0, 3)]  # 9)]    #  TODO Testing - Set innings to just 3

# Home team & Visitors score tracking

score_tracking_by_inning = [0 for init_inning in range(30)]  # Setting to max of 30 innings in extra innings

score_list = [list(score_tracking_by_inning),
              list(score_tracking_by_inning), ]

score_list_team_roster = [list(score_tracking_by_inning),
                          list(score_tracking_by_inning), ]

########################################################################################################################

#  Advance Runner based on hit result
#  **** Needs further testing ****


def advance_runner(hit_,
                   bb_diamond_adv_runner,
                   ):
    """Advances batter after a hit (single through home run) based on pitch_result.
    takes the pitch result and a dictionary of the bases as arguments"""

    hit_txt, hit_f, hit_descr = hit_

    print('{}'.format(hit_descr))

    home_plate_f, base1_f, base2_f, base3_f = bb_diamond_adv_runner.values()

    batter = 1   # Initialize batter to put batter on base if someone already on first

    while hit_f:
        if base3_f == 1:
            base3_f = 0
            home_plate_f += 1

        if base2_f == 1:
            base2_f = 0
            base3_f = 1

        if base1_f == 1:
            if batter:
                base1_f = 1
                batter = 0    # TODO  Check warning for usage; IDE is indicating variable is not used
            else:
                base1_f = 0
            base2_f = 1
            batter = 0
        else:
            if batter:
                base1_f = 1
                batter = 0

        hit_f -= 1  # Decrement hit_f in order to advance batter the appropriate number of bases

    bb_diamond_adv_runner['h_g'] = home_plate_f
    bb_diamond_adv_runner['b1_g'] = base1_f
    bb_diamond_adv_runner['b2_g'] = base2_f
    bb_diamond_adv_runner['b3_g'] = base3_f

    return hit_, bb_diamond_adv_runner


def print_scorebox(current_inning_f, visitors_list, home_list):
    """Generates a score box of nine innings along with the number of total runs for the game"""

    current_inning_f +=1

    # if less than nine innings show values for all nine innings
    if current_inning_f < 9:
        current_inning_f = 9

    print('INNING  ', end='')

    for inning_counter in range(0, current_inning_f):
        print('\t{:>2}'.format(inning_counter + 1), end='')

    print('\t R', end='')

    print()

    print('------     ', end='')

    for inning_counter in range(0, current_inning_f):
        print('\t--', end='')

    print('\t--', end='')

    print()

    print('VISITORS ', end='')

    for inning_counter in range(0, current_inning_f):
        print('\t{:>2}'.format(visitors_list[inning_counter]), end='')

    print('\t{:>2}'.format(sum(visitors_list)), end='')


    print()

    print('HOME    ', end='')

    for inning_counter in range(0, current_inning_f):
        print('\t{:>2}'.format(home_list[inning_counter]), end='')

    print('\t{:>2}'.format(sum(home_list)), end='')

    print('\n\n')


def batting_order():
    """Generate a batting order of players at random"""
    batting_lineup = []

    while len(batting_lineup) < 9:

        next_batter_f = random.randint(0, 8)  # TODO Check Shadow warning
        if next_batter_f in batting_lineup:
            continue
        else:
            batting_lineup.append(next_batter_f)

    return batting_lineup


def pitch_result():
    """Generate the result of a pitch at random based on available outcomes stored in a tuple"""
    pitch_result_tuple = (('strike', 10, 'Strike!',),
                          ('ball', 11, 'Ball!',),
                          ('foul ball', 12, 'Foul Ball!',),
                          ('foul out', 13, 'Out!',),
                          ('out - defense', 14, 'Out!',),
                          ('hit - single', 1, 'Hit! A Single',),
                          ('hit - double', 2, 'Hit! A Double',),
                          ('hit - triple', 3, 'Hit! A Triple',),
                          ('hit - home run', 4, 'Home Run!!!',),)

    pitch_result_return = random.randint(0, 8)
    return pitch_result_tuple[pitch_result_return]


def ball_count_print(outs_f, strikes_f, ball_f):
    """Prints out the current ball count based on arguments"""
    print("-" * 16)
    print("S: {}  B: {}  O: {}".format(strikes_f, ball_f, outs_f))
    print("-" * 16)
    print()
    print("*" * 80)
    print()


def process_pitch_result(pitch_result_f,
                         outs_count_f,
                         strikes_count_f,
                         ball_count_f,
                         foul_count_f,
                         bb_diamond_f):
    """Takes the generated pitch result and processes the batter. This includes a hit (calls the advance_runner function
    ) or Strikes, Balls and Fouls (stores the count). With four balls it walks the batter."""

    # print()  TODO Test Pitches
    # pitch_result_f = ('TEST > hit - double', 2)
    # pitch_result_f = ('TEST > hit - single', 1)
    # pitch_result_f = ('TEST > hit - home run', 4)
    # pitch_result_f = ('TEST > ball', 11)
    # pitch_result_f = ('TEST > strike', 10)
    # pitch_result_f = ('TEST > foul out', 13)
    result_txt, result_idx, result_description = pitch_result_f
    # print("*TEST* Pitch Result: ", result_txt, result_idx)

    # Hit
    if result_idx in range(1, 5):
        pitch_result_f, bb_diamond_f = advance_runner(pitch_result_f, bb_diamond_f)

    # Strike, Ball or Foul
    if result_idx in range(10, 15):

        if result_idx == 10:
            strikes_count_f += 1
            print("Strike {}!".format(strikes_count_f))

            if strikes_count_f == 3:
                print("Yer' out!")
                outs_count_f += 1

        if result_idx == 11:
            print('Ball!')
            ball_count_f += 1

            if ball_count_f == 4:

                bb_diamond_f = walk_batter(bb_diamond_f)

                pitch_result_f = ['ball', 44]

        if result_idx == 12:
            print("Foul ball!")
            if foul_count_f < 2:
                foul_count_f += 1
                if strikes_count_f < 2:
                    strikes_count_f += 1

        # Foul Ball that is caught resulting in an Out
        if result_idx == 13:
            print("Fouled out!")
            outs_count_f += 1

        # Pop Fly that is caught resulting in an Out
        if result_idx == 14:
            print("Pop fly caught - Yer' out!")
            outs_count_f += 1

    return (pitch_result_f,
            outs_count_f,
            strikes_count_f,
            ball_count_f,
            foul_count_f,
            bb_diamond_f,
            )


def next_batter(team_f,
                batting_lineup_f,
                batting_lineup_keep_f,):
    """Moves through the batting order and removes the next batter. When the batting order is exhausted, it reloads the
    order from a tuple that has the whole batting order."""

    if len(batting_lineup_f[team_f]) != 0:

        batter_up_f = batting_lineup_f[team_f][0]
        batting_lineup_f[team_f].pop(0)
    else:
        batting_lineup_f[team_f] = list(batting_lineup_keep_f[team_f])
        batter_up_f = batting_lineup_f[team_f][0]
        batting_lineup_f[team_f].pop(0)

    return team_f, batting_lineup_f, batter_up_f


def bases_picture(bb_diamond_f):
    """Generates a simple text based image of the bases and marks bases that have a base runner. This source
    information is stored in a dictionary"""

    base01 = bb_diamond_f['b1_g']
    base02 = bb_diamond_f['b2_g']
    base03 = bb_diamond_f['b3_g']

    if base01 == 1:
        base01_pic = '*'
    else:
        base01_pic = ' '

    if base02 == 1:
        base02_pic = '*'
    else:
        base02_pic = ' '

    if base03 == 1:
        base03_pic = '*'
    else:
        base03_pic = ' '

    print()
    print("       [{}]".format(base02_pic))
    print("      /   \\")
    print("     /     \\")
    print("   [{}]      [{}]".format(base03_pic, base01_pic))
    print("     \\     /")
    print("      \\   /")
    print("       [ ]")
    print()

    return


def walk_batter(bb_diamond_walk_runner):
    """After the fourth pitch result of ball, the batter is walked. Any runners on base advance one base (or go to
    home plate and score)."""

    home_plate_f, base1_f, base2_f, base3_f = bb_diamond_walk_runner.values()

    print('Bases before batter is walked:')
    print('base1_f: {}'.format(base1_f))
    print('base2_f: {}'.format(base2_f))
    print('base3_f: {}'.format(base3_f))
    print('home_plate_f: {}'.format(home_plate_f))
    print()
    print('Add Process here to walk the batter after four balls')     # TODO Add process to walk batter

    # if there is already a batter on first base, then put batter on first and process other runners

    if base1_f == 1:

        if base3_f == 1 and base2_f == 1:     # Bases loaded, increment home plate for third base runner to home
            home_plate_f += 1

        if base3_f == 1 and base2_f == 0:     # Move runner to second base, third base stays
            base2_f = 1

        if base3_f == 0 and base2_f == 1:     # Move runner to third base, second base stays
            base3_f = 1

        if base3_f == 0 and base2_f == 0:     # Move runner to second base
            base2_f = 1

    # if no one on first base, put batter on first, no change for other bases

    if base1_f == 0:
        base1_f = 1

    bb_diamond_walk_runner['h_g'] = home_plate_f
    bb_diamond_walk_runner['b1_g'] = base1_f
    bb_diamond_walk_runner['b2_g'] = base2_f
    bb_diamond_walk_runner['b3_g'] = base3_f

    print('Bases after batter is walked:')
    print('base1_f: {}'.format(base1_f))
    print('base2_f: {}'.format(base2_f))
    print('base3_f: {}'.format(base3_f))
    print('home_plate_f: {}'.format(home_plate_f))
    print()

    return bb_diamond_walk_runner


def at_bat(inning_data_func):
    """Processes the batter for a team at bat. Takes the current team at bat, the batting order (and complete batting
    order), base status dictionary, and score tracking."""

    (team_at_bat_fa,
     batting_lineup_fa, batting_lineup_fa_keep,
     outs_fa, strikes_fa, balls_fa, fouls_fa,
     bb_diamond_fa,
     team_roster_fa,
     current_inning_fa,
     score_list_fa,) = inning_data_func

    team_at_bat_fa, batting_lineup_fa, batter_up_fa = next_batter(team_at_bat_fa,
                                                                  batting_lineup_fa,
                                                                  batting_lineup_fa_keep,
                                                                  )

    while True:
        print('At bat for {}: {}'.format(team_description_func[team_at_bat_fa], players_tuple_func[batter_up_fa]))

        print('')
        
        outs_pre = int(outs_fa)
        
        pitch_result_fa, outs_fa, strikes_fa, balls_fa, fouls_fa, bb_diamond_fa = process_pitch_result(pitch_result(),
                                                                                                       outs_fa,
                                                                                                       strikes_fa,
                                                                                                       balls_fa,
                                                                                                       fouls_fa,
                                                                                                       bb_diamond_fa,
                                                                                                       )

        if outs_fa > outs_pre:

            strikes_fa = 0
            balls_fa = 0
            fouls_fa = 0

            bases_picture(bb_diamond_fa)

            ball_count_print(outs_fa,
                             strikes_fa,
                             balls_fa,)

            break

        if pitch_result_fa[0] in ('strike', 'ball', 'foul ball'):

            # Batter was walked, tally home_plate if there was a score, init and then break for next batter

            if pitch_result_fa[0] == 'ball' and pitch_result_fa[1] == 44:

                team_roster_fa[players_tuple_func[batter_up_fa]].append([team_at_bat_fa,
                                                                         batter_up_fa,
                                                                         current_inning_fa,
                                                                         0,
                                                                         bb_diamond_fa['h_g'],
                                                                         bb_diamond_fa['h_g'],
                                                                         ])
                # Clear ball count after batter is walked
                strikes_fa = 0
                balls_fa = 0
                fouls_fa = 0

                bases_picture(bb_diamond_fa)

                ball_count_print(outs_fa,
                                 strikes_fa,
                                 balls_fa,)

                break

            ball_count_print(outs_fa,
                             strikes_fa,
                             balls_fa,)
            continue

        if pitch_result_fa[1] in range(1, 5):

            # Process hit if there is no run batted in
            if bb_diamond_fa['h_g'] == 0:

                team_roster_fa[players_tuple_func[batter_up_fa]].append([team_at_bat_fa,
                                                                         batter_up_fa,
                                                                         current_inning_fa,
                                                                         1,
                                                                         bb_diamond_fa['h_g'],
                                                                         bb_diamond_fa['h_g']])

            # Process any hits that resulted in a run batted in
            if bb_diamond_fa['h_g'] != 0:

                # Add runs to score list
                score_list_fa[team_at_bat_fa][current_inning_fa] += bb_diamond_fa['h_g']

                # Pass player and results data to teams roster list and any runs scored. Clear Home Plate after
                # runs nd RBI's recorded
                team_roster_fa[players_tuple_func[batter_up_fa]].append([team_at_bat_fa,
                                                                         batter_up_fa,
                                                                         current_inning_fa,
                                                                         1,
                                                                         bb_diamond_fa['h_g'],
                                                                         bb_diamond_fa['h_g']])

                # Reset home plate
                bb_diamond_fa['h_g'] = 0

            # Clear Ball Count
            strikes_fa = 0
            balls_fa = 0
            fouls_fa = 0

            bases_picture(bb_diamond_fa)

            ball_count_print(outs_fa,
                             strikes_fa,
                             balls_fa,)

            print()

            # Show Score box

            print_scorebox(current_inning_fa, score_list[0], score_list[1])

            break

    return (team_at_bat_fa,
            batting_lineup_fa,
            batting_lineup_fa_keep,
            outs_fa,
            strikes_fa,
            balls_fa,
            fouls_fa,
            bb_diamond_fa,
            team_roster_fa,
            current_inning_fa,
            score_list_fa,)


def inning_process(inning_process_data_inning):
    """Process each team for an inning while outs are less than three. Utilizes the at_bat function that processes the
    current batter."""

    [current_inning_f,
     bb_diamond_inning,
     innings_half_inning,
     innings_name_inning,
     batting_lineup_inning,
     batting_lineup_keep_inning,
     team_roster_inning,
     score_list_inning,
     ] = inning_process_data_inning

    for team_at_bat_inning in range(0, 2):

        outs_m = 0
        balls_m = 0
        strikes_m = 0
        fouls_m = 0

        bb_diamond_inning = {base: 0 for base in bb_diamond_inning}

        print("{} of the Inning ({})".format(innings_half_inning[team_at_bat_inning],
                                             innings_name_inning[current_inning_f],))

        while outs_m < 3:

            inning_data = [team_at_bat_inning,
                           batting_lineup_inning,
                           batting_lineup_keep_inning,
                           outs_m,
                           strikes_m,
                           balls_m,
                           fouls_m,
                           bb_diamond_inning,
                           team_roster_inning,
                           current_inning_f,
                           score_list_inning,
                           ]

            (team_at_bat,
             batting_lineup,
             batting_lineup_keep,
             outs_m,
             strikes_m,
             balls_m,
             fouls_m,
             bb_diamond_inning,
             team_roster,
             current_inning_f,
             score_list,) = at_bat(inning_data)

    return (current_inning_f,
            bb_diamond_inning,
            innings_half_inning,
            innings_name_inning,
            batting_lineup_inning,
            batting_lineup_keep_inning,
            team_roster_inning,
            score_list_inning,
            )

########################################################################################################################

    # This section tests the teams roster   TODO Remove Section below after testing

    # Code for testing aggregation of scores; keep in main for now, but comment out some of the processes
    # print(team_roster_score_summ)



    #
    # # for test_ in iter(team_roster_score_summ):
    #     # print(test_)
    #
    # for team_aggregate in range(0,2):
    #     print('team idx:', team_aggregate)
    #
    #     for roster_ in team_roster:
    #         print('roster_player: ', roster_)
    #         for roster_2 in iter(team_roster[roster_]):
    #
    #             print('roster_2: {}'.format(roster_2))
    #
    #             if roster_2[0] == team_aggregate:
    #                 print('roster_2[0]: {}'.format(roster_2[0]))
    #                 print('roster_2[2]: {}'.format(roster_2[2]))
    #                 print('roster_2[4]: {}'.format(roster_2[4]))
    #                 team_roster_score_summ[roster_2[2]][roster_2[0]].append(roster_2[4])
    #
    # # print('team_roster_score_summ: {}'.format(team_roster_score_summ))
    #
    # # for chk in iter(team_roster_score_summ):
    # #     print('chk: {}, sum(chk): {}'.format(chk, sum(chk[0])))
    # # print('score_list_team_roster: {}'.format(score_list_team_roster))
    #
    # for team_value in range(0, 2):
    #     for chk in range(0, 9):
    #         # print('team: {} \tchk: {}, \tsum(chk): {}'.format(team_value, chk, sum(team_roster_score_summ[chk][team_value])))
    #         score_list_team_roster[team_value][chk] = sum(team_roster_score_summ[chk][team_value])
    #
    # # This section tests the scorebox   TODO Remove Section below after testing
    # print("Score box test:")
    # print_scorebox(score_list[0], score_list[1])
    #
    # # print(score_list)
    # # print('score_list_team_roster: {}'.format(score_list_team_roster))
    # print()
    # print("Score box for score_list_team_roster:")
    # print_scorebox(score_list_team_roster[0], score_list_team_roster[1])
    #
    # # print('Current data stored in team_roster: \n{}'.format(team_roster))
    #
    #
    #
    # # This section tests the the bases dictionary   TODO Remove Section below after testing
    #
    # # print("Bases in a dictionary: {}".format(bb_diamond))
    # # print("First Base: {}".format(bb_diamond.get('b1_g')))
    # # print("*" * 30)
    # # print()

