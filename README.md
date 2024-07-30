# Exercice 1

Pour l'exercice 1, vous trouverez mon modèle de données relationnel dans le dossier exercice 1.


# Exercice 2 2 en Flask

Pour l'exercice 2, vous le trouverez dans le dossier exercice 2.

# Note exercice

## explication du code rapidement

### Gestion des Clients, Produit, Facture etc... :

C'est principalement le même schéma :

GET /clients : Récupère tous les clients.
POST /clients : Ajoute un nouveau client.
GET /clients/{id} : Récupère les informations d'un client spécifique.
PUT /clients/{id} : Met à jour les informations d'un client spécifique.
DELETE /clients/{id} : Supprime un client.

Gestion des Produits :

GET /produits : Récupère tous les produits.
POST /produits : Ajoute un nouveau produit.
GET /produits/{id} : Récupère les informations d'un produit spécifique.
PUT /produits/{id} : Met à jour les informations d'un produit spécifique.
DELETE /produits/{id} : Supprime un produit.

Gestion des Taux de TVA :

GET /taux_tva : Récupère tous les taux de TVA.
POST /taux_tva : Ajoute un nouveau taux de TVA.
GET /taux_tva/{id} : Récupère les informations d'un taux de TVA spécifique.
PUT /taux_tva/{id} : Met à jour les informations d'un taux de TVA spécifique.
DELETE /taux_tva/{id} : Supprime un taux de TVA.

Gestion des Factures :

GET /factures : Récupère toutes les factures.
POST /factures : Ajoute une nouvelle facture.
GET /factures/{id} : Récupère les informations d'une facture spécifique.
PUT /factures/{id} : Met à jour les informations d'une facture spécifique.
DELETE /factures/{id} : Supprime une facture.


## Remarque ou  d’éventuelles possibilités d’évolutions :

Pour utiliser l'API, on devrait ajouter une gestion d'authentification et de validation,
ainsi qu'une gestion des erreurs plus robuste. 
