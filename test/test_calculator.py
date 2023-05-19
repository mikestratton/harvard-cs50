from calculator import raise_to_power_of
from calculator import square


def test_raise_to_power_of():
    assert raise_to_power_of(2, 2) == 4
    assert raise_to_power_of(3, 2) == 9
    assert raise_to_power_of(-2, 2) == 4
    assert raise_to_power_of(-3, 2) == 9


def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(0) == 0

