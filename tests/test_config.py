import pytest

from app.config import parse_replicas


@pytest.mark.parametrize("value, expected", [
    ("1", 1),
    ("3", 3),
    ("5", 5),
    (" 2 ", 2),
])
def test_valid_replicas(value, expected):
    assert parse_replicas(value) == expected


@pytest.mark.parametrize("value", [
    "0", "-1", "6", "abc", "", "1.5",
])
def test_invalid_replicas(value):
    with pytest.raises(ValueError):
        parse_replicas(value)
