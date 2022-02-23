"""
Processes handling base running, baseball picture
"""


def bases_picture(bb_diamond_f):

    """Generates a simple text based image of the bases and marks bases
       that have a base runner. This source information is stored in a
       dictionary"""

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
    print(f'       [{base02_pic}]')
    print('      /   \\')
    print('     /     \\')
    print(f'  [{base03_pic}]      [{base01_pic}]')
    print('     \\     /')
    print('      \\   /')
    print('       [ ]')
    print()

    return


def walk_batter(bb_diamond_walk_runner):

    """After the fourth pitch result of ball, the batter is walked. Any
       runners on base advance one base (or go to home plate and score)."""

    home_plate_f, base1_f, base2_f, base3_f = bb_diamond_walk_runner.values()

    print('Bases before batter is walked:')
    print(f'base1_f: {base1_f}')
    print(f'base2_f: {base2_f}')
    print(f'base3_f: {base3_f}')
    print(f'home_plate_f: {home_plate_f}')
    print()

    print('Add Process here to walk the batter after four balls')

    # if there is already a batter on first base, then put batter on first and
    # process other runners

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
    print(f'base1_f: {base1_f}')
    print(f'base2_f: {base2_f}')
    print(f'base3_f: {base3_f}')
    print(f'home_plate_f: {home_plate_f}')
    print()

    return bb_diamond_walk_runner


def advance_runner(hit_,
                   bb_diamond_adv_runner,
                   ):
    """Advances batter after a hit (single through home run) based on
     pitch_result. Takes the pitch result and a dictionary of the bases
     as arguments"""

    hit_txt, hit_f, hit_descr = hit_

    home_plate_f, base1_f, base2_f, base3_f = bb_diamond_adv_runner.values()

    # Initialize batter to put batter on base if someone already on first
    batter = 1

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
