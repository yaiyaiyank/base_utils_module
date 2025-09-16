import re


def remove_invalid_path_chars(string: str) -> str:
    """ファイル名として使用できない文字を削除する"""
    # Windowsでファイル名として使用できない文字を定義
    invalid_chars = r'[<>:"/\\|?*]'
    # 無効な文字を除去
    return re.sub(invalid_chars, "", string)
