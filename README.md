# Ayomi NPI

Heya !

J'espère que tout le monde va bien. :)

L'exercice était extrêmement fun, surtout que j'aime toujours fiddle avec ce genre d'algo et d'exercices.

Le projet est composé d'un dossier `server` comportant l'API et la connexion à la DB SQLite (fichier `calculations.db`), ainsi que d'un dossier `app` comportant l'application React. Les deux dossiers ont des `dockerfiles` définissant leurs images, et un `docker-compose.yml` se trouve à la racine du projet.

## Lancement du projet

Le projet est disponible en lançant la commande :

```bash
docker compose up build
```

Cela va rendre l'API disponible sur `localhost:8001` et l'application React sur `localhost:5173`. La documentation OpenAPI est disponible sur `localhost:8001/docs`.

## Fonctionnalités

Calculatrice NPI : Une calculatrice qui utilise la Notation Polonaise Inverse pour effectuer des opérations mathématiques.

Historique des calculs : Tous les calculs sont sauvegardés dans une base de données SQLite pour consultation ultérieure.

Exportation CSV : Possibilité d'exporter l'historique des calculs au format CSV.

## Utilisation

Accéder à l'application en vous rendant sur http://localhost:5173.

Effectuer un calcul :

- Entrez un nombre dans le champ prévu et appuyez sur "Push" ou la touche Entrée.
- Sélectionnez une opération si nécessaire en cliquant sur l'un des boutons opérateurs.
- Répétez l'opération pour construire votre pile NPI.
- Cliquez sur `Calculer` pour obtenir le résultat qui s'affiche en dessous du bouton de soumission.

Cliquez sur `Télécharger les données` pour télécharger un fichier CSV contenant l'historique des calculs.

## Structure du projet

`server` : Contient l'API FastAPI et la base de données SQLite.

`server/calculations.db` : La base de données.

`app` : Contient l'application React.

## Technologies utilisées

Frontend : React, Vite, Tailwind CSS

Backend : FastAPI, Uvicorn, SQLite

## Remarques

Assurez-vous que les ports 8001 et 5173 sont disponibles sur votre machine.

Améliorations futures :

- Améliorer l'API pour mettre en place un système de login et rôles utilisateurs (user qui a accès à la calculatrice, admin qui a accès aux export CSV)
- Implémenter une interface utilisateur plus avancée avec des fonctionnalités supplémentaires (affichages des calculs fait sans devoir passer par l'export, édition de la stack sans devoir recharger la page...).

Sinon, problème que j'ai rencontré et que je n'ai pas trouvé comment résoudre, c'est mon `test_calculate_rpn` qui fail à chaque fois car la base de données me renvoit cette erreur: `sqlalchemy.exc.OperationalError: (sqlite3.OperationalError) attempt to write a readonly database`. J'ai eu beau chercher si c'était des problèmes d'écriture lors du setup du fichier de base de données, et d'autres pistes du même genre, sans rien trouver. :( Je suis à peu près certain que la solution est beaucoup plus simple que je ne l'imagine, mais je dis pas non à quelques conseils !

## Conclusion

Merci d'avoir pris le temps de regarder ce projet ! Si vous avez des questions ou des suggestions, n'hésitez pas à me contacter. J'ai vraiment apprécié travailler sur cet exercice, et j'espère que vous trouverez le résultat intéressant.

Prenez soin de vous et passez une excellente journée ! 😊
