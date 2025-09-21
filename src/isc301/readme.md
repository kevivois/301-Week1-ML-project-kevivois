README - Utilisation du modèle final

Pour entraîner et utiliser le modèle final de prédiction, il faut utiliser les fonctions suivantes du code fourni :

- `polynomial_lasso_fit` : pour entraîner le modèle Lasso polynomial.
- `polynomial_lasso_model_predict` : pour prédire avec le modèle entraîné.

Exemple d'utilisation :
#### Exemple d'utilisation du modèle final (Lasso polynomial)

import pandas as pd
from isc301 import data_processing, polynomial_lasso_fit, polynomial_lasso_model_predict

#### Charger les données
df = pd.read_csv("maisons.csv")

#### Prétraitement des données
X, Y, X_train, y_train, X_test, Y_test, X_val, Y_val = data_processing(df)

#### Entraînement du modèle Lasso polynomial
model, poly = polynomial_lasso_fit(X_train, y_train, p=2, a=1.0)

#### Prédiction sur l'ensemble de test
Y_pred = polynomial_lasso_model_predict(poly, model, X_test)