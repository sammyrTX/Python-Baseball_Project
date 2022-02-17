"""
Test Suite
Check base runner output based on pitch and number of base runners.
"""
from baseball_funcs.game_set_up import (team_description_func,
                                        players_tuple_func,
                                        )

from baseball_funcs.base_running import advance_runner

###############################################################################

# For reference:

"""Pitch result types:
pitch_result_tuple = (('strike', 10, 'Strike!',),
                      ('ball', 11, 'Ball!',),
                      ('foul ball', 12, 'Foul Ball!',),
                      ('foul out', 13, 'Out!',),
                      ('out - defense', 14, 'Out!',),
                      ('hit - single', 1, 'Hit! A Single',),
                      ('hit - double', 2, 'Hit! A Double',),
                      ('hit - triple', 3, 'Hit! A Triple',),
                      ('hit - home run', 4, 'Home Run!!!',),)
"""

###############################################################################


# When there are no runners on base

def test_advance_runner_single():

    """Test Single, no person on base
    """

    hit_ = ('hit - single', 1, 'Hit! A Single',)
    bb_diamond_adv_runner = {'h_g': 0,
                             'b1_g': 0,
                             'b2_g': 0,
                             'b3_g': 0,
                             }

    hit_, bb_diamond_adv_runner_result = advance_runner(hit_,
                                                        bb_diamond_adv_runner,
                                                        )

    assert bb_diamond_adv_runner_result == {'h_g': 0,
                                            'b1_g': 1,
                                            'b2_g': 0,
                                            'b3_g': 0,
                                            }


def test_advance_runner_double():

    """Test Double, no person on base
    """

    hit_ = ('hit - double', 2, 'Hit! A Double',)
    bb_diamond_adv_runner = {'h_g': 0,
                             'b1_g': 0,
                             'b2_g': 0,
                             'b3_g': 0,
                             }

    hit_, bb_diamond_adv_runner_result = advance_runner(hit_,
                                                        bb_diamond_adv_runner,
                                                        )

    assert bb_diamond_adv_runner_result == {'h_g': 0,
                                            'b1_g': 0,
                                            'b2_g': 1,
                                            'b3_g': 0,
                                            }


def test_advance_runner_triple():

    """Test Triple, no person on base
    """

    hit_ = ('hit - triple', 3, 'Hit! A Triple',)
    bb_diamond_adv_runner = {'h_g': 0,
                             'b1_g': 0,
                             'b2_g': 0,
                             'b3_g': 0,
                             }

    hit_, bb_diamond_adv_runner_result = advance_runner(hit_,
                                                        bb_diamond_adv_runner,
                                                        )

    assert bb_diamond_adv_runner_result == {'h_g': 0,
                                            'b1_g': 0,
                                            'b2_g': 0,
                                            'b3_g': 1,
                                            }


def test_advance_runner_homer():

    """Test Homerun, no person on base
    """

    hit_ = ('hit - home run', 4, 'Home Run!!!')
    bb_diamond_adv_runner = {'h_g': 0,
                             'b1_g': 0,
                             'b2_g': 0,
                             'b3_g': 0,
                             }

    hit_, bb_diamond_adv_runner_result = advance_runner(hit_,
                                                        bb_diamond_adv_runner,
                                                        )

    assert bb_diamond_adv_runner_result == {'h_g': 1,
                                            'b1_g': 0,
                                            'b2_g': 0,
                                            'b3_g': 0,
                                            }

# When runner on first base


def test_advance_runner_single_b1():

    """Test Single, person on first base
    """

    hit_ = ('hit - single', 1, 'Hit! A Single',)
    bb_diamond_adv_runner = {'h_g': 0,
                             'b1_g': 1,
                             'b2_g': 0,
                             'b3_g': 0,
                             }

    hit_, bb_diamond_adv_runner_result = advance_runner(hit_,
                                                        bb_diamond_adv_runner,
                                                        )

    assert bb_diamond_adv_runner_result == {'h_g': 0,
                                            'b1_g': 1,
                                            'b2_g': 1,
                                            'b3_g': 0,
                                            }


def test_advance_runner_double_b1():

    """Test Double, person on first base
    """

    hit_ = ('hit - double', 2, 'Hit! A Double',)
    bb_diamond_adv_runner = {'h_g': 0,
                             'b1_g': 1,
                             'b2_g': 0,
                             'b3_g': 0,
                             }

    hit_, bb_diamond_adv_runner_result = advance_runner(hit_,
                                                        bb_diamond_adv_runner,
                                                        )

    assert bb_diamond_adv_runner_result == {'h_g': 0,
                                            'b1_g': 0,
                                            'b2_g': 1,
                                            'b3_g': 1,
                                            }


def test_advance_runner_triple_b1():

    """Test Triple, person on first base
    """

    hit_ = ('hit - triple', 3, 'Hit! A Triple',)
    bb_diamond_adv_runner = {'h_g': 0,
                             'b1_g': 1,
                             'b2_g': 0,
                             'b3_g': 0,
                             }

    hit_, bb_diamond_adv_runner_result = advance_runner(hit_,
                                                        bb_diamond_adv_runner,
                                                        )

    assert bb_diamond_adv_runner_result == {'h_g': 1,
                                            'b1_g': 0,
                                            'b2_g': 0,
                                            'b3_g': 1,
                                            }


def test_advance_runner_homer_b1():

    """Test Homerun, person on first base
    """

    hit_ = ('hit - home run', 4, 'Home Run!!!')
    bb_diamond_adv_runner = {'h_g': 0,
                             'b1_g': 1,
                             'b2_g': 0,
                             'b3_g': 0,
                             }

    hit_, bb_diamond_adv_runner_result = advance_runner(hit_,
                                                        bb_diamond_adv_runner,
                                                        )

    assert bb_diamond_adv_runner_result == {'h_g': 2,
                                            'b1_g': 0,
                                            'b2_g': 0,
                                            'b3_g': 0,
                                            }

# When runner on second base


def test_advance_runner_single_b2():

    """Test Single, person on second base
    """

    hit_ = ('hit - single', 1, 'Hit! A Single',)
    bb_diamond_adv_runner = {'h_g': 0,
                             'b1_g': 0,
                             'b2_g': 1,
                             'b3_g': 0,
                             }

    hit_, bb_diamond_adv_runner_result = advance_runner(hit_,
                                                        bb_diamond_adv_runner,
                                                        )

    assert bb_diamond_adv_runner_result == {'h_g': 0,
                                            'b1_g': 1,
                                            'b2_g': 0,
                                            'b3_g': 1,
                                            }


def test_advance_runner_double_b2():

    """Test Double, person on second base
    """

    hit_ = ('hit - double', 2, 'Hit! A Double',)
    bb_diamond_adv_runner = {'h_g': 0,
                             'b1_g': 0,
                             'b2_g': 1,
                             'b3_g': 0,
                             }

    hit_, bb_diamond_adv_runner_result = advance_runner(hit_,
                                                        bb_diamond_adv_runner,
                                                        )

    assert bb_diamond_adv_runner_result == {'h_g': 1,
                                            'b1_g': 0,
                                            'b2_g': 1,
                                            'b3_g': 0,
                                            }


def test_advance_runner_triple_b2():

    """Test Triple, person on second base
    """

    hit_ = ('hit - triple', 3, 'Hit! A Triple',)
    bb_diamond_adv_runner = {'h_g': 0,
                             'b1_g': 0,
                             'b2_g': 1,
                             'b3_g': 0,
                             }

    hit_, bb_diamond_adv_runner_result = advance_runner(hit_,
                                                        bb_diamond_adv_runner,
                                                        )

    assert bb_diamond_adv_runner_result == {'h_g': 1,
                                            'b1_g': 0,
                                            'b2_g': 0,
                                            'b3_g': 1,
                                            }


def test_advance_runner_homer_b2():

    """Test Homerun, person on second base
    """

    hit_ = ('hit - home run', 4, 'Home Run!!!')
    bb_diamond_adv_runner = {'h_g': 0,
                             'b1_g': 0,
                             'b2_g': 1,
                             'b3_g': 0,
                             }

    hit_, bb_diamond_adv_runner_result = advance_runner(hit_,
                                                        bb_diamond_adv_runner,
                                                        )

    assert bb_diamond_adv_runner_result == {'h_g': 2,
                                            'b1_g': 0,
                                            'b2_g': 0,
                                            'b3_g': 0,
                                            }

#################################
#################################
#################################

# When runner on third base


def test_advance_runner_single_b3():

    """Test Single, person on third base
    """

    hit_ = ('hit - single', 1, 'Hit! A Single',)
    bb_diamond_adv_runner = {'h_g': 0,
                             'b1_g': 0,
                             'b2_g': 0,
                             'b3_g': 1,
                             }

    hit_, bb_diamond_adv_runner_result = advance_runner(hit_,
                                                        bb_diamond_adv_runner,
                                                        )

    assert bb_diamond_adv_runner_result == {'h_g': 1,
                                            'b1_g': 1,
                                            'b2_g': 0,
                                            'b3_g': 0,
                                            }


def test_advance_runner_double_b3():

    """Test Double, person on third base
    """

    hit_ = ('hit - double', 2, 'Hit! A Double',)
    bb_diamond_adv_runner = {'h_g': 0,
                             'b1_g': 0,
                             'b2_g': 0,
                             'b3_g': 1,
                             }

    hit_, bb_diamond_adv_runner_result = advance_runner(hit_,
                                                        bb_diamond_adv_runner,
                                                        )

    assert bb_diamond_adv_runner_result == {'h_g': 1,
                                            'b1_g': 0,
                                            'b2_g': 1,
                                            'b3_g': 0,
                                            }


def test_advance_runner_triple_b3():

    """Test Triple, person on third base
    """

    hit_ = ('hit - triple', 3, 'Hit! A Triple',)
    bb_diamond_adv_runner = {'h_g': 0,
                             'b1_g': 0,
                             'b2_g': 0,
                             'b3_g': 1,
                             }

    hit_, bb_diamond_adv_runner_result = advance_runner(hit_,
                                                        bb_diamond_adv_runner,
                                                        )

    assert bb_diamond_adv_runner_result == {'h_g': 1,
                                            'b1_g': 0,
                                            'b2_g': 0,
                                            'b3_g': 1,
                                            }


def test_advance_runner_homer_b3():

    """Test Homerun, person on third base
    """

    hit_ = ('hit - home run', 4, 'Home Run!!!')
    bb_diamond_adv_runner = {'h_g': 0,
                             'b1_g': 0,
                             'b2_g': 0,
                             'b3_g': 1,
                             }

    hit_, bb_diamond_adv_runner_result = advance_runner(hit_,
                                                        bb_diamond_adv_runner,
                                                        )

    assert bb_diamond_adv_runner_result == {'h_g': 2,
                                            'b1_g': 0,
                                            'b2_g': 0,
                                            'b3_g': 0,
                                            }
