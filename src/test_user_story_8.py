"""
Unit tests for user_story_8.py.
"""
import numpy as np
import pytest
import user_story_8


def test_linear_regression_one():
    """
    Test 1 for function user_story_8.linear_regression(). Checks if the
    function returns the correct result for a small dataset.
    """
    x_data = np.asarray([2, 3, 4])
    y_data = np.asarray([7, 9, 11])
    assert user_story_8.linear_regression(x_data, y_data, 7) == 17.0


def test_linear_regression_two():
    """
    Test 2 for function user_story_8.linear_regression(). Checks if the
    function throws an error if x and y are of different lengths.
    """
    x_data = np.empty(2)
    y_data = np.empty(3)
    with pytest.raises(AssertionError):
        user_story_8.linear_regression(x_data, y_data, 1)
