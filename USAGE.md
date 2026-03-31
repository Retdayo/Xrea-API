# xrea-api 使い方一覧

## セットアップ

```python
from xrea_api import XreaClient, CoreserverClient

# XREA
client = XreaClient(
    account="myaccount",
    server_name="s1001.xrea.com",
    api_secret_key="your_secret_key",
)

# Coreserver
client = CoreserverClient(
    account="myaccount",
    server_name="s1001.coreserver.jp",
    api_secret_key="your_secret_key",
)

# オプション
client = XreaClient(
    account="myaccount",
    server_name="s1001.xrea.com",
    api_secret_key="your_secret_key",
    rate_limit_interval=1.0,  # リクエスト間隔（秒）デフォルト: 1.0
    timeout=30,               # HTTPタイムアウト（秒）デフォルト: 30
)
```

---

## エラーハンドリング

```python
from xrea_api import XreaApiError, XreaAuthError, XreaServerError

try:
    result = client.site.list()
except XreaAuthError as e:
    print(f"認証エラー: {e}")
except XreaServerError as e:
    print(f"サーバーエラー: {e}")
except XreaApiError as e:
    print(f"APIエラー: {e}")
```

| 例外クラス | 説明 |
|-----------|------|
| `XreaApiError` | 全例外の基底クラス |
| `XreaAuthError` | 認証失敗 |
| `XreaServerError` | APIが status_code=500 を返した |
| `XreaRateLimitError` | レート制限超過 |
| `XreaNotFoundError` | リソースが見つからない |

---

## client.user — ユーザー管理

```python
# アカウント情報を取得
result = client.user.info()

# アカウント設定を変更
result = client.user.info_edit(name="新しい名前")

# パスワードをリセット
result = client.user.pass_reset(new_password="NewPass123!")

# パスワードリマインダーを送信
result = client.user.pass_remind()

# パスワードを検証
result = client.user.pass_check(password="CurrentPass123!")
```

---

## client.site — サイト・ドメイン管理

```python
# 全サイト一覧を取得
result = client.site.list()

# ドメイン名でフィルタリング
result = client.site.list(grep="example.com")

# サイト設定を作成・変更
result = client.site.edit("example.com")
result = client.site.edit("example.com", php_version="8.2", ssl="on")

# ドメインを削除（no:1 は削除不可）
result = client.site.delete("example.com")
```

---

## client.mail — メールアカウント管理

```python
# メールアカウント一覧を取得
result = client.mail.list()

# フィルタリング
result = client.mail.list(grep="info@")

# メールアカウントを作成・変更
result = client.mail.edit("info@example.com", password="MailPass123!")

# メールアカウントを削除
result = client.mail.delete("info@example.com")
```

---

## client.mail_list — メーリングリスト管理

```python
# メーリングリスト一覧を取得
result = client.mail_list.list()

# フィルタリング
result = client.mail_list.list(grep="members@")

# メーリングリストを作成・変更
result = client.mail_list.edit("members@example.com")

# メーリングリストを削除
result = client.mail_list.delete("members@example.com")
```

---

## client.db — データベース管理

```python
# データベース一覧を取得
result = client.db.list()

# フィルタリング
result = client.db.list(grep="wp_")

# MySQLデータベースを作成
result = client.db.add("mydb", db_type="mysql", password="DbPass123!")

# PostgreSQLデータベースを作成
result = client.db.add("mydb_pg", db_type="postgresql", password="DbPass123!")

# データベース設定を変更
result = client.db.edit("mydb", password="NewPass123!")

# データベースを削除
result = client.db.delete("mydb")

# データベースをエクスポート（ダンプ）
result = client.db.dump("mydb")

# ダンプ一覧を取得
result = client.db.dump_list("mydb")

# ダンプからリストア
result = client.db.restore("mydb", dump_file="mydb_20240101.sql.gz")

# 全データベースをエクスポート
result = client.db.dump_all()
```

---

## client.ftp — FTP アカウント管理

```python
# メインFTPアカウント情報を取得
result = client.ftp.info()

# サブFTPアカウント一覧を取得
result = client.ftp.account_list()

# フィルタリング
result = client.ftp.account_list(grep="sub_")

# サブFTPアカウントを作成・変更
result = client.ftp.account_edit("subuser", password="FtpPass123!", dir="/public_html")

# サブFTPアカウントを削除
result = client.ftp.account_delete("subuser")
```

---

## client.server — サーバー情報

```python
# ディスク・ファイル使用量を取得
result = client.server.use_info()

# サーバーパフォーマンス統計を取得
result = client.server.stat()

# サーバーハードウェア仕様を取得
result = client.server.spec()

# メールストレージの内訳を取得
result = client.server.du_mail()

# ファイルストレージの内訳を取得
result = client.server.du_file()
```

---

## client.log — ログ管理

```python
# ログ保持設定を確認
result = client.log.settings()

# ログ保持設定を変更
result = client.log.settings_edit(keep_days=30)

# ログファイル一覧を取得
result = client.log.log_list()

# ドメイン指定でログ一覧を取得
result = client.log.log_list(domain="example.com")

# ログファイルの内容を取得
result = client.log.log_output(log_file="access_log_20240101.gz")

# 現在のログをアーカイブ
result = client.log.rawlog_save()
```

---

## client.cron — Cron ジョブ管理

```python
# Cronジョブ一覧を取得
result = client.cron.list()

# Cronジョブを新規作成（毎日3時に実行）
result = client.cron.edit(
    command="/usr/bin/php /home/myaccount/public_html/script.php",
    minute="0",
    hour="3",
)

# 毎時0分に実行
result = client.cron.edit(
    command="/usr/bin/python3 /home/myaccount/script.py",
    minute="0",
)

# 既存のCronジョブを更新
result = client.cron.edit(
    cron_id="12345",
    command="/usr/bin/php /home/myaccount/new_script.php",
    minute="30",
    hour="6",
)

# Cronジョブを削除
result = client.cron.delete(cron_id="12345")
```

**cron フィールドのデフォルト値は全て `"*"`（毎）です。**

---

## client.server_copy — サーバーコピー管理

```python
# 転送設定一覧を取得
result = client.server_copy.list()

# 転送設定を作成・変更
result = client.server_copy.edit(
    src_dir="/home/myaccount/public_html",
    dst_dir="/home/backup/public_html",
)

# 転送を今すぐ実行
result = client.server_copy.process(copy_id="1")

# 全ての転送をキャンセル
result = client.server_copy.stop()

# 転送設定を削除
result = client.server_copy.delete(copy_id="1")
```

---

## client.cms — CMS インストール

```python
# WordPress をインストール
result = client.cms.wp_install(
    domain="example.com",
    dir="/wp",
    db_name="mydb",
    admin_user="admin",
    admin_pass="WpPass123!",
)

# XOOPS をインストール
result = client.cms.xoops_install(domain="example.com", dir="/xoops")

# MovableType をインストール
result = client.cms.mt_install(domain="example.com", dir="/mt")

# phpMyAdmin をインストール
result = client.cms.phpmyadmin_install(domain="example.com")

# phpPgAdmin をインストール
result = client.cms.phppgadmin_install(domain="example.com")

# 管理ツールのインストール状態を確認
result = client.cms.phpadmin_check(domain="example.com")
```

---

## client.tool — 各種ツール

```python
# WordPressログインのジオブロッキング設定を確認
result = client.tool.wplogin_deny_list(domain="example.com")

# WordPressログインのアクセス制限を設定
result = client.tool.wplogin_deny_edit(domain="example.com", country="CN,RU")

# SSH許可IPアドレスを登録
result = client.tool.ssh_ip_allow(ip_address="203.0.113.1")

# htpasswd用の認証文字列を生成
result = client.tool.htpasswd_create(username="admin", password="HtPass123!")

# ファイルオーナーシップをリセット
result = client.tool.chown_reset()

# 特定パスのオーナーシップをリセット
result = client.tool.chown_reset(path="/home/myaccount/public_html")
```

---

## レスポンスの形式

全メソッドは API の `result` フィールドをそのまま返します。

```python
result = client.site.list()
# → list / dict / None (APIのresultフィールドの内容による)
```

エラー時は例外が発生します（`result` は返りません）。
