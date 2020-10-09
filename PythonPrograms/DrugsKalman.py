import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('drug-use-by-age.csv', index_col='age')

plt.title('Drug use by age\nin USA')
plt.xlabel('Age')
plt.ylabel('Use')
plt.axis([0, 500, 11, 66])
# plt.plot(data, 'green', label='Målt')
# plt.plot(actualWeight, 'orange', label='Virkelig')
# plt.plot(weights, 'blue', label='Kalman')
# plt.legend()
# plt.show()
# print(df)

df['alcohol-frequency'].plot(kind='hist', bins=100)

print(df.assign(sepal_ratio=df['alcohol-use'] / df['alcohol-frequency']).head())

print(df.median(axis=None, skipna=None, level=None, numeric_only=None))
print(df.min(axis=None, skipna=None, level=None, numeric_only=None))
print(df.max(axis=None, skipna=None, level=None, numeric_only=None))