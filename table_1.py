import pandas as pd

df = pd.DataFrame({'Найменування товару':['Картопля', 'Картопля', 'Картопля',
                                            'Капуста', 'Капуста', 'Капуста', 
                                            'Цибуля', 'Цибуля', 'Цибуля', 
                                            'Мед', 'Мед', 'Мед', 
                                            'Часник', 'Часник', 'Часник', 
                                            'Яблука', 'Яблука', 'Яблука'],
                'Рік':[2013, 2014, 2015,
                       2013, 2014, 2015,
                       2013, 2014, 2015,
                       2013, 2014, 2015,
                       2013, 2014, 2015,
                       2013, 2014, 2015],
                'Середня ціна за місяць':[30.8, 35.0, 35.6, 
                                        36.6, 40.0, 36.6, 
                                        50.8, 50.5, 52.2, 
                                        880.0, 990.3, 1000, 
                                        256.0, 310.2, 313.4, 
                                        67.5, 86.5, 89.5],
                'Роздрібна ціна':[32, 32, 32,
                                39, 39, 39,
                                40, 40, 40,
                                450, 450, 450,
                                250, 250, 250,
                                60, 60, 60]})

def opentabble_1():
    df.to_excel('./table_1.xlsx')