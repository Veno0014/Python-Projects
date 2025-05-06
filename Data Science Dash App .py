import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
import webbrowser
from threading import Timer
import os

# Load the data
current_directory = os.getcwd()
file_path = os.path.join(current_directory, "netflix_titles.xlsx")
netflix_df = pd.read_excel(file_path)

# Process data
netflix_df['release_year'] = pd.to_numeric(netflix_df['release_year'], errors='coerce')
netflix_df = netflix_df.dropna(subset=['release_year', 'type'])

if 'duration' in netflix_df.columns:
    netflix_df['duration'] = netflix_df['duration'].astype(str).str.extract(r'(\d+)')[0]
    netflix_df['duration'] = pd.to_numeric(netflix_df['duration'], errors='coerce')

# Helper function for country data
def get_content_by_country(df):
    country_count = df['country'].dropna().str.split(', ').explode().value_counts().reset_index()
    country_count.columns = ['Country', 'Count']
    return country_count

# Initialize Dash app
app = dash.Dash(__name__)
app.title = "Netflix Movie/Series Dashboard"

# Layout
app.layout = html.Div([
    html.H2("The Netflix Content Dashboard", style={'textAlign': 'center', 'color':   '#d91619'}),
    
    html.Div([
        html.Label('Select Year, Movie or TV Show:', style={'font-weight': 'bold'}),
        dcc.Dropdown(
            id='selection-dropdown',
            options=[
                {'label': 'Movie', 'value': 'Movie'},
                {'label': 'TV Show', 'value': 'TV Show'}
            ] + [{'label': str(int(year)), 'value': int(year)} for year in sorted(netflix_df['release_year'].dropna().unique(), reverse=True)],
            value='Movie',
            style={'width': '60%', 'margin': 'auto'}
        )
    ], style={'padding': '22px', 'textAlign': 'center'}),
    
    dcc.Graph(id='bar-graph'),
    dcc.Graph(id='scatter-graph'),
    dcc.Graph(id='chloro-graph'),
])

# Callback to update the graphs
@app.callback(
    [
        Output('bar-graph', 'figure'),
        Output('scatter-graph', 'figure'),
        Output('chloro-graph', 'figure')
    ],
    Input('selection-dropdown', 'value')
)
def update_graphs(selection):
    # Filtered dataset
    if selection == 'Movie' or selection == 'TV Show':
        filtered_df = netflix_df[netflix_df['type'] == selection]
    else:
        filtered_df = netflix_df[netflix_df['release_year'] == selection]

    # Constructs Bar Graph
    if selection == 'Movie' or selection == 'TV Show':
        year_counts = filtered_df['release_year'].value_counts().sort_index()
        bar_fig = px.bar(
            x=year_counts.index,
            y=year_counts.values,
            labels={'x': 'Release Year', 'y': f'Number of {selection}s'},
            title=f"{selection}s /Series Released Over Years",
            color_discrete_sequence=['#d91619']
        )
    else:
        type_counts = filtered_df['type'].value_counts()
        bar_fig = px.bar(
            x=type_counts.index,
            y=type_counts.values,
            labels={'x': 'Type', 'y': 'Number of Titles'},
            title=f"Content Released in {selection}",
            color_discrete_sequence=['#d91619']
        )

    # Constructs Scatter Plot (Duration vs Year)
    scatter_fig = px.scatter(
        filtered_df.dropna(subset=['duration']),
        x='release_year',
        y='duration',
        title='Content Duration Patterns',
        color='duration',
        color_continuous_scale='Viridis'
    )

    # Constructs Choropleth Map (Content by Country)
    country_data = get_content_by_country(filtered_df)
    chloro_fig = px.choropleth(
        country_data,
        locations='Country',
        locationmode='country names',
        color='Count',
        color_continuous_scale='reds',
        title='Content Distributed by Country'
    )

    # Improves Layouts
    for fig in [bar_fig, scatter_fig, chloro_fig]:
        fig.update_layout(
            paper_bgcolor="#ffffff",
            plot_bgcolor="#f9f9f9",
            font=dict(color="#2c3e50"),
            margin=dict(t=40, b=40, l=40, r=40)
        )

    return bar_fig, scatter_fig, chloro_fig

# Auto-open browser
def open_browser():
    webbrowser.open_new("http://127.0.0.1:8050/")

# Run app
if __name__ == '__main__':
    Timer(1, open_browser).start()
    app.run(debug=False)
