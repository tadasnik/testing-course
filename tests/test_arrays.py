import pytest
from code.arrays import add_arrays, subtract_arrays, multiply_arrays, divide_arrays


@pytest.mark.parametrize(
    "a, b, expect",
    [
        ([1, 2, 3], [4, 5, 6], [5, 7, 9]),
        ([-1, -5, -3], [-4, -3, 0], [-5, -8, -3]),
        ([6, 6, 6], [8, 8, 8], [14, 14, 14]),
    ],
)
@pytest.mark.parametrize(
    "a, b, expect",
    [
        ([2, 3, 4], [1, 1, 1], [1, 2, 3]),
    ],
)
def test_subtract_arrays(a, b, expect):
    output = subtract_arrays(a, b)

    assert output == expect, "fail subtraction"


def test_multiply_arrays():
    a = [1, 4, 5]
    b = [4, 3, 5]
    expect = [4, 12, 25]

    output = multiply_arrays(a, b)

    assert output == expect, "fail multiplication"


@pytest.mark.parametrize(
    "a, b, expect",
    [
        ([1, 2, 3], [4, 5, 6], [(1 / 4), (2 / 5), (3 / 6)]),
        ([0, 2, 3], [0, 5, 6], [0, (2 // 5), (3 // 6)]),
    ],
)
def test_divide_arrays(a, b, expect):
    output = divide_arrays(a, b)

    assert output == expect, "fail multiplication"


@pytest.mark.parametrize(
    "a, b, expected_error",
    [
        ([1, 2, 3], [4, 5, 6], [(1 / 4), (2 / 5), (3 / 6)]),
        ([0, 2, 3], [0, 5, 6], [0, (2 / 5), (3 / 6)]),
    ],
)
def test_divide_arrays_error(a, b, expect):
    output = divide_arrays(a, b)

    assert output == expect, "fail multiplication"


@pytest.fixture
def pair_of_lists():
    return [1, 2, 3], [4, 5, 6]


def test_add_arrays(pair_of_lists):
    a, b = pair_of_lists
    expect = [5, 7, 9]
    output = add_arrays(a, b)
    assert output == expect
