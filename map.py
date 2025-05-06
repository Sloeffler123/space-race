import pandas as pd
import plotly.express as px

us_data = pd.read_csv('us-space-race-data.csv')
russia_data = pd.read_csv('russia-space-race-data.csv')

combined = pd.concat([us_data, russia_data])

fig = px.line(combined, x='year', y='date', color='company', hover_data=['details', 'outcome', 'location'], markers=True)

fig.show()