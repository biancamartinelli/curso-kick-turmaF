from datetime import date, datetime, timedelta

hoje = date.today().weekday()

print(hoje.strftime("%d/%m/%y"))

print(hoje.strftime("%dd-%mm-%yy"))

print(hoje.strftime("%B %m, %Y"))