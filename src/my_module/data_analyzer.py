import pandas as pd

def analyze_stock_data(stock_data: pd.DataFrame) -> pd.DataFrame:
    """
    取得した株価データを解析する。

    Args:
        stock_data (pd.DataFrame): 株価データ

    Returns:
        pd.DataFrame: 解析結果のDataFrame
    """
    stock_data['SMA_50']    = stock_data['Close'].rolling(window=50).mean()
    stock_data['SMA_200']   = stock_data['Close'].rolling(window=200).mean()
    return stock_data
