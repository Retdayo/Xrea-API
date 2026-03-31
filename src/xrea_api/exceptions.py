class XreaApiError(Exception):
    """XREA API の基底例外クラス"""

    def __init__(self, message: str, status_code: int | None = None):
        super().__init__(message)
        self.status_code = status_code


class XreaAuthError(XreaApiError):
    """認証エラー"""


class XreaRateLimitError(XreaApiError):
    """レート制限エラー"""


class XreaNotFoundError(XreaApiError):
    """リソースが見つからない"""


class XreaServerError(XreaApiError):
    """サーバー側エラー (status_code=500)"""
