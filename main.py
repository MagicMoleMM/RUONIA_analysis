import pandas as pd
import numpy as np
import datetime as dt

import matplotlib.pyplot as plt
import seaborn as sns
from pylab import rcParams
rcParams['figure.figsize'] = 6, 4

data = pd.read_excel('/Users/MagicMole/Downloads/RC_F11_01_2010_T14_03_2022.xlsx')

# data = data[data['StatusXML'] == 0]
data = data.iloc[:, :-2]
data = data[data['MinRate'] != 'NaN']
data = data.rename(columns={'DT': 'Data', 'ruo': 'RUONIA', 'vol': 'Volume',
                            'T': 'Amount of deals', 'C': 'Amount of banks'})

data['year'] = data['Data'].apply(lambda x: dt.datetime.strftime(x, '%Y'))
data['month'] = data['Data'].apply(lambda x: dt.datetime.strftime(x, '%m'))
data['day'] = data['Data'].apply(lambda x: dt.datetime.strftime(x, '%d'))
data['MY'] = data['Data'].apply(lambda x: dt.datetime.strftime(x, '%Y/%m'))

data_mean = data.groupby(['MY']).mean().sort_values(by='MY')
data_mean = round(data_mean, 2)
print(data)

sns.lineplot(x='Data', y='RUONIA', data=data)
sns.displot(data['RUONIA'], bins=10, kde=False)
sns.jointplot(x='RUONIA', y='Volume', data=data, kind='hex', gridsize=20)

fig, ax = plt.subplots(figsize=[8, 8])
sns.heatmap(data_mean, annot=True, fmt=".0f", linewidths=.5, cmap="YlGnBu", ax=ax)

plt.show()
