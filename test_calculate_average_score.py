### Unit Tests
# test_calculate_average_score.py
import pytest
from clean_code_examples import calculate_average_score

# --- Happy path tests ---


def test_basic_average():
    """Test that average is calculated correctly for a normal list."""
    result = calculate_average_score([80, 90, 70], passing_threshold=70)
    assert result["average"] == 80.0


def test_pass_rate_all_passing():
    """Test pass rate when all scores are above the threshold."""
    result = calculate_average_score([80, 90, 100], passing_threshold=70)
    assert result["pass_rate"] == 100.0


def test_pass_rate_none_passing():
    """Test pass rate when no scores meet the threshold."""
    result = calculate_average_score([40, 50, 60], passing_threshold=70)
    assert result["pass_rate"] == 0.0


def test_highest_and_lowest():
    """Test that highest and lowest scores are returned correctly."""
    result = calculate_average_score([55, 72, 88, 91], passing_threshold=70)
    assert result["highest"] == 91
    assert result["lowest"] == 55


def test_single_score():
    """Test that a single score returns correct results."""
    result = calculate_average_score([75], passing_threshold=70)
    assert result["average"] == 75.0
    assert result["pass_rate"] == 100.0


# --- Edge case tests ---


def test_empty_list_raises_error():
    """Test that an empty list raises a ValueError."""
    with pytest.raises(ValueError, match="cannot be empty"):
        calculate_average_score([], passing_threshold=70)


def test_non_numeric_score_raises_error():
    """Test that a non-numeric score raises a TypeError."""
    with pytest.raises(TypeError):
        calculate_average_score([80, "ninety", 70], passing_threshold=70)


def test_score_above_100_raises_error():
    """Test that a score above 100 raises a ValueError."""
    with pytest.raises(ValueError, match="between 0 and 100"):
        calculate_average_score([80, 105, 70], passing_threshold=70)


def test_negative_score_raises_error():
    """Test that a negative score raises a ValueError."""
    with pytest.raises(ValueError):
        calculate_average_score([-5, 80, 70], passing_threshold=70)


def test_invalid_threshold_raises_error():
    """Test that an out-of-range threshold raises a ValueError."""
    with pytest.raises(ValueError):
        calculate_average_score([80, 90, 70], passing_threshold=110)


def test_none_input_raises_error():
    """Test that None input raises a TypeError."""
    with pytest.raises(TypeError):
        calculate_average_score(None, passing_threshold=70)


def test_boundary_score_exactly_at_threshold():
    """Test that a score exactly equal to the threshold counts as passing."""
    result = calculate_average_score([70, 80, 90], passing_threshold=70)
    assert result["pass_rate"] == 100.0
