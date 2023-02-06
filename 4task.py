#Известны год, номер месяца и день рождения человека,
# а также день, год и номер месяца сегодняшнего дня.
# Определите возраст человека (число полных лет).

import datetime
a = datetime.date(year=1997, month=7, day=31)
b = datetime.date(year=datetime.date.today().year, month=datetime.date.today().month, day=datetime.date.today().day)
print(int((b - a).days / 365))