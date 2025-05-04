import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots


data = pd.read_csv('another-adjusted.csv')

fig = px.scatter_map(data, lat='latitude', lon='longitude', hover_name='location', hover_data=['status', 'company', 'date', 'outcome', 'details', 'price'], color_discrete_sequence=['fuchsia'], zoom=3, height=300)

fig.update_layout(map_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()