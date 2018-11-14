from ShortLongShort.short_long_short import sls


def test_first_is_short():
    assert sls("1", "22") == "1221"
def test_second_is_short():
    assert sls("33", "4") == "4334"
