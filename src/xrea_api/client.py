"""メインクライアントクラス"""
from __future__ import annotations

from .base import BaseClient
from .endpoints import (
    CmsEndpoint,
    CronEndpoint,
    DatabaseEndpoint,
    FtpEndpoint,
    LogEndpoint,
    MailEndpoint,
    MailListEndpoint,
    ServerCopyEndpoint,
    ServerEndpoint,
    SiteEndpoint,
    ToolEndpoint,
    UserEndpoint,
)


class XreaClient:
    """XREA API クライアント。

    Parameters
    ----------
    account:
        登録アカウント名
    server_name:
        サーバー識別子 (例: ``s1001.xrea.com``)
    api_secret_key:
        コントロールパネルで発行した APIシークレットキー
    base_url:
        ベースURL。デフォルトは ``https://api.xrea.com/``。
        Coreserver の場合は ``https://api.coreserver.jp/`` を指定。
    rate_limit_interval:
        リクエスト間の最小待機秒数（デフォルト: 1.0 秒）
    timeout:
        HTTP タイムアウト秒数（デフォルト: 30 秒）

    Examples
    --------
    >>> from xrea_api import XreaClient
    >>> client = XreaClient(
    ...     account="myaccount",
    ...     server_name="s1001.xrea.com",
    ...     api_secret_key="xxxx",
    ... )
    >>> client.site.list()
    >>> client.db.list()
    """

    def __init__(
        self,
        account: str,
        server_name: str,
        api_secret_key: str,
        *,
        base_url: str = BaseClient.XREA_BASE_URL,
        rate_limit_interval: float = 1.0,
        timeout: int = 30,
    ) -> None:
        self._base = BaseClient(
            account=account,
            server_name=server_name,
            api_secret_key=api_secret_key,
            base_url=base_url,
            rate_limit_interval=rate_limit_interval,
            timeout=timeout,
        )

        self.user = UserEndpoint(self._base)
        self.site = SiteEndpoint(self._base)
        self.mail = MailEndpoint(self._base)
        self.mail_list = MailListEndpoint(self._base)
        self.db = DatabaseEndpoint(self._base)
        self.ftp = FtpEndpoint(self._base)
        self.server = ServerEndpoint(self._base)
        self.log = LogEndpoint(self._base)
        self.cron = CronEndpoint(self._base)
        self.server_copy = ServerCopyEndpoint(self._base)
        self.cms = CmsEndpoint(self._base)
        self.tool = ToolEndpoint(self._base)


class CoreserverClient(XreaClient):
    """Coreserver API クライアント。

    :class:`XreaClient` と同じインターフェースを持ち、ベース URL のみ異なる。

    Examples
    --------
    >>> from xrea_api import CoreserverClient
    >>> client = CoreserverClient(
    ...     account="myaccount",
    ...     server_name="s1001.coreserver.jp",
    ...     api_secret_key="xxxx",
    ... )
    """

    def __init__(
        self,
        account: str,
        server_name: str,
        api_secret_key: str,
        **kwargs,
    ) -> None:
        kwargs.setdefault("base_url", BaseClient.CORESERVER_BASE_URL)
        super().__init__(account, server_name, api_secret_key, **kwargs)
