import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html

# 1. Load the processed data
df = pd.read_csv('./processed_data/pink_morsels_daily_sales.csv')

# 2. Ensure date is a datetime object and sorted
df['date'] = pd.to_datetime(df['date'])
df = df.sort_values(by='date')

# 3. Initialize the Dash app
app = Dash(__name__)

# 4. Create the line chart
fig = px.line(
    df, 
    x='date', 
    y='sales($)', 
    color='region',
    title='Pink Morsel Sales Trends',
    labels={'sales($)': 'Total Sales ($)', 'date': 'Date', 'region': 'Region'}
)

# 5. Define the layout
app.layout = html.Div(children=[
    html.H1(
        children='Pink Morsel Visualiser',
        style={'textAlign': 'center', 'color': '#2c3e50', 'fontFamily': 'sans-serif'}
    ),

    dcc.Graph(
        id='sales-line-chart',
        figure=fig
    )
])

# 6. Run the app
if __name__ == '__main__':
    app.run(debug=True, port=3000)
