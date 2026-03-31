from .cms import CmsEndpoint
from .cron import CronEndpoint
from .database import DatabaseEndpoint
from .ftp import FtpEndpoint
from .log import LogEndpoint
from .mail import MailEndpoint, MailListEndpoint
from .server import ServerEndpoint
from .server_copy import ServerCopyEndpoint
from .site import SiteEndpoint
from .tool import ToolEndpoint
from .user import UserEndpoint

__all__ = [
    "CmsEndpoint",
    "CronEndpoint",
    "DatabaseEndpoint",
    "FtpEndpoint",
    "LogEndpoint",
    "MailEndpoint",
    "MailListEndpoint",
    "ServerEndpoint",
    "ServerCopyEndpoint",
    "SiteEndpoint",
    "ToolEndpoint",
    "UserEndpoint",
]
