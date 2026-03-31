"""各種ツール API"""
from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ..base import BaseClient


class ToolEndpoint:
    def __init__(self, client: BaseClient) -> None:
        self._c = client

    def wplogin_deny_list(self, domain: str) -> Any:
        """WordPress ログインのジオブロッキング設定を取得する。

        Parameters
        ----------
        domain:
            対象ドメイン
        """
        return self._c.request("/v1/tool/wplogin_deny_list", data={"domain": domain})

    def wplogin_deny_edit(self, domain: str, **kwargs: Any) -> Any:
        """WordPress ログインのアクセス制限を設定する。

        Parameters
        ----------
        domain:
            対象ドメイン
        **kwargs:
            設定パラメータ（国コード等）
        """
        return self._c.request("/v1/tool/wplogin_deny_edit", data={"domain": domain, **kwargs})

    def ssh_ip_allow(self, ip_address: str) -> Any:
        """SSH 許可 IP アドレスを登録する。

        Parameters
        ----------
        ip_address:
            許可する IP アドレス
        """
        return self._c.request("/v1/tool/ssh_ip_allow", data={"ip_address": ip_address})

    def htpasswd_create(self, username: str, password: str) -> Any:
        """htpasswd 用の認証文字列を生成する。

        Parameters
        ----------
        username:
            ユーザー名
        password:
            パスワード
        """
        return self._c.request(
            "/v1/tool/htpasswd_create",
            data={"username": username, "password": password},
        )

    def chown_reset(self, path: str | None = None) -> Any:
        """ファイルオーナーシップをリセットする。

        Parameters
        ----------
        path:
            対象パス（省略時は全体）
        """
        data: dict[str, Any] = {}
        if path is not None:
            data["path"] = path
        return self._c.request("/v1/tool/chown_reset", data=data)
