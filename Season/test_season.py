from season import calculate_minutes, calculate_days, convet_number_to_words
from datetime import timedelta, datetime

def test_calculate_days():
    birth_date = '1997-08-18'
    today = '2023-04-07'

    expected_days = datetime.fromisoformat(today) - datetime.fromisoformat(birth_date)
    actual_days = calculate_days(birth_date, today)

    assert actual_days == expected_days

def test_calculate_minutes():
    passed_days = timedelta(days=10, hours=5, minutes=30)
    expected_minutes = 14730
    actual_minutes = calculate_minutes(passed_days)
    assert actual_minutes == expected_minutes

def test_convert_number_to_words():
    number = 1671093.0
    expected_string = 'one million, six hundred seventy-one thousand ninety-three point zero minutes'
    actual_string = convet_number_to_words(number)

    assert actual_string == expected_string