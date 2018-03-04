from TenMinWalk.ten_min_walk import isValidWalk


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
