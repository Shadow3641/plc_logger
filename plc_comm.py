from pylogix import PLC  # Import the Pylogix library to communicate with Allen-Bradley PLCs


def read_tag(plc, tag):
    """
    Reads a single tag from the PLC.

    Parameters:
        plc : pylogix.PLC instance
            The active PLC connection object used to read tags.
        tag : str
            The name of the tag to read from the PLC.

    Returns:
        tuple:
            status (str): 'Success' if the read was successful, or an error description.
            value: The value of the tag read from the PLC, or None if an error occurred.

    Notes:
        - Handles exceptions gracefully so the main program won't crash if the PLC read fails.
        - Can be used for standard tags or top-level UDTs.
    """
    try:
        # Attempt to read the tag using the pylogix PLC object
        result = plc.Read(tag)

        # Return the status string and the actual value
        return result.Status, result.Value

    except Exception as e:
        # If any exception occurs during communication, return an error string and None
        return f"Error: {e}", None


def flatten_udt(tag_name, value, parent_key=''):
    """
    Recursively flattens a UDT (User-Defined Type) from the PLC into simple key-value pairs.

    Parameters:
        tag_name : str
            The base name of the PLC tag (e.g., 'Motor_Status_UDT').
        value : dict or primitive
            The value returned from the PLC. Can be a nested dictionary (UDT) or a single value.
        parent_key : str
            Used internally during recursion to build the full flattened key name.

    Returns:
        dict:
            A dictionary with flattened keys. Nested UDT members become keys like:
            'Motor_Status_UDT.Running', 'Drive_Parameters_UDT.Speed', etc.

    Example:
        Input:
            tag_name = "Motor_Status_UDT"
            value = {"Running": 1, "Fault": 0}
        Output:
            {"Motor_Status_UDT.Running": 1, "Motor_Status_UDT.Fault": 0}

    Notes:
        - Supports multiple levels of nesting (UDTs within UDTs).
        - Useful for logging all individual PLC parameters to CSV or monitoring systems.
    """
    flat = {}

    if isinstance(value, dict):
        # If the value is a dictionary (nested UDT), iterate through its members
        for k, v in value.items():
            # Build the full key name: either 'parent.child' or 'tag.child' if top-level
            key_name = f"{parent_key}.{k}" if parent_key else f"{tag_name}.{k}"

            # Recursively flatten the next level
            flat.update(flatten_udt(tag_name, v, key_name))

    else:
        # Base case: the value is a primitive (int, float, string, bool, etc.)
        # Assign it to the full key name
        flat[parent_key] = value

    return flat
