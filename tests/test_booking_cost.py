from src.booking_cost import calculate_booking_cost
import pytest

@pytest.mark.parametrize(
    "nights, rate, expected",
    [
        (3, 15000, 45000),  # typical stay
        (1, 20000, 20000),  # minimum nights
        (7, 10000, 70000),  # seven nights, no free night
        (30, 10000, 300000),  # maximum nights
        (5, 0, 0),  # zero rate
    ],
)
def test_calculate_booking_cost_with_valid_input_returns_total(nights, rate, expected):
    # Act
    result = calculate_booking_cost(nights, rate)

    # Assert
    assert result == expected

def test_calculate_booking_cost_with_valid_input_returns_int():
    # Arrange
    nights = 2
    rate = 12345

    # Act
    result = calculate_booking_cost(nights, rate)

    # Assert
    assert type(result) is int

@pytest.mark.parametrize(#hello
    "nights, rate",
    [
        (0, 10000),  # nights below minimum
        (31, 10000),  # nights above maximum
        (3, -1),  # negative rate
    ],
)
def test_calculate_booking_cost_with_out_of_range_input_raises_value_error(nights, rate):
    # Act and assert
    with pytest.raises(ValueError):
        calculate_booking_cost(nights, rate)

@pytest.mark.parametrize(#hello
    "nights, rate",
    [
        ("3", 10000),  # nights is string
        (True, 10000),  # nights is bool
        (3, 100.5),  # rate is float
        (3, True),  # rate is bool
    ],
)
def test_calculate_booking_cost_with_invalid_type_raises_type_error(nights, rate): #he
    # Act and assert
    with pytest.raises(TypeError):
        calculate_booking_cost(nights, rate)
