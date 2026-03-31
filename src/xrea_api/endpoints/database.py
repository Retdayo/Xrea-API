"""データベース管理 API"""
from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

if TYPE_CHECKING:
    from ..base import BaseClient

DbType = Literal["mysql", "postgresql"]


class DatabaseEndpoint:
    def __init__(self, client: BaseClient) -> None:
        self._c = client

    def list(self, grep: str | None = None) -> Any:
        """データベース一覧を取得する。

        Parameters
        ----------
        grep:
            フィルタリング文字列（省略可）
        """
        data: dict[str, Any] = {}
        if grep is not None:
            data["grep"] = grep
        return self._c.request("/v1/db/list", data=data)

    def add(self, db_name: str, db_type: DbType = "mysql", **kwargs: Any) -> Any:
        """データベースを作成する。

        Parameters
        ----------
        db_name:
            データベース名
        db_type:
            ``"mysql"`` または ``"postgresql"``
        **kwargs:
            password 等の追加パラメータ
        """
        return self._c.request(
            "/v1/db/add",
            data={"db_name": db_name, "db_type": db_type, **kwargs},
        )

    def edit(self, db_name: str, **kwargs: Any) -> Any:
        """データベース設定を変更する。

        Parameters
        ----------
        db_name:
            対象データベース名
        **kwargs:
            変更するパラメータ
        """
        return self._c.request("/v1/db/edit", data={"db_name": db_name, **kwargs})

    def delete(self, db_name: str) -> Any:
        """データベースを削除する。

        Parameters
        ----------
        db_name:
            削除するデータベース名
        """
        return self._c.request("/v1/db/delete", data={"db_name": db_name})

    def dump(self, db_name: str) -> Any:
        """データベースをエクスポートする。

        Parameters
        ----------
        db_name:
            対象データベース名
        """
        return self._c.request("/v1/db/dump", data={"db_name": db_name})

    def restore(self, db_name: str, dump_file: str) -> Any:
        """バックアップからデータベースをリストアする。

        Parameters
        ----------
        db_name:
            リストア対象のデータベース名
        dump_file:
            使用するダンプファイル名
        """
        return self._c.request(
            "/v1/db/restore",
            data={"db_name": db_name, "dump_file": dump_file},
        )

    def dump_list(self, db_name: str) -> Any:
        """利用可能なダンプ一覧を取得する。

        Parameters
        ----------
        db_name:
            対象データベース名
        """
        return self._c.request("/v1/db/dump_list", data={"db_name": db_name})

    def dump_all(self) -> Any:
        """全データベースをエクスポートする。"""
        return self._c.request("/v1/db/dump_all")
