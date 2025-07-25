from app import create_app
from dotenv import load_dotenv
import os

# Încarcă automat fișierul de variabile
if os.path.exists('.env.local'):
    print("🔧 Using .env.local")
    load_dotenv('.env.local')
else:
    print("🔧 Using .env")
    load_dotenv('.env')

app = create_app()

if __name__ == "__main__":
    debug = os.getenv("FLASK_DEBUG", "False").lower() in ("1", "true", "yes")
    port = int(os.getenv("PORT", 5000))
    app.run(debug=debug, host="0.0.0.0", port=port)
