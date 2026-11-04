import pytest
from unittest.mock import patch
from statistic_calculator import (
    calculate_mean,
    calculate_median,
    calculate_mode,
    calculate_range,
    calculate_variance,
    calculate_std_dev,
    get_user_data,
)

def test_calculate_mean():
    assert calculate_mean([10, 20, 30, 40, 50]) == 30.0

def test_calculate_median_odd():
    # Odd number of elements: middle value is 11
    assert calculate_median([15, 3, 9, 22, 11]) == 11.0

def test_calculate_median_even():
    # Even number of elements: average of 20 and 30
    assert calculate_median([10, 20, 30, 40]) == 25.0

def test_calculate_mode_single():
    assert calculate_mode([1, 2, 2, 3, 4]) == 2.0

def test_calculate_mode_multiple():
    # Both 2 and 3 appear twice
    modes = calculate_mode([1, 2, 2, 3, 3, 4])
    assert set(modes) == {2.0, 3.0}

def test_calculate_mode_none():
    # All items appear only once
    assert "No mode" in calculate_mode([1, 2, 3, 4])

def test_calculate_range():
    assert calculate_range([5, 10, 2, 20]) == 18.0

def test_calculate_variance_and_std_dev():
    data = [2, 4, 4, 4, 5, 5, 7, 9]
    variance = calculate_variance(data, is_sample=True)
    std_dev = calculate_std_dev(variance)
    
    # Check approximate values for sample variance and standard deviation
    assert pytest.approx(variance, 0.01) == 4.57
    assert pytest.approx(std_dev, 0.01) == 2.14

def test_get_user_data_mock():
    # Simulate user typing two numbers then 'done'
    user_inputs = iter(["12.5", "7.5", "done"])
    with patch("builtins.input", lambda _: next(user_inputs)):
        data = get_user_data()
        assert data == [12.5, 7.5]