import pandas as pd
import plotly.express as px

data = pd.read_csv('rocket-data.csv')

companys = data['company'].values,
count = data['company'].value_counts().reset_index(),
outcomes = data['outcome'].value_counts().reset_index(),
                     
fig = px.sunburst(data, path=['company', 'outcome'])

fig.show()