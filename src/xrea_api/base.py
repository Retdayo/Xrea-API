"""ベースHTTPクライアント（認証・レート制限・レスポンス処理）"""
from __future__ import annotations

import time
from typing import Any

import requests

from .exceptions import XreaApiError, XreaAuthError, XreaServerError


class BaseClient:
    """XREA / Coreserver API への低レベルHTTPクライアント。

    Parameters
    ----------
    account:
        登録アカウント名
    server_name:
        サーバー識別子 (例: s1001.xrea.com)
    api_secret_key:
        コントロールパネルで発行した APIシークレットキー
    base_url:
        ベースURL。デフォルトは XREA (``https://api.xrea.com/``)。
        Coreserver の場合は ``https://api.coreserver.jp/`` を指定。
    rate_limit_interval:
        リクエスト間の最小待機秒数（デフォルト: 1.0 秒）
    timeout:
        HTTPタイムアウト秒数（デフォルト: 30 秒）
    """

    XREA_BASE_URL = "https://api.xrea.com/"
    CORESERVER_BASE_URL = "https://api.coreserver.jp/"

    def __init__(
        self,
        account: str,
        server_name: str,
        api_secret_key: str,
        *,
        base_url: str = XREA_BASE_URL,
        rate_limit_interval: float = 1.0,
        timeout: int = 30,
    ) -> None:
        self.account = account
        self.server_name = server_name
        self.api_secret_key = api_secret_key
        self.base_url = base_url.rstrip("/")
        self.rate_limit_interval = rate_limit_interval
        self.timeout = timeout

        self._session = requests.Session()
        self._last_request_time: float = 0.0

    def _wait_for_rate_limit(self) -> None:
        elapsed = time.monotonic() - self._last_request_time
        wait = self.rate_limit_interval - elapsed
        if wait > 0:
            time.sleep(wait)

    def _auth_params(self) -> dict[str, str]:
        return {
            "account": self.account,
            "server_name": self.server_name,
            "api_secret_key": self.api_secret_key,
        }

    def request(
        self,
        path: str,
        data: dict[str, Any] | None = None,
    ) -> Any:
        """指定パスへ POST リクエストを送信し、result を返す。

        Parameters
        ----------
        path:
            ``/v1/site/list`` のような APIパス
        data:
            追加POSTパラメータ（認証情報は自動付与）

        Returns
        -------
        Any
            レスポンスの ``result`` フィールド
        """
        self._wait_for_rate_limit()

        url = f"{self.base_url}{path}"
        payload = {**self._auth_params(), **(data or {})}

        try:
            resp = self._session.post(url, data=payload, timeout=self.timeout)
            resp.raise_for_status()
        except requests.exceptions.HTTPError as exc:
            raise XreaApiError(str(exc)) from exc
        except requests.exceptions.RequestException as exc:
            raise XreaApiError(str(exc)) from exc
        finally:
            self._last_request_time = time.monotonic()

        try:
            body = resp.json()
        except ValueError as exc:
            raise XreaApiError(f"JSON decode error: {resp.text}") from exc

        status_code = body.get("status_code", 200)
        message = body.get("message", "")

        if status_code == 500:
            if "auth" in message.lower() or "secret" in message.lower():
                raise XreaAuthError(message, status_code=status_code)
            raise XreaServerError(message, status_code=status_code)

        return body.get("result")
