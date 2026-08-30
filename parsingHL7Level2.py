import json
from typing import Any, Dict


def get_field(fields: list, index: int, default: str = "") -> str:
    """
    Safely retrieve a field from an HL7 segment list by index.
    Prevents IndexError on short or truncated segments.
    """
    if 0 <= index < len(fields):
        return fields[index]
    return default


def parse_hl7_level2(raw_str_sample: str) -> Dict[str, Any]:
    """
    Level 2 HL7 Parser: Converts raw HL7 v2 messages into a dictionary
    with nested observation objects.
    """
    results = {}
    results["observations"] = []

    # Universal line normalization handling \r\n, \n, and \r line endings
    sample_1 = raw_str_sample.replace("\r\n", "\r").replace("\n", "\r").split("\r")

    for item in sample_1:
        fields = item.split("|")

        if fields[0] == "MSH":
            results["message_type"] = get_field(fields, 8, "")
            results["message_control_id"] = get_field(fields, 9, "")

        elif fields[0] == "PID":
            results["patient_id"] = get_field(fields, 3, "")
            results["patient_name"] = get_field(fields, 5, "")
            results["DOB"] = get_field(fields, 7, "")
            results["sex"] = get_field(fields, 8, "")

        elif fields[0] == "PV1":
            results["patient_class"] = get_field(fields, 2, "")
            results["assigned_location"] = get_field(fields, 3, "").replace("^", " ")

        elif fields[0] == "ORC":
            results["order_id"] = get_field(fields, 2, "")

        elif fields[0] == "OBR":
            results["test_requested"] = get_field(fields, 4, "")

        elif fields[0] == "NTE":
            results["notes"] = get_field(fields, 3, "")

        elif fields[0] == "OBX":
            local_dict = {
                "obser_test": get_field(fields, 3, "").replace("^", " "),
                "ObserValue": get_field(fields, 5, ""),
                "units": get_field(fields, 6, ""),
                "abn_flag": get_field(fields, 8, ""),
            }
            results["observations"].append(local_dict)

    return results
