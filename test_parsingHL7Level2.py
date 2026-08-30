import json

# Import the function from hl7_parser.py (do NOT include .py in the import)
from parsingHL7Level2 import parse_hl7_level2

# 1. Define your sample HL7 string
Techsample_hl7_level1 = (
    r"MSH|^~\&|LAB_SYS|HOSPITAL_A|EHR_SYS|HEALTH_CLOUD|20260824083000||ORM^O01|MSG200001|P|2.3"
    + "\r"
    r"PID|1||PAT100892^^^HOSPITAL^MRN||DOE^JOHN^A||19850315|M" + "\r"
    r"PV1|1|I|ICU^BED01^01||||1234^SMITH^JANE^M^^DR" + "\r"
    r"ORC|NW|ORD9901|LAB7741||IP||||20260824080000" + "\r"
    r"OBR|1|ORD9901|LAB7741|CBC^COMPLETE BLOOD COUNT|||20260824081500" + "\r"
    r"NTE|1|L|Patient fasting for 12 hours prior to draw" + "\r"
    r"OBX|1|NM|678-7^WBC^LN||7.5|10*3/uL|4.5-11.0|N|||F" + "\r"
    r"OBX|2|NM|789-8^RBC^LN||4.8|10*6/uL|4.2-5.4|N|||F" + "\r"
    r"ORC|NW|ORD9902|LAB7742||IP||||20260824080000" + "\r"
    r"OBR|2|ORD9902|LAB7742|CMP^COMPREHENSIVE METABOLIC PANEL|||20260824081500" + "\r"
    r"OBX|1|NM|2345-7^GLUCOSE^LN||110|mg/dL|70-99|H|||F"
)

# 2. Call the imported function
parsed_dict = parse_hl7_level2(Techsample_hl7_level1)

# 3. Print the formatted result
print(json.dumps(parsed_dict, indent=4))
