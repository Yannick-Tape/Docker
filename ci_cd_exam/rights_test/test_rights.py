import os
import requests

api_address = 'api'
api_port = 8000

users = [
    ("alice", "wonderland", True, True),  # accès v1 et v2
    ("bob", "builder", True, False)       # accès uniquement v1
]

sentence = "testing access"

for username, password, access_v1, access_v2 in users:
    # Test accès /v1
    r_v1 = requests.get(
        url=f"http://{api_address}:{api_port}/v1/sentiment",
        params={"username": username, "password": password, "sentence": sentence}
    )

    # Test accès /v2
    r_v2 = requests.get(
        url=f"http://{api_address}:{api_port}/v2/sentiment",
        params={"username": username, "password": password, "sentence": sentence}
    )

    result_v1 = r_v1.status_code == 200
    result_v2 = r_v2.status_code == 200

    output = f"""
============================
     Authorization test
============================

User: {username}

Test /v1 --> expected: {access_v1}, got: {result_v1}
Test /v2 --> expected: {access_v2}, got: {result_v2}

==> {"SUCCESS" if result_v1 == access_v1 and result_v2 == access_v2 else "FAILURE"}
"""

    print(output)

    if os.environ.get("LOG") == "1":
        with open("/log/api_test.log", "a") as file:
            file.write(output)

