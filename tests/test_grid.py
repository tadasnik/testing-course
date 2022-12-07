from code.grid import Grid


def test_fill():
    """
    Test that a cell in the bulk of the grid is correct.
    """
    grid = Grid(4, 4)
    grid.fill(1, 2)
    grid.fill(1, 2)
    assert grid.nFilled() == 1
