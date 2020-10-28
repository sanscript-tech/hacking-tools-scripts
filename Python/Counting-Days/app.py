from datetime import date
import sys

if len(sys.argv) < 2:
    print("Please provide date as commandline argument.")
    sys.exit()

target_date = map(int, sys.argv[1].split("/")[::-1])
current_date = date.today()
target_date = date(*target_date)
delta = target_date - current_date

print(f'{delta.days} days left until {target_date}')
