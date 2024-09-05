# テストコードについて

## 基本的なテストの種類

- ユニットテスト（Unit Testing）
  - 単一の機能やメソッドが正しく動作するかを検証します。
  - 依存関係から切り離して、個々の機能を独立してテストします。
  - 例: fetch_stock_data 関数が正しくデータを取得するかをテストする。

- 統合テスト（Integration Testing）
    - 複数のコンポーネントが正しく連携して動作するかを検証します。
    - 依存するモジュールや外部システムと一緒にテストします。
    - 例: fetch_stock_data と analyze_stock_data を組み合わせてテストする。

- 機能テスト（Functional Testing）
    - ソフトウェアの特定の機能が要求通りに動作するかを検証します。
    - ユーザーの視点から見た機能全体をテストします。
    - 例: 株価データの取得から解析、グラフ生成までの全体の流れをテストする。

- システムテスト（System Testing）
    - システム全体が要求通りに動作するかを検証します。
    - 開発環境ではなく、できるだけ本番環境に近い環境でテストします。

- 受け入れテスト（Acceptance Testing）
    - ユーザーの要求を満たしているかどうかを検証します。
    - 最終的な確認のために実施されます。

## テスト設計のアプローチ

- ホワイトボックステスト（White-box Testing）
    - コードの内部構造や動作を理解した上でテストを設計します。
    - 例: 各分岐やループを網羅するテストを作成する。

- ブラックボックステスト（Black-box Testing）
    - コードの内部構造を知らずに、外部から見た機能や振る舞いに基づいてテストを設計します。
    - 例: 入力と出力の関係をテストする。




# Pythonのテストフレームワークについて

- unittest
  - 標準ライブラリ: Pythonに標準で組み込まれているため、追加のインストールが不要です。
  - シンプル: 基本的なテストを書くには十分で、直感的に使えます。
- pytest
  - 柔軟性: より複雑なテストケースに対応しやすく、シンプルなテストも書きやすい。
  - 豊富な機能: フィクスチャやマーカ、プラグインなどの強力な機能を持っており、大規模なプロジェクトにも適しています。
  - 普及率: 現在では多くのプロジェクトで採用されており、コミュニティのサポートも充実しています。

# pytestについて

前提知識を共有したので、やっと本題に入る

<details>
<summary>作成されたテストコードに対する詳解</summary>
もちろんです。`pytest` で作成したテストコードの詳細な解説を行います。

### テストコード全体

以下が `pytest` で作成したテストコードの全体です。

```python
import pytest
import pandas as pd
from my_module.data_fetcher import fetch_stock_data
from my_module.data_analyzer import analyze_stock_data
from my_module.data_plotter import plot_stock_data
import os

@pytest.fixture
def stock_data():
    ticker = "AAPL"
    start_date = "2020-01-01"
    end_date = "2020-12-31"
    return fetch_stock_data(ticker, start_date, end_date)

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
```

### 詳細な解説

#### インポート文

```python
import pytest
import pandas as pd
from my_module.data_fetcher import fetch_stock_data
from my_module.data_analyzer import analyze_stock_data
from my_module.data_plotter import plot_stock_data
import os
```

- `pytest`: `pytest` テストフレームワークを使用するためのインポート。
- `pandas`: DataFrameを操作するためのインポート。
- `my_module.data_fetcher`, `my_module.data_analyzer`, `my_module.data_plotter`: テスト対象の関数を含むモジュールのインポート。
- `os`: ファイル操作のための標準ライブラリ。

#### `pytest` のフィクスチャ

```python
@pytest.fixture
def stock_data():
    ticker = "AAPL"
    start_date = "2020-01-01"
    end_date = "2020-12-31"
    return fetch_stock_data(ticker, start_date, end_date)
```

- `@pytest.fixture`: テストで使う共通の初期データを提供するためのデコレータ。ここでは `stock_data` という名前のフィクスチャを定義しています。
- `stock_data` 関数: テストで使用する株価データを取得し、DataFrameとして返します。このフィクスチャは後続のテストで再利用されます。

#### `test_fetch_stock_data`

```python
def test_fetch_stock_data(stock_data):
    assert isinstance(stock_data, pd.DataFrame)
    assert not stock_data.empty
```

- `test_fetch_stock_data`: `fetch_stock_data` 関数をテストします。
- `assert isinstance(stock_data, pd.DataFrame)`: `fetch_stock_data` が返す値が `DataFrame` 型であることを確認します。
- `assert not stock_data.empty`: 返された `DataFrame` が空でないことを確認します。

#### `test_analyze_stock_data`

```python
def test_analyze_stock_data(stock_data):
    analyzed_data = analyze_stock_data(stock_data)
    assert 'SMA_50' in analyzed_data.columns
    assert 'SMA_200' in analyzed_data.columns
```

- `test_analyze_stock_data`: `analyze_stock_data` 関数をテストします。
- `analyzed_data = analyze_stock_data(stock_data)`: `stock_data` を入力として `analyze_stock_data` 関数を呼び出します。
- `assert 'SMA_50' in analyzed_data.columns`: 解析結果のDataFrameに 'SMA_50' 列が含まれていることを確認します。
- `assert 'SMA_200' in analyzed_data.columns`: 解析結果のDataFrameに 'SMA_200' 列が含まれていることを確認します。

#### `test_plot_stock_data`

```python
def test_plot_stock_data(stock_data):
    analyzed_data = analyze_stock_data(stock_data)
    output_file = "test_stock_plot.png"
    plot_stock_data(analyzed_data, output_file)
    assert os.path.exists(output_file)
    os.remove(output_file)
```

- `test_plot_stock_data`: `plot_stock_data` 関数をテストします。
- `analyzed_data = analyze_stock_data(stock_data)`: `stock_data` を入力として `analyze_stock_data` 関数を呼び出します。
- `output_file = "test_stock_plot.png"`: 出力ファイルのパスを指定します。
- `plot_stock_data(analyzed_data, output_file)`: `plot_stock_data` 関数を呼び出してグラフを作成し、指定されたファイルに保存します。
- `assert os.path.exists(output_file)`: 指定されたファイルが実際に存在することを確認します。
- `os.remove(output_file)`: テストが終了したら、生成されたファイルを削除してクリーンアップします。

### テストを実行する方法

以下のコマンドでテストを実行します。

```bash
pytest tests
```

これにより、`tests` フォルダ内の全てのテストが実行され、結果が表示されます。

### まとめ

- **フィクスチャの使用**: 共通のテストデータを準備するために `@pytest.fixture` を使います。
- **アサーション**: `assert` 文を使って、関数の出力が期待通りであることを確認します。
- **テスト関数の命名**: テスト関数は `test_` で始まる名前にします。これにより `pytest` が自動的にテスト関数を検出します。

テストコードを書く際には、テスト対象の機能が正しく動作することを確認するための様々なケースを網羅するように心がけましょう。

</details>

<br>

かいつまんで話すと以下を注意して`pytest`のコードを作成するのがいい

- **フィクスチャの使用**: 共通のテストデータを準備するために `@pytest.fixture` を使います。
- **アサーション**: `assert` 文を使って、関数の出力が期待通りであることを確認します。
- **テスト関数の命名**: テスト関数は `test_` で始まる名前にします。これにより `pytest` が自動的にテスト関数を検出します。
