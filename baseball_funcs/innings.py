"""
Processes and data structures for an inning
"""

from baseball_funcs.at_bat import (at_bat,
                                   )

# in process of moving innings code from main to innings package

def innings_nine(batting_lineup, batting_lineup_keep):

    """Process nine innings"""

    from baseball_funcs.game_set_up import(innings_tracker,
                                           bb_diamond,
                                           innings_half,
                                           innings_name,
                                           team_roster,
                                           score_list,
                                           )

    from baseball_funcs.scorebox import print_scorebox

    current_inning = 0

    # Innings Loop - Process Nine Innings plus extra if necessary

    while True:

        print("-" * 50, '\n')

        inning_process_data = [current_inning,
                               bb_diamond,
                               innings_half,
                               innings_name,
                               batting_lineup,
                               batting_lineup_keep,
                               team_roster,
                               score_list,
                               ]
        (current_inning,
         bb_diamond,
         innings_half,
         innings_name,
         batting_lineup,
         batting_lineup_keep,
         team_roster,
         score_list,
         ) = inning_process(inning_process_data)

        print("-" * 50, '\n')

        print()

        print_scorebox(current_inning, score_list[0], score_list[1])

        print()

        #  *** RESUME HERE ***
        #  need to create logic to handle extra innings or finish at nine innings

        if current_inning == 8 and sum(score_list[0]) != sum(score_list[1]):
            break
        elif current_inning >= 8 and sum(score_list[0]) == sum(score_list[1]):
            current_inning += 1
        else:
            current_inning += 1

        print(f'VISITOR: {sum(score_list[0])} \t HOME: {sum(score_list[1])}', '\n')

        # Play extra innings if there is a tie at the end of nine
        if sum(score_list[0]) == sum(score_list[1]):

            # Pack game data
            inning_process_data = [current_inning,
                                   bb_diamond,
                                   innings_half,
                                   innings_name,
                                   batting_lineup,
                                   batting_lineup_keep,
                                   team_roster,
                                   score_list,
                                   ]

            innings_extra(inning_process_data)


def innings_extra(inning_process_data):
    """If game is tied at end of nine innings, process extra innings
    until tie is broken
    """
    pass
    # Run extra innings

    (current_inning,
     bb_diamond,
     innings_half,
     innings_name,
     batting_lineup,
     batting_lineup_keep,
     team_roster,
     score_list,
     ) = inning_process_data

    while sum(score_list[0]) == sum(score_list[1]):

        current_inning += 1
        if innings_name[current_inning] != '*** OUT OF RANGE ***':

            print(innings_name[current_inning], "*** EXTRA INNINGS BEGIN ***")

            inning_process_data = [current_inning,
                                   bb_diamond,
                                   innings_half,
                                   innings_name,
                                   batting_lineup,
                                   batting_lineup_keep,
                                   team_roster,
                                   score_list,
                                   ]
            (current_inning,
             bb_diamond,
             innings_half,
             innings_name,
             batting_lineup,
             batting_lineup_keep,
             team_roster,
             score_list,
             ) = inning_process(inning_process_data)


def inning_process(inning_process_data_inning):
    """Process each team for an inning while outs are less than three.
       Utilizes the at_bat function that processes the current batter."""

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

        print(f'>>> {innings_half_inning[team_at_bat_inning]} of the {innings_name_inning[current_inning_f]} <<<\n')

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
