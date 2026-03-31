"""ユーザー管理 API"""
from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ..base import BaseClient


class UserEndpoint:
    def __init__(self, client: BaseClient) -> None:
        self._c = client

    def info(self) -> Any:
        """アカウント情報を取得する。"""
        return self._c.request("/v1/user/info")

    def info_edit(self, **kwargs: Any) -> Any:
        """アカウント設定を変更する。

        Parameters
        ----------
        **kwargs:
            変更するフィールドをキーワード引数で渡す。
        """
        return self._c.request("/v1/user/info_edit", data=kwargs)

    def pass_reset(self, new_password: str) -> Any:
        """パスワードをリセットする。

        Parameters
        ----------
        new_password:
            新しいパスワード
        """
        return self._c.request("/v1/user/pass_reset", data={"new_password": new_password})

    def pass_remind(self) -> Any:
        """パスワードリマインダーを送信する。"""
        return self._c.request("/v1/user/pass_remind")

    def pass_check(self, password: str) -> Any:
        """パスワードを検証する。

        Parameters
        ----------
        password:
            確認するパスワード
        """
        return self._c.request("/v1/user/pass_check", data={"password": password})
