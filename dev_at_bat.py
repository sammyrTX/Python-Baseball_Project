# 01-28-19 - Updates to player at bat processing

from baseball_functions import *

# Player positions stored in a tuple

teams_description = ('VISITORS', 'HOME')

players_tuple = ("Pitcher", "Catcher", "First Base", "Second Base", "Third Base", "Shortstop", "Left Field"
                 , "Center Field", "Right Field")

pitch_result_tuple = (('strike', 10), ('ball', 11), ('foul ball', 12), ('foul out', 13), ('out - defense', 14),
                      ('hit - single', 1), ('hit - double', 2), ('hit - triple', 3), ('hit - homerun', 4))

bb_diamond = {'b1_g': 0, 'b2_g': 0, 'b3_g': 0, 'h_g': 0,}     # Possible alternate to track who is on base


def at_bat(team_f, player_f):

    print(bases_picture())

    print(teams_description[team_f], '|', players_tuple[player_f])

    return



print()

at_bat(0, 2)

print()


    # Creating process to get a team, player & outs count to the function
    # Will return the team, player and one or more of the following:
    #
    #     - An Out
    #     - hit
    #     - RBI's'
    #     - Runs scored (to add to the team's score for the inning')

# outs_count, strikes_count, ball_count, foul_count = process_pitch_result(pitch_result(), outs_count, strikes_count,
#                                                                          ball_count, foul_count)
#
# print('Outs Count: {}\nStrikes: {}\nBalls: {}\nFoul Balls: {}'.format(outs_count, strikes_count, ball_count, foul_count))

########################################################################################################################


print('*** START **************************************************')

outs_count = strikes_ = ball_count = foul_count = 0

while outs_count < 3:

    strikes_ = ball_count = foul_count = 0

    print()
    print('At Bat Begin >>>>>>')
    print()

    print('>>>>>>>> BEFORE Pitch Result')
    print('>>>>>>>> outs_count: {}'.format(outs_count))

    # test     TODO Remove when ready
    # strikes_ = 3
    # outs_count += 1

    while strikes_ != 3:

        outs_count_check = outs_count

        pitch_result_, outs_count, strikes_, ball_count, foul_count = process_pitch_result(pitch_result(),
                                                                                                   outs_count,
                                                                                                   strikes_,
                                                                                                   ball_count,
                                                                                                   foul_count)

        print('Strikes (main): {}'.format(strikes_))
        print('pitch_result_: {}'.format(pitch_result_))

        if pitch_result_[1] in range(1,5):
            print('A Hit! : {}'.format(pitch_result_))
            print()
            strikes_ = ball_count = foul_count = 0
            break

        # Should not need since pitch_process is tallying strikes; confirm with testing with only strikes returned TODO Remove once confirmed
        # if strikes_count == 1:
        #
        #     strikes_ += 1
        #     print("Strike {}!".format(strikes_))
        #
        #     if strikes_ == 3:
        #         print("Yer' out!")
        #         outs_count += 1
        #         break

        if ball_count == 4:
            print('*** Walk the batter *** : {}'.format(pitch_result_))
            print()

            # TODO Need to test walk_batter function

            bb_diamond['b1_g'], bb_diamond['b2_g'], bb_diamond['b3_g'], bb_diamond['h_g'] = \
                walk_batter(bb_diamond['b1_g'], bb_diamond['b2_g'], bb_diamond['b3_g'], bb_diamond['h_g'])

            #  TODO Need to increment team runs if any were made when batter was walked

            strikes_ = ball_count = foul_count = 0
            ball_count_print(outs_count, strikes_, ball_count)  # TODO
            break

        if outs_count > outs_count_check:

            print('Strikes (strikes_count): {}'.format(strikes_))
            print('OUT!')
            print('<<<< outs_count: {}'.format(outs_count))

            strikes_ = ball_count = foul_count = 0
            ball_count_print(outs_count, strikes_, ball_count)  # TODO

            break

        # TEST   TODO REMOVE when ready - this should stop an infinite loop
        # if outs_count > 10:
        #
        #     print('Strikes (strikes_count): {}'.format(strikes_count))
        #     print('OUT!')
        #     print('<<<< outs_count: {}'.format(outs_count))
        #     break

        # ball_count_print(0, 3, ball_count_f)   TODO for testing - remove when finished

        print()
        print('Outs Count: {}\nStrikes: {}\nBalls: {}\nFoul Balls: {}'.format(outs_count, strikes_, ball_count,
                                                                              foul_count))
        print()

        ball_count_print(outs_count, strikes_, ball_count)  # TODO

        print()

    print()

    ball_count_print(outs_count, strikes_, ball_count)  # TODO

    print()
    print('At Bat End >>>>>>')
    print()

print('*** END ****************************************************')
