# Utilise une image légère de Python
FROM python:3.9-slim

# Installe la bibliothèque "requests"
RUN pip install requests

# Copie le script Python de test dans l’image
COPY test_auth.py /test_auth.py

# Lance automatiquement le test quand le container démarre
CMD ["python", "/test_auth.py"]

