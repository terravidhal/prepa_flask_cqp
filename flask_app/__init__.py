from flask import Flask
from dotenv import load_dotenv
import os

# Charger les variables d'environnement à partir du fichier .env
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")