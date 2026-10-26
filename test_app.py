from app import app

client = app.test_client()


# Test 1 : Vérifier la page d'accueil
def test_accueil():
    reponse = client.get("/")
    assert reponse.status_code == 200


# Test 2 : Vérifier l'état du service
def test_health():
    reponse = client.get("/health")
    assert reponse.status_code == 200
    assert reponse.get_json()["status"] == "ok"


# Test 3 : Vérifier la liste des notes
def test_liste_notes():
    reponse = client.get("/notes")
    assert reponse.status_code == 200
    assert len(reponse.get_json()) >= 2


# Test 4 : Rechercher la note d'un étudiant
def test_recherche_etudiant():
    reponse = client.get("/notes?etudiant=Amina")
    assert reponse.status_code == 200

    notes = reponse.get_json()
    assert len(notes) > 0
    assert notes[0]["note"] == 15.5
    
def test_version():
    response = client.get("/version")

    assert response.status_code == 200

    data = response.get_json()
    assert data["application"] == "notes-etudiant"
    assert data["version"] == "1.0.0"