import json
from typing import Any, Dict


def parse_hl7_level1(raw_str_sample: str) -> Dict[str, Any]:
    results = {}
    sample_1 = raw_str_sample.split("\r")
    for item in sample_1:
        fields = item.split("|")

        if fields[0] == "MSH":
            results["message_type"] = fields[8]
            results["message_control_id"] = fields[9]

        elif fields[0] == "PID":
            results["patient_id"] = fields[3]
            results["patient_name"] = fields[5]
            results["DOB"] = fields[7]
            results["sex"] = fields[8]

        elif fields[0] == "PV1":
            results["patient_class"] = fields[2]
            results["assigned_location"] = fields[3].replace("^", " ")

        elif fields[0] == "ORC":
            results["order_id"] = fields[2]

        elif fields[0] == "OBR":
            results["test_requested"] = fields[4]

        elif fields[0] == "NTE":
            results["Notes"] = fields[3]

        elif fields[0] == "OBX":
            results["obser_test"] = fields[3].replace("^", " ")
            results["ObserValue"] = fields[5]
            results["units"] = fields[6]
            results["abn_flag"] = fields[8]

    return results
