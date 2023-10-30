import os

DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "example")
DB_HOST = os.getenv("DB_HOST", "127.0.0.1")
DB_PORT = int(os.getenv("DB_PORT", 27017))
DB_DB = os.getenv("DB_DB", "flask_db")
FLASK_PORT = int(os.getenv('FLASK_PORT', 8080))


