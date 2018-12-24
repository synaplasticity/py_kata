from HouseRent.house_rent_calc import rent_for_years


def test_rent_for_3year_interval():
    assert rent_for_years(35000, 1.5) == 35000


def test_rent_for_3year_interval_for_4years():
    assert rent_for_years(35000, 15, increase_interval=3, years=4) == 40250


def test_rent_for_3year_interval_for_7years():
    assert rent_for_years(35000, 15, increase_interval=3, years=7) == 46287.5


def test_rent_for_3year_interval_for_10years():
    assert rent_for_years(35000, 15, increase_interval=3, years=10) == 53230.62
