# Introduction to Deep Learning

会社の同期勉強会用の資料  
Neural NetworkとDeep Learningそれぞれで手書き文字認識を行って，両者の違いを確認する

## 実験

以下のJupyter Notebookを使って実験を行うことが出来る

- neural_network.ipynb
- deep_learning.ipynb

## 文字認識アプリケーション

文字認識をFlaskアプリケーションとして動かす  
それぞれ以下のディレクトリにアプリケーションが格納されているが，動かすためには事前に実験で作成したモデルが保存されている必要がある

- app_neural_network
- app_deep_learning

元アプリはこちら：  
[ginrou/handwritten_classifier](https://github.com/ginrou/handwritten_classifier)

実行方法は以下の通り


```
$ python app.py
```

## 実験環境構築

動作確認：Python 2.7.9

1. このレポジトリを任意の場所にcloneして以下のコマンドを実行 ※要：virtualenv環境

```
$ pip install -r requirements.txt
```

2. 以下のサイトから `mnist.pkl.gz` データをダウンロードして， `data` ディレクトリ以下に保存
http://deeplearning.net/tutorial/gettingstarted.html

3. 以下のコマンドを実行

```
$ python pre_processing.py
```
