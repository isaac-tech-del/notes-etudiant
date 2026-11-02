# Exigences de sécurité

## Authentification
L'application doit vérifier l'identité de l'utilisateur avant de donner accès aux notes.

## Autorisation
Chaque utilisateur doit accéder uniquement aux données et aux fonctions autorisées pour son rôle.

## Protection des données
Les notes des étudiants doivent être protégées contre les accès et les modifications non autorisés.

## Gestion des jetons
Les jetons d'authentification doivent être vérifiés côté serveur et ne doivent pas être publiés dans le dépôt Git.

## Tests de sécurité
Des tests automatisés doivent vérifier le refus des requêtes sans jeton valide et l'accès autorisé avec un jeton valide.