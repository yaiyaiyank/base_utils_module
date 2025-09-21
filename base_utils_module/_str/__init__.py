import re


def remove_invalid_path_chars(string: str) -> str:
    """ファイル名として使用できない文字を削除する"""
    # Windowsでファイル名として使用できない文字を定義
    invalid_chars = r'[<>:"/\\|?*]'
    # 無効な文字を除去
    return re.sub(invalid_chars, "", string)


def join_comma(str_list: list[str]) -> str:
    """
    ['id INTEGER PRIMARY KEY AUTOINCREMENT', 'name TEXT']
    ->
    'id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT'
    """

    joined_str = ", ".join(str_list)
    return joined_str


def join_ander(str_list: list[str]) -> str:
    """
    ['read', 'text']
    ->
    'read_text'
    """

    joined_str = "_".join(str_list)
    return joined_str
