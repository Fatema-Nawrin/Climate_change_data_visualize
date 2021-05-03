

import pandas as pd
import numpy as np
pd.options.mode.chained_assignment = None

file = pd.read_csv('TemperaturesByCountry.csv')

df=file[file['Country']=='United Kingdom']

new_df=df.dropna(subset = ["AverageTemperature"])
print(new_df)


new_df["dt"] = pd.to_datetime(new_df["dt"]).dt.strftime('%d/%m/%Y')
print(new_df.to_string())


new_df.rename(columns={'dt': 'Date', 'AverageTemperature': 'AvgTemp','AverageTemperatureUncertainty':'AvgTempUncertainty ' }, inplace=True)

new_df.to_csv('uk_climate.csv',index=False)






