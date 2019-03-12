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

import random

# data for functions
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

#  **** Advance Runner Needs further testing ****


def advance_runner(hit_,
                   bb_diamond_adv_runner,
                   ):

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


def print_scorebox(visitors_list, home_list):
    print('INNING  ', end='')

    for ctr in range(0,len(visitors_list)):
        print('\t{:>2}'.format(ctr + 1), end='')

    print('\t R', end='')

    print()

    print('------     ', end='')

    for ctr in range(0,len(visitors_list)):
        # print(ctr)
        print('\t--', end='')

    print('\t--', end='')

    print()

    print('VISITORS ', end='')

    for ctr in range(0,len(visitors_list)):
        # print(ctr)
        print('\t{:>2}'.format(visitors_list[ctr]), end='')

    print('\t{:>2}'.format(sum(visitors_list)), end='')


    print()

    print('HOME    ', end='')

    for ctr in range(0,len(home_list)):
        # print(ctr)
        print('\t{:>2}'.format(home_list[ctr]), end='')

    print('\t{:>2}'.format(sum(home_list)), end='')


def batting_order():
    batting_lineup = []

    while len(batting_lineup) < 9:

        next_batter_f = random.randint(0, 8)  # TODO Check Shadow warning
        if next_batter_f in batting_lineup:
            continue
        else:
            batting_lineup.append(next_batter_f)

    return batting_lineup


def pitch_result():
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
    print("*" * 16)
    print("S: {}  B: {}  O: {}".format(strikes_f, ball_f, outs_f))
    print("*" * 16)
    print()
    print("*" * 80)
    print()


def process_pitch_result(pitch_result_f,
                         outs_count_f,
                         strikes_count_f,
                         ball_count_f,
                         foul_count_f,
                         bb_diamond_f):

    # Add code here to simulate specific pitch_result_'s in order test the while loop  TODO Set pitch_result for testing
    # e.g. pitch_result_ = ('TEST > foul out', 13)

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

    if len(batting_lineup_f[team_f]) != 0:

        batter_up_f = batting_lineup_f[team_f][0]
        batting_lineup_f[team_f].pop(0)
    else:
        batting_lineup_f[team_f] = list(batting_lineup_keep_f[team_f])
        batter_up_f = batting_lineup_f[team_f][0]
        batting_lineup_f[team_f].pop(0)

    return team_f, batting_lineup_f, batter_up_f


def bases_picture(bb_diamond_f):

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
