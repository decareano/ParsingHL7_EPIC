import json

# Import the function from hl7_parser.py (do NOT include .py in the import)
from parsingHL7 import parse_hl7_to_dict

# 1. Define your sample HL7 string
sample_hl7 = (
    r"MSH|^~\&|EPIC|HOSPITAL_A|AWS_LAMBDA|HEALTH_CLOUD|20260824083000||ADT^A08|MSG100001|P|2.3"
    + "\r"
    r"PID|1||PAT100892^^^HOSPITAL^MRN||DOE^JOHN^A||19850315|M|||123 MAIN ST^^BOSTON^MA^02108"
    + "\r"
    r"OBX|1|NM|GLUCOSE^Glucose Level||105|mg/dL|70-99|H" + "\r"
    r"OBX|2|NM|A1C^Hemoglobin A1c||6.2|%|4.0-5.6|H"
)

# 2. Call the imported function
parsed_dict = parse_hl7_to_dict(sample_hl7)

# 3. Print the formatted result
print(json.dumps(parsed_dict, indent=4))
