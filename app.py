import os
import sqlite3
from flask import Flask, jsonify, request

app = Flask(__name__)

# Fichier où sont conservées les notes
DB = "notes.db"


# Initialisation de la base de données
def init_db():
    with sqlite3.connect(DB) as con:
        con.execute(
            "CREATE TABLE IF NOT EXISTS notes "
            "(id INTEGER PRIMARY KEY, etudiant TEXT, module TEXT, note REAL)"
        )

        # Ajouter des notes si la base est vide
        if con.execute("SELECT COUNT(*) FROM notes").fetchone()[0] == 0:
            con.executemany(
                "INSERT INTO notes (etudiant, module, note) VALUES (?, ?, ?)",
                [
                    ("Amina", "DevSecOps", 15.5),
                    ("Youssef", "DevSecOps", 12.0),
                ],
            )


# Préparer la base de données au démarrage
init_db()


# Page d'accueil
@app.route("/")
def accueil():
    return (
        "<!DOCTYPE html>"
        "<html lang='fr'>"
        "<head><meta charset='utf-8'>"
        "<title>Notes des étudiants</title></head>"
        "<body>"
        "<h1>Consultation des notes</h1>"
        "<p><a href='/notes'>Voir les notes</a></p>"
        "</body></html>"
    )


# Vérifier le fonctionnement de l'application
@app.route("/health")
def health():
    return jsonify(status="ok")


# Consulter et rechercher les notes
@app.route("/notes")
def lister_notes():
    etudiant = request.args.get("etudiant", "")

    with sqlite3.connect(DB) as con:
        rows = con.execute(
            "SELECT id, etudiant, module, note "
            "FROM notes WHERE etudiant LIKE ?",
            (f"%{etudiant}%",),
        ).fetchall()

    return jsonify(
        [
            {
                "id": r[0],
                "etudiant": r[1],
                "module": r[2],
                "note": r[3],
            }
            for r in rows
        ]
    )


# Démarrer le serveur
if __name__ == "__main__":
    app.run(
        host=os.environ.get("APP_HOST", "127.0.0.1"),
        port=5000,
    )
