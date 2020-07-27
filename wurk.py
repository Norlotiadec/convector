import pandas as pd

df = pd.read_csv('acme_worksheet.csv', index_col='Date', parse_dates=True)
pvt = df.pivot_table(index=['Employee Name'], columns=['Date'], values='Work Hours', fill_value=int(0))

pvt.to_csv('out1.csv')
