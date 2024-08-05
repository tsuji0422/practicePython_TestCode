import yfinance as yf
import pandas as pd

def fetch_stock_data(ticker: str, start_date: str, end_date: str) -> pd.DataFrame:
    """
    指定されたティッカーシンボルの株価データをYahoo Financeから取得する。

    Args:
        ticker (str): 株のティッカーシンボル
        start_date (str): データ取得の開始日 (YYYY-MM-DD)
        end_date (str): データ取得の終了日   (YYYY-MM-DD)

    Returns:
        pd.DataFrame: 株価データのDataFrame
    """
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    return stock_data
