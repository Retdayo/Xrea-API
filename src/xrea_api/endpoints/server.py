"""サーバー情報 API"""
from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ..base import BaseClient


class ServerEndpoint:
    def __init__(self, client: BaseClient) -> None:
        self._c = client

    def use_info(self) -> Any:
        """ディスク・ファイル使用量を取得する。"""
        return self._c.request("/v1/server/use_info")

    def stat(self) -> Any:
        """サーバーパフォーマンス統計を取得する。"""
        return self._c.request("/v1/server/stat")

    def spec(self) -> Any:
        """サーバーハードウェア仕様を取得する。"""
        return self._c.request("/v1/server/spec")

    def du_mail(self) -> Any:
        """メールストレージの内訳を取得する。"""
        return self._c.request("/v1/server/du_mail")

    def du_file(self) -> Any:
        """ファイルストレージの内訳を取得する。"""
        return self._c.request("/v1/server/du_file")
