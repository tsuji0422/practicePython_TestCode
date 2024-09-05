import sys
import os
from dotenv import load_dotenv

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from my_module import fetch_stock_data, analyze_stock_data, plot_stock_data

def main():
    """
    メイン関数。株価データの取得、解析、グラフ作成を行う。
    """
    # .envファイルのパスを指定して読み込む
    load_dotenv(".env")

    # 環境変数を取得
    ticker = os.getenv("ticker")
    start_date = os.getenv("start_date")
    end_date = os.getenv("end_date")
    
    # 株価データの取得
    stock_data = fetch_stock_data(ticker, start_date, end_date)
    
    # データの解析
    analysis_results = analyze_stock_data(stock_data)
    
    # グラフの作成と保存
    output_file = "out/stock_plot.png"
    plot_stock_data(analysis_results, output_file)

if __name__ == "__main__":
    main()
