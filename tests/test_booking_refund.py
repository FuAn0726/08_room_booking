from src.booking_refund import is_refundable
import pytest

@pytest.mark.parametrize(
    "hours, flexible, expected",
    [
        (72, True, True),  # flexible, well before check in
        (48, True, True),  # flexible, exactly 48 hours
        (47, True, False),  # flexible, 47 hours
        (72, False, False),  # nonflexible, 72 hours
    ],
)
def test_is_refundable_with_valid_input_returns_bool(hours, flexible, expected):
    # Act
    result = is_refundable(hours, flexible)

    # Assert
    assert result is expected

def test_is_refundable_with_negative_hours_raises_value_error():
    # Arrange
    hours = -1
    flexible = True

    # Act and assert
    with pytest.raises(ValueError):
        is_refundable(hours, flexible)

@pytest.mark.parametrize(
    "hours, flexible",
    [
        (48.0, True),  # hours is float
        (True, True),  # hours is bool
        (72, 1),  # flexible is int
    ],
)
def test_is_refundable_with_invalid_type_raises_type_error(hours, flexible):
    # Act and assert
    with pytest.raises(TypeError):
        is_refundable(hours, flexible)
