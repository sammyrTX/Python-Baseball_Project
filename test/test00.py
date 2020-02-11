"""
Test Suite
"""
from baseball_funcs.game_set_up import (team_description_func,
                                        )

print(f'TESTING!!!')


def test00_00():

    assert team_description_func is ('VISITORS', 'HOME')


print('End Testing...!')
