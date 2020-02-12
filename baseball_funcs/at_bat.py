"""
Functions that process players at bat and the resulting hits, runs, ball
count.

    pitch_result_tuple : randomize the results of a pitch.
"""

import random

from baseball_funcs.game_set_up import(team_description_func,
                                       players_tuple_func,
                                       score_list,
                                       )

from baseball_funcs.base_running import(bases_picture,
                                        walk_batter,
                                        advance_runner,
                                        )

from baseball_funcs.scorebox import print_scorebox


def pitch_result():

    """Generate the result of a pitch at random based on available outcomes
       stored in a tuple"""
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
    print(f'S: {strikes_f}  B: {ball_f}  O: {outs_f}')
    print("-" * 16)
    print()
    print("*" * 50)
    print()


def process_pitch_result(pitch_result_f,
                         outs_count_f,
                         strikes_count_f,
                         ball_count_f,
                         foul_count_f,
                         bb_diamond_f,):
    """Takes the generated pitch result and processes the batter. This
       includes a hit (calls the advance_runner function) or Strikes,
       Balls and Fouls (stores the count). With four balls it walks the
       batter."""

    # Test pitches can be inserted here see sample on next line
    # pitch_result_f = ('TEST hit - double', 2, 'TEST Hit! A Double')
    result_txt, result_idx, result_description = pitch_result_f

    # Hit
    if result_idx in range(1, 5):

        print(f'{result_description}!')

        pitch_result_f, bb_diamond_f = advance_runner(pitch_result_f,
                                                      bb_diamond_f)

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
            bb_diamond_f,)


def next_batter(team_f,
                batting_lineup_f,
                batting_lineup_keep_f,):

    """Moves through the batting order and removes the next batter. When
       the batting order is exhausted, it reloads the order from a tuple
       that has the whole batting order."""

    if len(batting_lineup_f[team_f]) != 0:

        batter_up_f = batting_lineup_f[team_f][0]
        batting_lineup_f[team_f].pop(0)
    else:
        batting_lineup_f[team_f] = list(batting_lineup_keep_f[team_f])
        batter_up_f = batting_lineup_f[team_f][0]
        batting_lineup_f[team_f].pop(0)

    return team_f, batting_lineup_f, batter_up_f


def at_bat(inning_data_func):
    """Processes the batter for a team at bat. Takes the current team at bat,
       the batting order (and complete batting order), base status,dictionary,
       and score tracking."""

    (team_at_bat_fa,
     batting_lineup_fa,
     batting_lineup_fa_keep,
     outs_fa,
     strikes_fa,
     balls_fa,
     fouls_fa,
     bb_diamond_fa,
     team_roster_fa,
     current_inning_fa,
     score_list_fa,) = inning_data_func

    (team_at_bat_fa,
     batting_lineup_fa,
     batter_up_fa) = next_batter(
        team_at_bat_fa,
        batting_lineup_fa,
        batting_lineup_fa_keep,
    )

    while True:
        print(f'At bat for {team_description_func[team_at_bat_fa]}: {players_tuple_func[batter_up_fa]}\n')

        outs_pre = int(outs_fa)

        (pitch_result_fa,
         outs_fa,
         strikes_fa,
         balls_fa,
         fouls_fa,
         bb_diamond_fa) = process_pitch_result(pitch_result(),
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

            # Batter was walked, tally home_plate if there was a score, init
            # and then break for next batter

            if pitch_result_fa[0] == 'ball' and pitch_result_fa[1] == 44:

                team_roster_fa[players_tuple_func[batter_up_fa]].append(
                    [team_at_bat_fa,
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

                team_roster_fa[players_tuple_func[batter_up_fa]].append(
                    [team_at_bat_fa,
                     batter_up_fa,
                     current_inning_fa,
                     1,
                     bb_diamond_fa['h_g'],
                     bb_diamond_fa['h_g']
                     ])

            # Process any hits that resulted in a run batted in
            if bb_diamond_fa['h_g'] != 0:

                # Add runs to score list
                score_list_fa[team_at_bat_fa][current_inning_fa] += bb_diamond_fa['h_g']

                # Pass player and results data to teams roster list and any
                # runs scored. Clear Home Plate after runs and RBI's
                # recorded
                team_roster_fa[players_tuple_func[batter_up_fa]].append(
                    [team_at_bat_fa,
                     batter_up_fa,
                     current_inning_fa,
                     1,
                     bb_diamond_fa['h_g'],
                     bb_diamond_fa['h_g'],
                     ])

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
