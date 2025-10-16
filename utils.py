import os
from datetime import datetime, timedelta

def format_timestamp(dt=None, fmt="%Y-%m-%d %H:%M:%S"):
    """
    Returns a formatted timestamp string.

    Parameters:
        dt : datetime, optional
            If provided, format this datetime object.
            Defaults to current datetime if None.
        fmt : str
            Python strftime format string.

    Returns:
        str: Formatted timestamp string.
    
    Example:
        >>> format_timestamp()
        '2025-10-16 13:45:23'
    """
    if dt is None:
        dt = datetime.now()
    return dt.strftime(fmt)


def safe_float(value, default=None):
    """
    Safely converts a value to float. Returns default if conversion fails.

    Parameters:
        value : any
            Value to convert to float.
        default : any
            Value to return if conversion fails. Defaults to None.

    Returns:
        float or default

    Example:
        >>> safe_float("12.3")
        12.3
        >>> safe_float("abc", 0)
        0
    """
    try:
        return float(value)
    except (ValueError, TypeError):
        return default


def cleanup_old_files(folder, days=7, extension=".png"):
    """
    Deletes files older than a specified number of days in a folder.

    Parameters:
        folder : str
            Path to the folder to clean up.
        days : int
            Delete files older than this many days. Defaults to 7.
        extension : str
            Only delete files with this extension. Defaults to '.png'.

    Behavior:
        - Scans the folder for matching files.
        - Deletes files older than specified days.
        - Prints deleted files for logging purposes.
    """
    now = datetime.now()
    cutoff = now - timedelta(days=days)

    for filename in os.listdir(folder):
        if filename.endswith(extension):
            filepath = os.path.join(folder, filename)
            file_time = datetime.fromtimestamp(os.path.getmtime(filepath))
            if file_time < cutoff:
                os.remove(filepath)
                print(f"🗑️ Deleted old file: {filepath}")


def dict_to_row(flat_keys, row_dict):
    """
    Converts a dictionary of PLC tag values to a CSV row list following the given header order.

    Parameters:
        flat_keys : list of str
            Ordered list of CSV header keys.
        row_dict : dict
            Dictionary of tag names and their current values.

    Returns:
        list:
            Row values in the same order as flat_keys.

    Example:
        >>> flat_keys = ['Motor_Status_UDT.Running', 'Drive_Parameters_UDT.Speed']
        >>> row_dict = {'Motor_Status_UDT.Running':1, 'Drive_Parameters_UDT.Speed':1200}
        >>> dict_to_row(flat_keys, row_dict)
        [1, 1200]
    """
    return [row_dict.get(k, "") for k in flat_keys]
