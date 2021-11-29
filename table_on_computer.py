from prettytable import PrettyTable

table = PrettyTable(['Товар','Рік','Середня ринкова ціна','Роздрібна ціна'])
table.add_row(["Капуста", "2013", 30.8, 32])
table.add_row(["Капуста", "2014", 35.0, 32])
table.add_row(["Капуста", "2015", 35.6, 32])

table.add_row(["Картопля", "2013", 36.6, 39])
table.add_row(["Картопля", "2014", 40.0, 39])
table.add_row(["Картопля", "2015", 36.6, 39])

table.add_row(["Цибуля", "2013", 50.8, 40])
table.add_row(["Цибуля", "2014", 50.5, 40])
table.add_row(["Цибуля", "2015", 52.2, 40])

table.add_row(["Мед", "2013", 880.0, 450])
table.add_row(["Мед", "2014", 990.3, 450])
table.add_row(["Мед", "2015", 1000, 450])

table.add_row(["Часник", "2013", 256.0, 250])
table.add_row(["Часник", "2014", 310.2, 250])
table.add_row(["Часник", "2015", 313.4, 250])

table.add_row(["Яблука", "2013", 67.5, 60])
table.add_row(["Яблука", "2014", 86.5, 60])
table.add_row(["Яблука", "2015", 89.5, 60])

def opentabble():
    print('\nАНАЛІЗ ЗМІНИ ЦІН')
    print(table)