import os
import omni.usd
from urllib.parse import unquote
import omni.timeline

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
    # 初期化はcomputeに任せる
    pass

def compute(db):
    # タイムラインの現在の時間を取得
    current_time = omni.timeline.get_timeline_interface().get_current_time()
    
    # 強制リセットのトリガー
    last_time = getattr(db.state, 'last_time', -1.0)
    
    if not getattr(db.state, 'initialized', False) or current_time < last_time or current_time == 0:
        db.state.idx = 0
        db.state.lines = []
        path = get_path()
        if os.path.exists(path):
            try:
                with open(path, "r") as f:
                    db.state.lines = [l.strip() for l in f.readlines() if l.strip()]
            except:
                pass
        db.state.initialized = True
        db.state.last_time = current_time
        print(f"--- Hard Reset: Playback starts from 0 (Time: {current_time}) ---")

    db.state.last_time = current_time
    lines = getattr(db.state, 'lines', [])
    curr_idx = db.state.idx

    if curr_idx < len(lines):
        try:
            line_data = lines[curr_idx].split(',')
            db.outputs.out_values = [x == "True" for x in line_data]
            db.state.idx = curr_idx + 1
        except:
            db.state.idx = curr_idx + 1
    else:
        db.state.idx = len(lines)
        
    return True