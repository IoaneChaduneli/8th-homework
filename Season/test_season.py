from season import calculate_minutes, calculate_days, convet_number_to_words
from datetime import timedelta, datetime

def test_calculate_days():
    birth_date = '1997-08-18'
    today = '2023-04-07'

    birth_date_obj = datetime.fromisoformat(birth_date)
    today_obj = datetime.fromisoformat(today)

    expected_days = today_obj - birth_date_obj
    actual_days = calculate_days(today_obj,birth_date_obj )

    assert actual_days == expected_days
    
def test_calculate_minutes():
    passed_days = timedelta(days=10, hours=5, minutes=30)
    expected_minutes = 14730
    actual_minutes = calculate_minutes(passed_days)
    assert actual_minutes == expected_minutes

def test_convert_number_to_words():
    number = 123
    expected_string = 'one hundred, twenty three minutes'
    actual_string = convet_number_to_words(number)
    assert actual_string == expected_string
