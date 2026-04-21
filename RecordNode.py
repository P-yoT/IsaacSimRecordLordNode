import os

def get_path():# USDファイルの場所を基準にvalues.csvのパスを決定する。
    stage = omni.usd.get_context().get_stage()
    usd_url = stage.GetRootLayer().identifier
    clean_path = unquote(usd_url.replace("file:", "")).lstrip("/")
    if ":" in clean_path and clean_path[0] == "/":
        clean_path = clean_path[1:]
    clean_path = os.path.normpath(clean_path)
    root = os.path.dirname(clean_path) if usd_url and "anonymous" not in usd_url else os.path.expanduser("~")  # ルートディレクトリをUSDファイルの場所にするか、匿名の場合はユーザーディレクトリにする
    return os.path.join(root, "tmp", "values.csv") 


def setup(db):
    try:
        # フォルダが無ければ作成
        os.makedirs(os.path.dirname(SAVE_PATH), exist_ok=True)
        # ファイルを新規作成（上書き）
        with open(SAVE_PATH, "w") as f:
            pass
        print(f"Record Setup: {SAVE_PATH}")
    except Exception as e:
        print(f"Setup Error: {e}")

def compute(db):
    try:
        # 入力を取得。ScriptNodeで定義したものと同じ名前でアクセスできる
        values = db.inputs.values
        # 文字列にして追記
        line = ",".join(map(str, values))
        with open(SAVE_PATH, "a") as f:
            f.write(line + "\n")
    except:
        pass
    return True