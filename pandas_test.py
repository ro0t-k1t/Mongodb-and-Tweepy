__author__ = 'ronanpiercehiggins'


import pandas as pd
import datetime
from pandas_datareader import data
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

web_stats = {'Day':[1,2,3,4,5,6],
             'Visitors':[43,34,65,56,29,76],
             'Bounce Rate':[65,67,78,65,45,52]}

df = pd.DataFrame(web_stats)


start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2015, 8, 22)

df.set_index('Day', inplace=True)

#df = data.DataReader("XOM", "yahoo", start, end)

print(df.head())
print(df.head(2))

print(df['Visitors'])

df.plot()
plt.show()

"""df['High'].plot()
plt.legend()
plt.show()"""









