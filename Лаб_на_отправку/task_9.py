salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев

all_spend = spend
for i in  range(1, 10):
    all_spend += spend * (1 + increase)**i
need_money = all_spend - 10 * salary

print(round(need_money))