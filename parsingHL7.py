import json
import re


def parse_hl7_to_dict(hl7_raw_str):
    results = {}
    lines = hl7_raw_str.split("\r")
    for line in lines:
        if not line.strip():
            continue
        fields = line.split("|")
        segment_name = fields[0]

        if fields[0] == "PID":
            results["patient_id"] = fields[3]
            results["patient_name"] = fields[5].replace("^", " ")
            results["DOB"] = fields[7]
            results["Gender"] = fields[8]
        elif fields[0] == "MSH":
            results["message_type"] = fields[8]
            results["message_control_id"] = fields[9]
        elif fields[0] == "PV1":
            results["patient_class"] = fields[2]
            results["assigned_location"] = fields[3]
        elif segment_name.startswith("Z"):
            sub_dict = {}
            for index in range(1, len(fields)):
                if fields[index]:
                    if "^" in fields[index]:
                        sub_dict[f"field_{index}"] = fields[index].split("^")
                    else:
                        sub_dict[f"field_{index}"] = fields[index]
            results[segment_name] = sub_dict

    return results
