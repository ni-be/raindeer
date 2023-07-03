"""
Unit tests for user_story_3.py.
"""
import pytest
import user_story_3


def test_plot_weather_parameters_annual_one():
    """
    Test for function user_story_3.plot_weather_parameters_annual(). Checks
    if the function throws an error if the list of years is not sorted.
    """
    with pytest.raises(AssertionError):
        user_story_3.plot_weather_parameters_annual([1923, 1925, 1924])
