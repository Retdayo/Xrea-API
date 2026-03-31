"""xrea-api — XREA / Coreserver API Python ラッパー"""
from .client import CoreserverClient, XreaClient
from .exceptions import (
    XreaApiError,
    XreaAuthError,
    XreaNotFoundError,
    XreaRateLimitError,
    XreaServerError,
)

__version__ = "0.1.0"

__all__ = [
    "XreaClient",
    "CoreserverClient",
    "XreaApiError",
    "XreaAuthError",
    "XreaNotFoundError",
    "XreaRateLimitError",
    "XreaServerError",
]
