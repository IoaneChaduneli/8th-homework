from datetime import datetime, date, time
import inflect

today = datetime.now()
x = input(": ")
x = datetime.fromisoformat(x)
passed = today - x
print(passed.days)
# passed_list = str(passed).split(" ")
# days = float(passed_list[0])
# the = str(passed_list[2]).split(':')
# print((the))
# for t in the:
   
#     f = float(t)

# print(f)
# minutes = round((days * 24 * 60) + f)

# eng = f"{inflect.engine().number_to_words(minutes, andword='')} minutes"
# print(eng)