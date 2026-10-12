import os
import json
import requests

url = os.environ.get("AML_ENDPOINT_URL")
key = os.environ.get("AML_ENDPOINT_KEY")

if not url or not key:
    raise SystemExit(
        "ERROR: AML_ENDPOINT_URL or AML_ENDPOINT_KEY is missing."
    )

payload = {
    "input_data": {
        "columns": [
            "air_temp_k",
            "process_temp_k",
            "rpm",
            "torque_nm",
            "tool_wear_min",
            "type"
        ],
        "data": [
            [298.1, 308.6, 1551.0, 42.8, 0.0, "M"],
            [302.5, 310.9, 1325.0, 68.2, 215.0, "L"]
        ]
    }
}

response = requests.post(
    url,
    headers={
        "Authorization": f"Bearer {key}",
        "Content-Type": "application/json"
    },
    json=payload,
    timeout=60
)

print("HTTP Status:", response.status_code)
print("Response:", response.text)
response.raise_for_status()
