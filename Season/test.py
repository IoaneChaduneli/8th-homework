from datetime import datetime, date, time
import inflect

# today = datetime.now()
# x = input(": ")
# x = datetime.fromisoformat(x)
# passed = today - x
# print(passed.days)
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

x = '2020-02-02'
y = '2023-04-07'

result = datetime.fromisoformat(y) - datetime.fromisoformat(x)

print(result)

x = datetime.now()
y = '2020-02-02'

expected = x - datetime.fromisoformat(y)

print(expected)