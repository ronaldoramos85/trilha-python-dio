from datetime import date, datetime, time, timezone

'''

data = date(2023, 7, 10)
print(data)
print(date.today())


data_hora = datetime(2023, 7, 10)
print(data_hora)
print(datetime.today())

hora = time(10, 20, 0)
print(hora)



data_teste = date(2020,10,20)
print(f"data_teste : {data_teste}")
delta = date.today() - data_teste
print(f"Decorreram {delta} desde {data_teste} até hoje ({date.today()})")'''

print(f"Valor de today: {datetime.today()}")

print(f"Valor de datetime.now: {datetime.now()}")

print(f"Valor de datetime.utcnow: {datetime.utcnow()}")

print(f"Valor de datetime.now(timezone.utc): {datetime.now(timezone.utc)}")