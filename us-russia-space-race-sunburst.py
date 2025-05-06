import pandas as pd
import plotly.express as px

us_data = all_data[all_data['company'] == 'NASA']
russia_data = all_data[all_data['company'] == 'RVSN USSR']

combined = pd.concat([us_data, russia_data])


fig = px.sunburst(combined, path=['company','outcome', 'date'])

fig.show()