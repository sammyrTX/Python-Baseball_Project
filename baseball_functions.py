# Function to advance base runners based on hit passed from __main__


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
