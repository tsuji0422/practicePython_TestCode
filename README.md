# Project Overview

## プロジェクトの主目的

主目的はGitHubで使える機能の確認だ。
このプロジェクトでは次について確認する。

- **基本的なテストコードの実行方法について(pytest)**
- テストコードの自動化について
  - GitHub Actions の設定について
  - プルリクエストによる自動実行方法について
- テスト環境の構築
  - poetryの導入
  - Dockerの導入
- CI/CDの利用による定期実行とサーバ内での自動化
  - GitHub Actions のワークフローにDockerのステップ追加

今回は「基本的なテストコードの実行方法について(pytest)」について確認を行う。

## プロジェクトの題材

上記を確認するために、今回は株価解析を行う。

![image](/docs/images/README/projectOverview.drawio.svg)

やることとしては

-  Yahoo Financeから株価データを取得する
-  pandasを用いてデータ解析をする
-  matplotlibなどでグラフを作成しフォルダに保存する

## 詳細

- [GetStarted!](/docs/getStarted.md)
