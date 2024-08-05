import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../src'))

import pytest
import pandas as pd
from my_module import fetch_stock_data, analyze_stock_data, plot_stock_data
import os


#### テストフィクスチャ
# テスト関数が利用する共通のデータやリソースをセットアップする
# テスト関数が終了した後に後始末をする

@pytest.fixture
def stock_data():
    ticker      = "AAPL"
    start_date  = "2020-01-01"
    end_date    = "2020-12-31"
    return fetch_stock_data(ticker, start_date, end_date)


#### テストケース
# テスト関数名は test_ で始める
# テスト関数は assert 文を使ってテストを実行する
# テスト関数は pytest で実行される

def test_fetch_stock_data(stock_data):
    assert isinstance(stock_data, pd.DataFrame)
    assert not stock_data.empty

def test_analyze_stock_data(stock_data):
    analyzed_data = analyze_stock_data(stock_data)
    assert 'SMA_50' in analyzed_data.columns
    assert 'SMA_200' in analyzed_data.columns

def test_plot_stock_data(stock_data):
    analyzed_data = analyze_stock_data(stock_data)
    output_file = "test_stock_plot.png"
    plot_stock_data(analyzed_data, output_file)
    assert os.path.exists(output_file)
    os.remove(output_file)