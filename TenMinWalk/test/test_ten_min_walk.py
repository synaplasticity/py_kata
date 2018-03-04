from TenMinWalk.ten_min_walk import toggle_dir
from TenMinWalk.ten_min_walk import isValidWalk


def test_toogle_dir_north():
    assert toggle_dir('n') is 's'


def test_toogle_dir_south():
    assert toggle_dir('s') is 'n'


def test_toogle_dir_east():
    assert toggle_dir('e') is 'w'


def test_toogle_dir_west():
    assert toggle_dir('w') is 'e'


def test_less_than_ten_mins():
    assert isValidWalk(['n', 'e', 'w', 's']) is False


def test_greater_than_ten_mins():
    assert isValidWalk(['n', 'e', 'w', 's', 'n', 'e', 'w',
                       's', 'n', 'e', 'w', 's']) is False


def test_is_ten_mins():
    assert isValidWalk(['e', 'n', 'n', 'w', 'n', 'w',
                       's', 's', 's', 'e']) is True


def test_is_ten_mins_but_not_bak_to_origin():
    assert isValidWalk(['e', 'n', 'n', 'w', 'n', 'w',
                       's', 'n', 's', 'e']) is False
