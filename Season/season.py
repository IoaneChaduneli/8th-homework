from datetime import datetime
import inflect, sys

def calculate_days(birth_date, today = datetime.now()):
    birth_date_of_iso = datetime.fromisoformat(birth_date)
    passed_days = (today - birth_date_of_iso)
    return passed_days

def calculate_minutes(passed_days):
    if passed_days.days > 0:
        list_of_passed_days = str(passed_days).split(' ')
        days = float(list_of_passed_days[0])
        list_of_hour_minutes_seconds = str(list_of_passed_days[2]).split(':')
        hours = float(list_of_hour_minutes_seconds[0])
        minutes = float(list_of_hour_minutes_seconds[1])
        
        total_minutes = round(days * 24 * 60) + (hours * 60) + minutes
        return int(total_minutes)
        
    else:
        return 'Zero Minutes'
        

def convet_number_to_words(minute):
    converter_of_letter = inflect.engine().number_to_words(minute, andword='')
    return f'{converter_of_letter} minutes'

def main():
    date_of_birth = input('Enter Date of birth (yyyy-mm-dd): ')
    try:
        if datetime.fromisoformat(date_of_birth):
            calculate_day = calculate_days(date_of_birth)
            calculate_minute = calculate_minutes(calculate_day)
            result = convet_number_to_words(calculate_minute)
            print(result)
            

    except ValueError as e:
        sys.exit(f'{e} is not ISO format input')

if __name__ == '__main__':
    main()
