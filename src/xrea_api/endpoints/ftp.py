"""FTP アカウント管理 API"""
from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ..base import BaseClient


class FtpEndpoint:
    def __init__(self, client: BaseClient) -> None:
        self._c = client

    def info(self) -> Any:
        """メイン FTP アカウント情報を取得する。"""
        return self._c.request("/v1/ftp/info")

    def account_list(self, grep: str | None = None) -> Any:
        """サブ FTP アカウント一覧を取得する。

        Parameters
        ----------
        grep:
            フィルタリング文字列（省略可）
        """
        data: dict[str, Any] = {}
        if grep is not None:
            data["grep"] = grep
        return self._c.request("/v1/ftp/account_list", data=data)

    def account_edit(self, ftp_account: str, **kwargs: Any) -> Any:
        """サブ FTP アカウントを作成・変更する。

        Parameters
        ----------
        ftp_account:
            FTP アカウント名
        **kwargs:
            password、dir 等の追加パラメータ
        """
        return self._c.request(
            "/v1/ftp/account_edit",
            data={"ftp_account": ftp_account, **kwargs},
        )

    def account_delete(self, ftp_account: str) -> Any:
        """サブ FTP アカウントを削除する。

        Parameters
        ----------
        ftp_account:
            削除する FTP アカウント名
        """
        return self._c.request("/v1/ftp/account_delete", data={"ftp_account": ftp_account})
