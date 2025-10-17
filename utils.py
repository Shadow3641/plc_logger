"""
Helper functions used across modules.
"""

from datetime import datetime

def timestamp_now():
    """Return current timestamp as string."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
