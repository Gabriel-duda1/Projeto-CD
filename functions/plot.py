import yfinance as yf
import plotly.express as px

def plot_price(ticker):
    """
    A function to plot the close price given a ticker.
    """

    data = yf.download(
        ticker,
        multi_level_index = False
    )

    fig = px.line(
        data.reset_index(),
        x = 'Date', y = ['Close']
    )

    return fig