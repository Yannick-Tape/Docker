import os
import requests

api_address = 'api'  # nom du container de l'API dans docker-compose
api_port = 8000

users = [
    ("alice", "wonderland", 200),
    ("bob", "builder", 200),
    ("clementine", "mandarine", 403)
]

for username, password, expected_code in users:
    r = requests.get(
        url=f"http://{api_address}:{api_port}/permissions",
        params={"username": username, "password": password}
    )

    output = f"""
============================
    Authentication test
============================

request done at "/permissions"
| username="{username}"
| password="{password}"

Expected result = {expected_code}; 
Actual result   = {r.status_code}

==> {"SUCCESS" if r.status_code == expected_code else "FAILURE"}

"""

    print(output)

    if os.environ.get("LOG") == "1":
        with open("/log/api_test.log", "a") as file:
            file.write(output)

