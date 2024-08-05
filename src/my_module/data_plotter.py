import pandas as pd
import matplotlib.pyplot as plt

def plot_stock_data(stock_data: pd.DataFrame, output_file: str):
    """
    株価データのグラフを作成し、指定されたファイルに保存する。

    Args:
        stock_data (pd.DataFrame): 株価データ
        output_file (str): 保存するファイルのパス
    """
    plt.figure(figsize=(14, 7))
    plt.plot(stock_data['Close'], label='Close Price')
    plt.plot(stock_data['SMA_50'], label='50-Day SMA')
    plt.plot(stock_data['SMA_200'], label='200-Day SMA')
    plt.title('Stock Price and Moving Averages')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid()
    plt.savefig(output_file)
    plt.close()
