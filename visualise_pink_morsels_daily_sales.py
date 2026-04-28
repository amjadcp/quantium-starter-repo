import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output

# 1. Data Prep
df = pd.read_csv('processed_data/pink_morsels_daily_sales.csv')
df['date'] = pd.to_datetime(df['date'])
df = df.sort_values(by='date')

app = Dash(__name__)

# 2. App Layout
app.layout = html.Div(style={
    'backgroundColor': '#f8f9fa', 
    'padding': '40px', 
    'fontFamily': '"Segoe UI", Roboto, Helvetica, Arial, sans-serif'
}, children=[
    
    # Header
    html.H1(
        "Pink Morsel Sales Visualiser",
        style={'textAlign': 'center', 'color': '#2c3e50', 'marginBottom': '30px'}
    ),

    # Control Panel (Radio Buttons)
    html.Div(style={
        'backgroundColor': 'white',
        'padding': '20px',
        'borderRadius': '10px',
        'boxShadow': '0 4px 6px rgba(0,0,0,0.1)',
        'maxWidth': '600px',
        'margin': '0 auto 30px auto',
        'textAlign': 'center'
    }, children=[
        html.Label("Select Region:", style={'fontWeight': 'bold', 'marginRight': '15px'}),
        dcc.RadioItems(
            id='region-filter',
            options=[
                {'label': 'North', 'value': 'north'},
                {'label': 'East', 'value': 'east'},
                {'label': 'South', 'value': 'south'},
                {'label': 'West', 'value': 'west'},
                {'label': 'All', 'value': 'all'}
            ],
            value='all',
            inline=True,
            inputStyle={"margin-left": "20px", "margin-right": "5px"},
            style={'display': 'inline-block'}
        ),
    ]),

    # Graph Container
    html.Div(style={
        'backgroundColor': 'white',
        'padding': '20px',
        'borderRadius': '10px',
        'boxShadow': '0 4px 6px rgba(0,0,0,0.1)'
    }, children=[
        dcc.Graph(id='sales-line-chart')
    ])
])

# 3. Callback for Interactivity
@app.callback(
    Output('sales-line-chart', 'figure'),
    Input('region-filter', 'value')
)
def update_graph(selected_region):
    # Filter logic
    if selected_region == 'all':
        filtered_df = df
    else:
        filtered_df = df[df['region'] == selected_region]

    # Create figure
    fig = px.line(
        filtered_df, 
        x='date', 
        y='sales($)', 
        color='region' if selected_region == 'all' else None,
        line_shape='spline', # Makes the line look smoother
        render_mode='svg',
        labels={'sales($)': 'Total Sales ($)', 'date': 'Date', 'region': 'Region'}
    )

    # Modernize chart styling
    fig.update_layout(
        plot_bgcolor='white',
        paper_bgcolor='white',
        font_color='#2c3e50',
        margin=dict(l=40, r=40, t=40, b=40)
    )
    fig.update_xaxes(showgrid=True, gridcolor='#eee')
    fig.update_yaxes(showgrid=True, gridcolor='#eee')
    
    return fig

if __name__ == '__main__':
    app.run(debug=True, port=3000)
