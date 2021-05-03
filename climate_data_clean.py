

import pandas as pd
import numpy as np

pd.options.mode.chained_assignment = None
# default='warn'

file = pd.read_csv('TemperaturesByCountry.csv')



df=file[file['Country']=='Bangladesh']
#dataframe was filtered by taking only Bd's values


new_df=df.dropna(subset = ["AverageTemperature"])
print(new_df)
#all the rows with no average temperature value was dropped


new_df["dt"] = pd.to_datetime(new_df["dt"]).dt.strftime('%d/%m/%Y')
print(new_df.to_string())
#Dates in the dataframe were in two different formats.It was changed into one format.


new_df.rename(columns={'dt': 'Date', 'AverageTemperature': 'AvgTemp','AverageTemperatureUncertainty':'AvgTempUncertainty ' }, inplace=True)


new_df.to_csv('bd_climate.csv',index=False)





