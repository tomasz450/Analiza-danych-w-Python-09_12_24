import pandas as pd
import os

def fetch_financial_data(company='AMZN'):
    """
    This function fetches stock market quotations.
    """
    import pandas_datareader.data as web
    return web.DataReader(name=company, data_source='stooq')

google = fetch_financial_data('GOOGL')

google = google.reset_index()
google['Year'] = google['Date'].dt.year
google['Month'] = google['Date'].dt.month



data = pd.Timestamp.today()
data_dzis = data.strftime(format='%Y%m%d')


file_path = os.path.join(os.getcwd(), f'./statystyki_{data_dzis}.xlsx')
google[(google.Date > '2023-01-01') & (google.Date < '2023-12-31')].groupby('Month')['Close'].mean().to_excel(file_path)
print(f"plik zapisany do: {file_path}")
