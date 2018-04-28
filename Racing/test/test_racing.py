from Racing.racing import race


def test_runner_1_at_0_speed():
    assert race(0, 1, 1) is None


def test_runner_2_at_0_speed():
    assert race(1, 0, 1) is None


def test_lead_at_0_distance():
    assert race(1, 1, 0) is None


def test_first_has_to_be_slower_than_second():
    assert race(2, 1, 1) is None

def test_time_required_for_catchup():
    race(720, 850, 70)
