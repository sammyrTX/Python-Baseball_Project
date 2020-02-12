"""
Test Suite
"""
from baseball_funcs.game_set_up import (team_description_func,
                                        players_tuple_func,
                                        )

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

print('End Testing...!')
