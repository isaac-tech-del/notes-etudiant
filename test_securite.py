
from app import app


def test_notes_sans_jeton():
    client = app.test_client()
    response = client.get("/notes")

    assert response.status_code == 401


def test_notes_avec_jeton_invalide():
    client = app.test_client()
    response = client.get(
        "/notes",
        headers={"Authorization": "Bearer FAUX_TOKEN"}
    )

    assert response.status_code == 401


def test_etudiant_consulte_ses_notes():
    client = app.test_client()
    response = client.get(
        "/notes",
        headers={
            "Authorization": "Bearer TOKEN_TEST_ETUDIANT"
        }
    )

    assert response.status_code == 200

    notes = response.get_json()
    assert len(notes) >= 1

    for note in notes:
        assert note["etudiant"] == "Amina"


def test_enseignant_consulte_les_notes():
    client = app.test_client()
    response = client.get(
        "/notes",
        headers={
            "Authorization": "Bearer TOKEN_TEST_ENSEIGNANT"
        }
    )

    assert response.status_code == 200
    assert len(response.get_json()) >= 2
