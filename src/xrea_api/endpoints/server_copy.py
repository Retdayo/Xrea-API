"""サーバーコピー (転送) 管理 API"""
from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ..base import BaseClient


class ServerCopyEndpoint:
    def __init__(self, client: BaseClient) -> None:
        self._c = client

    def list(self) -> Any:
        """転送設定一覧を取得する。"""
        return self._c.request("/v1/server_copy/list")

    def edit(self, **kwargs: Any) -> Any:
        """ファイル同期設定を作成・変更する。

        Parameters
        ----------
        **kwargs:
            設定パラメータ
        """
        return self._c.request("/v1/server_copy/edit", data=kwargs)

    def process(self, copy_id: str) -> Any:
        """単一転送を実行する。

        Parameters
        ----------
        copy_id:
            実行する転送設定 ID
        """
        return self._c.request("/v1/server_copy/process", data={"copy_id": copy_id})

    def stop(self) -> Any:
        """全ての転送をキャンセルする。"""
        return self._c.request("/v1/server_copy/stop")

    def delete(self, copy_id: str) -> Any:
        """転送プロファイルを削除する。

        Parameters
        ----------
        copy_id:
            削除する転送設定 ID
        """
        return self._c.request("/v1/server_copy/delete", data={"copy_id": copy_id})
