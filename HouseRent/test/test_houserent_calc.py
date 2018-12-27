from HouseRent.house_rent_calc import rent_per_month
from HouseRent.house_rent_calc import annual_rent_for_period


def test_rent_for_1year_interval():
    assert rent_per_month(35000, 1.5) == 35000


def test_rent_for_3year_interval_for_3years():
    assert rent_per_month(35000, 1.5, increase_interval=3, years=3) == 35000


def test_rent_for_3year_interval_for_4years():
    assert rent_per_month(35000, 15, increase_interval=3, years=4) == 40250


def test_rent_for_3year_interval_for_7years():
    assert rent_per_month(35000, 15, increase_interval=3, years=7) == 46287.5


def test_rent_for_3year_interval_for_10years():
    assert rent_per_month(35000, 15, increase_interval=3, years=10) == 53230.62


def test_rent_for_3year_interval_for_16years():
    assert rent_per_month(35000, 15, increase_interval=3, years=16) == 70397.50


def test_annual_rent_for_3years():
    assert (annual_rent_for_period(35000, 15, increase_interval=3, years=3) ==
            35000 * 12 * 3)
