# 01-28-19 - Updates to player at bat processing

from baseball_functions import *

# Player positions stored in a tuple

teams_description = ('VISITORS', 'HOME')

players_tuple = ("Pitcher", "Catcher", "First Base", "Second Base", "Third Base", "Shortstop", "Left Field"
                 , "Center Field", "Right Field")



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

outs_count = outs_count_pr = strikes_= strikes_count = ball_count = foul_count = 0

while outs_count < 3:

    strikes_ = strikes_count = ball_count = foul_count = 0

    print()
    print('At Bat Begin >>>>>>')
    print()

    print('>>>>>>>> outs_count_pr: {}'.format(outs_count_pr))
    print('>>>>>>>> outs_count: {}'.format(outs_count))

    while strikes_ != 3:

        pitch_result_, outs_count_pr, strikes_count, ball_count, foul_count = process_pitch_result(pitch_result(),
                                                                                                outs_count,
                                                                                                strikes_count,
                                                                                                ball_count,
                                                                                                foul_count)

        strikes_ += strikes_count

        print('Strikes (main): {}'.format(strikes_))
        print('pitch_result_: {}'.format(pitch_result_))

        if pitch_result_[1] in range(1,5):
            print('A Hit! : {}'.format(pitch_result_))
            print()
            break

        if outs_count_pr == 1:

            print('Strikes (strikes_count): {}'.format(strikes_count))
            print('OUT!')
            outs_count += 1
            print('<<<< outs_count_pr: {}'.format(outs_count_pr))
            print('<<<< outs_count: {}'.format(outs_count))
            break

        # ball_count_print(0, 3, ball_count_f)   TODO for testing - remove when finished

        print('Outs Count: {}\nStrikes: {}\nBalls: {}\nFoul Balls: {}'.format(outs_count, strikes_count, ball_count,
                                                                              foul_count))
        print()

        ball_count_print(outs_count, strikes_count, ball_count)  # TODO

    ball_count_print(outs_count, strikes_count, ball_count)  # TODO

    print()
    print('At Bat End >>>>>>')
    print()

print('*** END ****************************************************')
