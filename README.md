# OCI Generative AI SDK (Python)の使い方 


VMからGenerative AIのPythonサンプルコードを呼び出す手順です

## 前提条件
* Chicagoリージョンをサブスクライブしていること
* VCNがあること

## ポリシー設定
Generative AIサービスの利用ポリシーを設定します。
下記はany-userですが、必要なユーザグループに対して権限を付与します。
```sh
Allow any-user to use generative-ai-family in compartment (compartment_name)
```
## VM作成
Oracle Linux8, パブリックサブネットにて作成する。
SSHキーは既存の公開キーがあればそちらを設定。


## pip, oci python sdkインストール
pipがインストールされていない場合は下記を実行します。
（例）Python3.6の場合
```sh
curl https://bootstrap.pypa.io/pip/3.6/get-pip.py -o get-pip.py
python get-pip.py
```
なお、pip最新版は下記はこちらです（ https://bootstrap.pypa.io/get-pip.py ）

```sh
pip install oci
```

## 動作確認
git clone等でchattest_demo.pyをVMにコピーし、ソースの下記部分にgenerative ai実行権限のあるcompartment_idを記述します。
```python
compartment_id = "(my_compartment_id)"
```
デモソースを実行します
```sh
python chattest_demo.py
```




