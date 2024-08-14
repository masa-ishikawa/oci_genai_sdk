# OCI Generative AI SDK (Python)の使い方 


VMからGenerative AIのPythonサンプルコードを呼び出す手順です

## 前提条件
* VM,VCNがあること
* Chicagoリージョンをサブスクライブしていること
* Pythonがインストールされていること（3.6以上）



## 1. ポリシー設定
Generative AIサービスの利用ポリシーを設定します。
下記はany-userですが、必要なユーザグループに対して権限を付与します。
```sh
Allow any-user to use generative-ai-family in compartment (compartment_name)
```

## pip, oci python sdkインストール
pipがインストールされていない場合は下記を実行します。
（例）Python3.6の場合
```sh
curl https://bootstrap.pypa.io/pip/3.6/get-pip.py -o get-pip.py
python get-pip.py
```
なお、pip最新版は下記はこちらです（https://bootstrap.pypa.io/get-pip.py）

```sh
pip install oci
```

## デモ
git clone等でchattest_demo.pyをVMにコピーし、ソースの下記部分にgenerative ai実行権限のあるcompartment_idを記述します。
```python
compartment_id = "(my_compartment_id)"
```
デモを実行します
```sh
python chattest_demo.py
```




