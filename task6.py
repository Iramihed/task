#Известны год, номер месяца и день рождения каждого
# из двух человек. Определить, кто из них старше.

import datetime
a=datetime.datetime(2012,12,20)
b=datetime.datetime(1989,12,10)
if a<b:
    print("первый старше")
else:
    b>a
    print("второй старше")