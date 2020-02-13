"""
Test Suite
"""
from baseball_funcs.game_set_up import (team_description_func,
                                        players_tuple_func,
                                        )

from baseball_funcs.base_running import advance_runner

print("=" * 70)

print(f'TESTING!!!')


def test00_00():

    assert team_description_func == ('VISITORS', 'HOME')


def test00_01():

    xy = 232

    assert xy == 232


def test00_02():

    assert players_tuple_func == ("Pitcher",
                                  "Catcher",
                                  "First Base",
                                  "Second Base",
                                  "Third Base",
                                  "Shortstop",
                                  "Left Field",
                                  "Center Field",
                                  "Right Field",)


def test_advance_runner_single():

    """Test Single, no person on base
    """

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
