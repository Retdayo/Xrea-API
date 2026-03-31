"""ログ管理 API"""
from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ..base import BaseClient


class LogEndpoint:
    def __init__(self, client: BaseClient) -> None:
        self._c = client

    def settings(self) -> Any:
        """ログ保持設定を確認する。"""
        return self._c.request("/v1/log/settings")

    def settings_edit(self, **kwargs: Any) -> Any:
        """ログ保持設定を変更する。

        Parameters
        ----------
        **kwargs:
            変更するパラメータ
        """
        return self._c.request("/v1/log/settings_edit", data=kwargs)

    def log_list(self, domain: str | None = None) -> Any:
        """利用可能なログ一覧を取得する。

        Parameters
        ----------
        domain:
            対象ドメイン（省略可）
        """
        data: dict[str, Any] = {}
        if domain is not None:
            data["domain"] = domain
        return self._c.request("/v1/log/log_list", data=data)

    def log_output(self, log_file: str) -> Any:
        """ログファイルの内容を取得する。

        Parameters
        ----------
        log_file:
            取得するログファイル名
        """
        return self._c.request("/v1/log/log_output", data={"log_file": log_file})

    def rawlog_save(self) -> Any:
        """現在のログをアーカイブする。"""
        return self._c.request("/v1/log/rawlog_save")
