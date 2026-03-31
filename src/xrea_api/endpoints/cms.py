"""CMS インストール API"""
from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ..base import BaseClient


class CmsEndpoint:
    def __init__(self, client: BaseClient) -> None:
        self._c = client

    def wp_install(self, domain: str, **kwargs: Any) -> Any:
        """WordPress をインストールする。

        Parameters
        ----------
        domain:
            インストール先ドメイン
        **kwargs:
            dir、db_name、admin_user、admin_pass 等
        """
        return self._c.request("/v1/cms/wp_install", data={"domain": domain, **kwargs})

    def xoops_install(self, domain: str, **kwargs: Any) -> Any:
        """XOOPS をインストールする。

        Parameters
        ----------
        domain:
            インストール先ドメイン
        **kwargs:
            追加パラメータ
        """
        return self._c.request("/v1/cms/xoops_install", data={"domain": domain, **kwargs})

    def mt_install(self, domain: str, **kwargs: Any) -> Any:
        """MovableType をインストールする。

        Parameters
        ----------
        domain:
            インストール先ドメイン
        **kwargs:
            追加パラメータ
        """
        return self._c.request("/v1/cms/mt_install", data={"domain": domain, **kwargs})

    def phpmyadmin_install(self, domain: str, **kwargs: Any) -> Any:
        """phpMyAdmin をインストールする。

        Parameters
        ----------
        domain:
            インストール先ドメイン
        **kwargs:
            追加パラメータ
        """
        return self._c.request("/v1/cms/phpmyadmin_install", data={"domain": domain, **kwargs})

    def phppgadmin_install(self, domain: str, **kwargs: Any) -> Any:
        """phpPgAdmin をインストールする。

        Parameters
        ----------
        domain:
            インストール先ドメイン
        **kwargs:
            追加パラメータ
        """
        return self._c.request("/v1/cms/phppgadmin_install", data={"domain": domain, **kwargs})

    def phpadmin_check(self, domain: str) -> Any:
        """管理ツールのインストール状態を確認する。

        Parameters
        ----------
        domain:
            確認するドメイン
        """
        return self._c.request("/v1/cms/phpadmin_check", data={"domain": domain})
