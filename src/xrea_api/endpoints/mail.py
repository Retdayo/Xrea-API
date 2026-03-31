"""メール・メーリングリスト管理 API"""
from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ..base import BaseClient


class MailEndpoint:
    def __init__(self, client: BaseClient) -> None:
        self._c = client

    def list(self, grep: str | None = None) -> Any:
        """メールアカウント一覧を取得する。

        Parameters
        ----------
        grep:
            フィルタリング文字列（省略可）
        """
        data: dict[str, Any] = {}
        if grep is not None:
            data["grep"] = grep
        return self._c.request("/v1/mail/list", data=data)

    def edit(self, mail_address: str, **kwargs: Any) -> Any:
        """メールアカウントを作成・変更する。

        Parameters
        ----------
        mail_address:
            メールアドレス
        **kwargs:
            password、capacity 等の追加パラメータ
        """
        return self._c.request("/v1/mail/edit", data={"mail_address": mail_address, **kwargs})

    def delete(self, mail_address: str) -> Any:
        """メールアカウントを削除する。

        Parameters
        ----------
        mail_address:
            削除するメールアドレス
        """
        return self._c.request("/v1/mail/delete", data={"mail_address": mail_address})


class MailListEndpoint:
    """メーリングリスト管理"""

    def __init__(self, client: BaseClient) -> None:
        self._c = client

    def list(self, grep: str | None = None) -> Any:
        """メーリングリスト一覧を取得する。

        Parameters
        ----------
        grep:
            フィルタリング文字列（省略可）
        """
        data: dict[str, Any] = {}
        if grep is not None:
            data["grep"] = grep
        return self._c.request("/v1/mail_list/list", data=data)

    def edit(self, mail_address: str, **kwargs: Any) -> Any:
        """メーリングリストを作成・変更する。

        Parameters
        ----------
        mail_address:
            メーリングリストのアドレス
        **kwargs:
            追加パラメータ
        """
        return self._c.request("/v1/mail_list/edit", data={"mail_address": mail_address, **kwargs})

    def delete(self, mail_address: str) -> Any:
        """メーリングリストを削除する。

        Parameters
        ----------
        mail_address:
            削除するメーリングリストのアドレス
        """
        return self._c.request("/v1/mail_list/delete", data={"mail_address": mail_address})
