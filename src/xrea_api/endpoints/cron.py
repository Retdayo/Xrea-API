"""Cron ジョブ管理 API"""
from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ..base import BaseClient


class CronEndpoint:
    def __init__(self, client: BaseClient) -> None:
        self._c = client

    def list(self) -> Any:
        """Cron ジョブ一覧を取得する。"""
        return self._c.request("/v1/cron/list")

    def edit(
        self,
        cron_id: str | None = None,
        *,
        minute: str = "*",
        hour: str = "*",
        day: str = "*",
        month: str = "*",
        weekday: str = "*",
        command: str,
        **kwargs: Any,
    ) -> Any:
        """Cron ジョブを作成・更新する。

        Parameters
        ----------
        cron_id:
            更新する場合は既存の Cron ID（新規作成時は省略）
        minute:
            分フィールド（デフォルト: ``"*"``）
        hour:
            時フィールド（デフォルト: ``"*"``）
        day:
            日フィールド（デフォルト: ``"*"``）
        month:
            月フィールド（デフォルト: ``"*"``）
        weekday:
            曜日フィールド（デフォルト: ``"*"``）
        command:
            実行するコマンド
        **kwargs:
            その他のパラメータ
        """
        data: dict[str, Any] = {
            "minute": minute,
            "hour": hour,
            "day": day,
            "month": month,
            "weekday": weekday,
            "command": command,
            **kwargs,
        }
        if cron_id is not None:
            data["cron_id"] = cron_id
        return self._c.request("/v1/cron/edit", data=data)

    def delete(self, cron_id: str) -> Any:
        """Cron ジョブを削除する。

        Parameters
        ----------
        cron_id:
            削除する Cron ID
        """
        return self._c.request("/v1/cron/delete", data={"cron_id": cron_id})
