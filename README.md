# IsaacSimRecordLoadNode
IsaacSimのScriptNodeで使用できるファイル読み込み、出力ノードです。

# 実行方法
後述の使用するスクリプト毎にAttributeを指定する。
IsaacSimのScriptNode内にコピペするか、ダウンロードしたスクリプトのパスをScriptNodeのscript Pathで指定し、各イベントノードから接続する。

## RecordScript.py
ScriptNodeに以下のAttributeを追加する。
|-I/O-|-型-|-名前-|
|---|---|---|
|Input|任意|values|

## LoadScript.py
ScriptNodeに以下のAttributeを追加する。
|-I/O-|-型-|-名前-|
|---|---|---|
|Output|任意|values|
※型はファイル内に保存されているデータと一致する必要がある
