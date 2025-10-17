"""
Handles PLC communication using pylogix.
Supports reading tags and returning values.
"""

from pylogix import PLC
import config

def read_tags():
    """
    Read all configured tags from PLC.
    Returns a dictionary: {tag_name: value}
    """
    results = {}
    with PLC() as comm:
        comm.IPAddress = config.PLC_IP
        for tag in config.PLC_TAGS:
            # Read tag from PLC
            response = comm.Read(tag)
            if response.Status == "Success":
                results[tag] = response.Value
            else:
                results[tag] = None  # Could not read
    return results
