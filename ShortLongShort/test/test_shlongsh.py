from ShortLongShort.short_long_short import sls


def test_first_is_short():
    print(sls("1", "22"))
    assert sls("1", "22") == "1221"
