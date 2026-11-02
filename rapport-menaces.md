# Rapport d'analyse des menaces
## Application de consultation des notes des étudiants

### 1. Description du système
L'application utilise une API web développée avec Flask pour consulter et gérer les notes des étudiants. Les données sont stockées dans une base SQLite.

### 2. Menaces identifiées

#### Flux Étudiant vers API
- Divulgation des notes des étudiants (Information Disclosure) : un utilisateur peut accéder aux notes d'un autre étudiant sans autorisation.
- Modification non autorisée des notes (Tampering) : un utilisateur peut tenter de modifier des notes sans permission.

#### API Web Flask
- Usurpation d'identité (Spoofing) : un utilisateur peut tenter d'utiliser l'identité d'un autre étudiant.
- Élévation des privilèges (Elevation of Privilege) : un étudiant peut tenter d'accéder à des fonctions réservées à un enseignant ou à un administrateur.

#### Base de données SQLite
- Modification non autorisée (Tampering) : des données peuvent être modifiées ou supprimées sans autorisation.
- Divulgation des données (Information Disclosure) : les notes peuvent être accessibles à une personne non autorisée.

### 3. Mesures de mitigation
- Mettre en place une authentification sécurisée.
- Vérifier les rôles et les autorisations côté serveur.
- Limiter l'accès au fichier SQLite.
- Journaliser les opérations importantes.
- Effectuer des sauvegardes régulières.
- Surveiller la disponibilité de l'API.

### 4. Conclusion
L'analyse STRIDE permet d'identifier les principaux risques liés à l'identité, à la confidentialité, à l'intégrité et à la disponibilité de l'application. Les mesures proposées contribuent à réduire ces risques.