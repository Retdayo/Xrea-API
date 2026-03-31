"""サイト管理 API"""
from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ..base import BaseClient


class SiteEndpoint:
    def __init__(self, client: BaseClient) -> None:
        self._c = client

    def list(self, grep: str | None = None) -> Any:
        """ドメイン一覧を取得する。

        Parameters
        ----------
        grep:
            フィルタリング文字列（省略可）
        """
        data: dict[str, Any] = {}
        if grep is not None:
            data["grep"] = grep
        return self._c.request("/v1/site/list", data=data)

    def edit(
        self,
        domain: str,
        *,
        php_version: str | None = None,
        ssl: str | None = None,
        **kwargs: Any,
    ) -> Any:
        """サイト設定を作成・変更する。

        Parameters
        ----------
        domain:
            対象ドメイン名
        php_version:
            PHP バージョン（省略可）
        ssl:
            SSL 設定（省略可）
        **kwargs:
            その他のパラメータ
        """
        data: dict[str, Any] = {"domain": domain, **kwargs}
        if php_version is not None:
            data["php_version"] = php_version
        if ssl is not None:
            data["ssl"] = ssl
        return self._c.request("/v1/site/edit", data=data)

    def delete(self, domain: str) -> Any:
        """ドメインを削除する (no:1 は削除不可)。

        Parameters
        ----------
        domain:
            削除するドメイン名
        """
        return self._c.request("/v1/site/delete", data={"domain": domain})
