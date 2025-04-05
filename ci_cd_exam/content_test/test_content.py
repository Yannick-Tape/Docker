import os
import requests

# Adresse et port de l’API
api_address = 'api'
api_port = 8000

# Identifiants du compte utilisé pour le test
username = "alice"
password = "wonderland"

# Phrases à tester et leur polarité attendue (+1 = positif, -1 = négatif)
sentences = [
    ("life is beautiful", 1),   # Positif attendu
    ("that sucks", -1)          # Négatif attendu
]

# Versions de modèles à tester
models = ["v1", "v2"]

# Boucle sur les versions et les phrases à tester
for version in models:
    for sentence, expected_sign in sentences:
        r = requests.get(
            url=f"http://{api_address}:{api_port}/{version}/sentiment",
            params={
                "username": username,
                "password": password,
                "sentence": sentence
            }
        )

        if r.status_code == 200:
            # On récupère et force le typage du score en float
            prediction = float(r.json().get("score", 0))
            result_sign = 1 if prediction > 0 else -1
            correct = (result_sign * expected_sign) > 0
        else:
            correct = False

        # Message de sortie formaté
        output = f"""
============================
     Content test ({version})
============================

Sentence: "{sentence}"
Expected: {"positive" if expected_sign > 0 else "negative"}
Returned: {r.json() if r.status_code == 200 else 'ERROR'}

==> {"SUCCESS" if correct else "FAILURE"}

"""

        print(output)

        # Écriture dans le fichier log si LOG = "1"
        if os.environ.get("LOG") == "1":
            with open("/log/api_test.log", "a") as file:
                file.write(output)

