# xrea-api

Python wrapper for the [XREA / Coreserver API](https://apidoc.xrea.com/).

## Installation

```bash
pip install xrea-api
```

## Quick Start

```python
from xrea_api import XreaClient

client = XreaClient(
    account="your_account",
    server_name="s1001.xrea.com",
    api_secret_key="your_secret_key",
)

# サイト一覧の取得
sites = client.site.list()

# メールアカウント一覧
mails = client.mail.list()

# データベース一覧
dbs = client.db.list()
```

## Supported Endpoints

| カテゴリ | 説明 |
|---------|------|
| `client.user` | アカウント管理 |
| `client.site` | サイト・ドメイン管理 |
| `client.mail` | メールアカウント管理 |
| `client.mail_list` | メーリングリスト管理 |
| `client.db` | データベース管理 |
| `client.ftp` | FTPアカウント管理 |
| `client.server` | サーバー情報 |
| `client.log` | ログ管理 |
| `client.cron` | Cronジョブ管理 |
| `client.server_copy` | サーバーコピー管理 |
| `client.cms` | CMSインストール |
| `client.tool` | 各種ツール |

## Rate Limiting

XREA APIは1秒間に1リクエストの制限があります。本ライブラリは自動的にレート制限を適用します。

## Authentication

APIキーはXREAコントロールパネルから発行してください。

## License

MIT
