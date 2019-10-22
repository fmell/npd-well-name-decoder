from ..npd import parse_wellbore_name


def test_parse_wellbore_name():
    EXAMPLE_WELLBORE_NAME = "1234/5-6 S"
    EXPECTED_RESULT = {
        "quadrant": 1234,
        "block": 5,
        "wellbore_id": None,
        "well_number": 6,
        "well_type": "S",
    }
    res = parse_wellbore_name(EXAMPLE_WELLBORE_NAME)
    assert res == EXPECTED_RESULT


def test_parse_wellbore_name_with_wellbore_id():
    EXAMPLE_WELLBORE_NAME = "1234/5-A-6 S"
    EXPECTED_RESULT = {
        "quadrant": 1234,
        "block": 5,
        "wellbore_id": "A",
        "well_number": 6,
        "well_type": "S",
    }
    res = parse_wellbore_name(EXAMPLE_WELLBORE_NAME)
    assert res == EXPECTED_RESULT
