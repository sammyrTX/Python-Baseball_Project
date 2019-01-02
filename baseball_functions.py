# Functions for baseball project:
# - advance base runners based on hit passed from __main__
# - print score box
# - generate batting order
# - generate pitch result

import random


def advance_runner(hit_f, base1_f, base2_f, base3_f, home_plate_f):
    print("before advance:")
    print(hit_f, base1_f, base2_f, base3_f, home_plate_f)

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
        else:
            base1_f = 1

        hit_f -= 1
        print("after 1 loop:\t", hit_f, base1_f, base2_f, base3_f, home_plate_f)
        print("batter: {}".format(batter))
    print("function returns:", hit_f, base1_f, base2_f, base3_f, home_plate_f)
    print("batter: {}".format(batter))
    return hit_f, base1_f, base2_f, base3_f, home_plate_f


def print_scorebox(home_list, visitors_list):
    # print("TEST TEST TEST")
    # print("Home Team List Score: {}".format(home_list[0]))
    # print("Home Team List Score: {}".format(home_list[3]))
    print("INNING  ", "\t 1", "\t 2", "\t 3", "\t 4", "\t 5", "\t 6", "\t 7", "\t 8", "\t 9", "\t R", "\t H", "\t E")
    print("------  ", "\t--", "\t--", "\t--", "\t--", "\t--", "\t--", "\t--", "\t--", "\t--", "\t--", "\t--", "\t--")
    print("HOME:     \t{:>2} \t{:>2} \t{:>2} \t{:>2} \t{:>2} \t{:>2} \t{:>2} \t{:>2} \t{:>2} \t{:>2} \t{:>2} \t{:>2}".format(home_list[0],
                     home_list[1], home_list[2],home_list[3], home_list[4], home_list[5],home_list[6], home_list[7],
                                                                                                     home_list[8],
                                                                                                     sum(home_list), 88, 88))

    print("VISITORS: \t{:>2} \t{:>2} \t{:>2} \t{:>2} \t{:>2} \t{:>2} \t{:>2} \t{:>2} \t{:>2} \t{:>2} \t{:>2} \t{:>2}"
          .format(visitors_list[0], visitors_list[1], visitors_list[2], visitors_list[3], visitors_list[4]
                  , visitors_list[5], visitors_list[6], visitors_list[7], visitors_list[8], sum(visitors_list), 99, 99))
    
    
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
