# Docker
Formation Data Engineer


# 🧪 CI/CD Dockerisé pour API de Sentiment Analysis

Ce projet met en place un pipeline de test **automatisé** via Docker Compose pour une API de **Sentiment Analysis** développée avec FastAPI.

---

## 📌 Objectif

Valider automatiquement le bon fonctionnement de l’API avant déploiement grâce à **3 tests automatisés** :

1. ✅ **Authentication** – Vérifie que les utilisateurs peuvent s’authentifier
2. ✅ **Authorization** – Vérifie que les utilisateurs ont accès aux bons modèles (v1/v2)
3. ✅ **Content** – Vérifie que les prédictions de sentiment sont cohérentes

---

## 🗂️ Arborescence du projet

ci_cd_exam/ ├── auth_test/ │ ├── Dockerfile │ └── test_auth.py ├── rights_test/ │ ├── Dockerfile │ └── test_rights.py ├── content_test/ │ ├── Dockerfile │ └── test_content.py ├── log.txt ← Résultat des tests ├── setup.sh ← Script pour tout lancer automatiquement └── docker-compose.yml ← Orchestration multi-conteneurs

yaml
Copy
Edit

---

## 🧰 Prérequis

- Docker installé ✅
- Docker Compose installé ✅

---

## 🚀 Lancement du pipeline

Depuis le dossier `ci_cd_exam`, exécuter :

```bash
chmod +x setup.sh
./setup.sh
Ce script :

Supprime les anciens containers (s’ils existent)

Rebuild toutes les images de test

Lance l’API et les 3 tests

Affiche les résultats dans le terminal

Sauvegarde les logs dans log.txt

📋 Résultats attendus
À la fin, vous devez voir des messages de ce type dans la console et dans log.txt :

bash
Copy
Edit
Authentication test
==> SUCCESS

Authorization test
==> SUCCESS

Content test (v1/v2)
==> SUCCESS
🔍 Détails sur les tests
🔐 auth_test
Vérifie les identifiants :

✅ alice / wonderland

✅ bob / builder

❌ clementine / mandarine

🔒 rights_test
Vérifie les droits :

✅ alice → accès v1 & v2

✅ bob → accès seulement à v1

🧪 content_test
Analyse de phrases :

✅ "life is beautiful" → positif

✅ "that sucks" → négatif

Les deux phrases sont testées avec v1 et v2.

🧼 Nettoyage
Tu peux manuellement arrêter et supprimer tous les containers avec :

bash
Copy
Edit
docker-compose down
Ou supprimer le fichier de log :

bash
Copy
Edit
rm log.txt
📦 Générer une archive pour remise
Depuis le dossier parent :

bash
Copy
Edit
cd ..
tar -czvf ci_cd_exam.tar.gz ci_cd_exam

 
