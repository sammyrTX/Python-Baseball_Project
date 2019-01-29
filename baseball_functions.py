# Functions for baseball project:
# - advance base runners based on hit passed from __main__
# - print score box
# - generate batting order
# - generate pitch result
# - ball count print
# - process pitch result
# - next batter

import random

#  **** Advance Runner Needs further testing ****


def advance_runner(hit_f,
                   base1_f,
                   base2_f,
                   base3_f,
                   home_plate_f):

    print("before advance:")
    print("Hits: {} 1st: {} 2nd: {} 3rd: {} Home: {}"
          .format(hit_f,
                  base1_f,
                  base2_f,
                  base3_f,
                  home_plate_f))

    print("Hit Result = {}".format(hit_f))

    batter = 1   # Initialize batter to put batter on base if someone already on first
    print("batter: {}".format(batter))

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
                batter = 0
            else:
                base1_f = 0
            base2_f = 1
            batter = 0
        else:
            if batter:
                base1_f = 1
                batter = 0

        hit_f -= 1
        print()
        print("after 1 loop:\t", hit_f, base1_f, base2_f, base3_f, home_plate_f)
        print("Hits: {} 1st: {} 2nd: {} 3rd: {} Home: {}".format(hit_f, base1_f, base2_f, base3_f, home_plate_f))  #TODO
        print("batter: {}".format(batter))
    print("function returns:", hit_f, base1_f, base2_f, base3_f, home_plate_f)
    print("batter: {}".format(batter))
    return hit_f, base1_f, base2_f, base3_f, home_plate_f


def print_scorebox(visitors_list, home_list):
    print("INNING  ", "\t 1", "\t 2", "\t 3", "\t 4", "\t 5", "\t 6", "\t 7", "\t 8", "\t 9", "\t R", "\t H")
    print("------  ", "\t--", "\t--", "\t--", "\t--", "\t--", "\t--", "\t--", "\t--", "\t--", "\t--", "\t--")
    print("HOME:     \t{:>2} \t{:>2} \t{:>2} \t{:>2} \t{:>2} \t{:>2} \t{:>2} \t{:>2} \t{:>2} \t{:>2} \t{:>2}".
          format(home_list[0], home_list[1], home_list[2], home_list[3], home_list[4], home_list[5], home_list[6]
                 , home_list[7],home_list[8], sum(home_list), 0))

    print("VISITORS: \t{:>2} \t{:>2} \t{:>2} \t{:>2} \t{:>2} \t{:>2} \t{:>2} \t{:>2} \t{:>2} \t{:>2} \t{:>2}"
          .format(visitors_list[0], visitors_list[1], visitors_list[2], visitors_list[3], visitors_list[4]
                  , visitors_list[5]
                  , visitors_list[6]
                  , visitors_list[7]
                  , visitors_list[8]
                  , sum(visitors_list), 0))


def batting_order():
    batting_lineup = []

    while len(batting_lineup) < 9:
        next_batter = random.randint(0, 8)
        if next_batter in batting_lineup:
            continue
        else:
            batting_lineup.append(next_batter)

    # print("batting order: {}".format(batting_lineup))
    return batting_lineup


def pitch_result():
    pitch_result_tuple = (('strike', 10), ('ball', 11), ('foul ball', 12), ('foul out', 13), ('out - defense', 14),
                          ('hit - single', 1), ('hit - double', 2), ('hit - triple', 3), ('hit - homerun', 4))
    pitch_result_return = random.randint(0, 8)
    return pitch_result_tuple[pitch_result_return]


def ball_count_print(outs_f, strikes_f, ball_f):
    print("*" * 16)
    print("S: {}  B: {}  O: {}".format(strikes_f, ball_f, outs_f))
    print("*" * 16)


def process_pitch_result(pitch_result_f, outs_count_f, strikes_count_f, ball_count_f, foul_count_f):

    # Need to add steps to process advancing runners and tracking runs scored  TODO
    # Need to add steps to process a batter getting walked (4 balls)

    result_txt, result_idx = pitch_result_f
    print("Pitch Result: ",result_txt, result_idx)

    # Hit

    if result_idx in range(1,5):
        print("A hit: ", result_txt, result_idx)
        print("Add step here to advance runner")

    # Strike, Ball or Foul

    if result_idx in range(10, 15):

        if result_idx == 10:
            strikes_count_f += 1
            print("Strike {}!".format(strikes_count_f))
            if strikes_count_f == 3:
                print("Yer' out!")
                outs_count_f = 1

        if result_idx == 12:
            print("Foul ball!")
            if foul_count_f < 2:
                foul_count_f += 1
                if strikes_count_f < 2:
                    strikes_count_f +=1

            print("Foul count: {}".format(foul_count_f))

        # Foul Ball that is caught resulting in an Out

        if result_idx == 13:
            print("Fouled out!")
            outs_count_f = 1

        # Pop Fly that is caught resulting in an Out

        if result_idx == 14:
            print("Pop fly caught - Yer' out!")
            outs_count_f = 1

    # ball_count_print(outs_count_f, strikes_count_f, ball_count_f)   TODO Move to at bat function
    # ball_count_print(0, 3, ball_count_f)   TODO for testing - remove when finished
    print()

    return pitch_result_f, outs_count_f, strikes_count_f, ball_count_f, foul_count_f


def next_batter(team_f, batting_lineup_f, batting_lineup_keep_f):

    players_tuple_f = ("Pitcher", "Catcher", "First Base", "Second Base", "Third Base", "Shortstop", "Left Field"
                     , "Center Field", "Right Field")

    # troubleshooting print statements; remove after testing   TODO Test Prints to be removed
    # print("from function: batting_lineup_f: {}".format(batting_lineup_f))
    # print("from function: batting_lineup_keep_f: {}".format(batting_lineup_keep_f))
    # print(batting_lineup_f == batting_lineup_keep_f)

    if len(batting_lineup_f[team_f]) != 0:

        batter_up_f = batting_lineup_f[team_f][0]
        batting_lineup_f[team_f].pop(0)
        print("At bat: {}".format(players_tuple_f[batter_up_f]))

        # troubleshooting print statements; remove after testing   TODO Test Prints to be removed
        # print("len(batting_lineup_f[team_f]: {}".format(len(batting_lineup_f[team_f])))
        # print("check len of list: {}".format(len(batting_lineup_f[team_f]) != 0))
        # print("check the keep tuple: {}".format(batting_lineup_keep_f[team_f]))
    else:
        # troubleshooting print statements; remove after testing   TODO Test Prints to be removed
        # print("Hit the else clause here ***")
        # print("lineup: {}   keep tuple: {}".format(id(batting_lineup_f), id(batting_lineup_keep_f)))

        batting_lineup_f[team_f] = list(batting_lineup_keep_f[team_f])

        # troubleshooting print statements; remove after testing   TODO Test Prints to be removed
        # print("keep list: {}".format(list(batting_lineup_keep_f[team_f])))
        # print("just keep: {}".format(batting_lineup_keep_f[team_f]))
        # print("batting lineup after updating to batting line up keep: {}".format(batting_lineup_f[team_f]))

        batter_up_f = batting_lineup_f[team_f][0]
        batting_lineup_f[team_f].pop(0)
        print("At bat: {}".format(players_tuple_f[batter_up_f]))

    print(">>>> Line Up for team {}: {}".format(team_f, batting_lineup_f[team_f]))

    return team_f, batting_lineup_f, batter_up_f


def bases_picture():

    # Place holder for bases picture to potentially use to show status of bases during an at bat

    base01 = '*'
    base02 = ' '
    base03 = '*'

    print("            [{}]".format(base02))
    print("           /   \\")
    print("          /     \\")
    print("        [{}]      [{}]".format(base03, base01))
    print("          \\     /")
    print("           \\   /")
    print("            [ ]")
