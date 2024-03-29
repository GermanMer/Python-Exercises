#Exercise 10: Calculate number of days between two given dates

#Given:
#2020-02-25
#date_1 = datetime(2020, 2, 25)
#2020-09-17
#date_2 = datetime(2020, 9, 17)

#Expected output:
#205 days

from datetime import datetime

date_1 = datetime(2020, 2, 25)
date_2 = datetime(2020, 9, 17)

day_dif = date_2 - date_1

print(day_dif.days, "days")
