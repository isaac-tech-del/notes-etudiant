
from app import app


client = app.test_client()


# Tester la page d'accueil
def test_accueil():
    reponse = client.get("/")
    assert reponse.status_code == 200


# Tester l'état de santé de l'application
def test_health():
    reponse = client.get("/health")
    assert reponse.status_code == 200

    donnees = reponse.get_json()
    assert donnees["status"] == "ok"


# Tester la consultation de toutes les notes
def test_liste_notes():
    reponse = client.get(
        "/notes",
        headers={
            "Authorization": "Bearer TOKEN_TEST_ENSEIGNANT"
        }
    )

    assert reponse.status_code == 200
    notes = reponse.get_json()
    assert len(notes) >= 2


# Tester la recherche des notes d'Amina
def test_recherche_etudiant():
    reponse = client.get(
        "/notes?etudiant=Amina",
        headers={
            "Authorization": "Bearer TOKEN_TEST_ENSEIGNANT"
        }
    )

    assert reponse.status_code == 200

    notes = reponse.get_json()
    assert len(notes) >= 1
    assert notes[0]["etudiant"] == "Amina"
    assert notes[0]["note"] == 15.5


# Tester la version de l'application
def test_version():
    reponse = client.get("/version")

    assert reponse.status_code == 200

    donnees = reponse.get_json()
    assert donnees["application"] == "notes-etudiant"
    assert donnees["version"] == "1.0.0"
