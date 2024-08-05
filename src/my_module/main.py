import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from my_module import fetch_stock_data, analyze_stock_data, plot_stock_data

def main():
    """
    メイン関数。株価データの取得、解析、グラフ作成を行う。
    """
    ticker      = "AAPL"  # 例としてAppleのティッカーシンボルを使用
    start_date  = "2020-01-01"
    end_date    = "2021-01-01"
    
    # 株価データの取得
    stock_data = fetch_stock_data(ticker, start_date, end_date)
    
    # データの解析
    analysis_results = analyze_stock_data(stock_data)
    
    # グラフの作成と保存
    output_file = "out/stock_plot.png"
    plot_stock_data(analysis_results, output_file)

if __name__ == "__main__":
    main()
