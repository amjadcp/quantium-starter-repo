from dash.testing.composite import DashComposite
from visualise_pink_morsels_daily_sales import app

def test_header_exists(dash_duo):
    # Start the app
    dash_duo.start_server(app)
    
    # 1. Check if the header is present and contains correct text
    # We look for the H1 tag
    header = dash_duo.find_element("h1")
    
    assert header.text == "Pink Morsel Sales Visualiser"
    assert header.is_displayed()

def test_visualisation_exists(dash_duo):
    dash_duo.start_server(app)
    
    # 2. Check if the Graph component is present
    # We look for the ID assigned in dcc.Graph
    visualiser = dash_duo.find_element("#sales-line-chart")
    
    assert visualiser.is_displayed()

def test_region_picker_exists(dash_duo):
    dash_duo.start_server(app)
    
    # 3. Check if the RadioItems (region picker) is present
    # We look for the ID assigned in dcc.RadioItems
    region_picker = dash_duo.find_element("#region-filter")
    
    assert region_picker.is_displayed()
