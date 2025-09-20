import pandas
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from typing import Tuple
from sklearn.linear_model import Ridge
import array
from sklearn.linear_model import Lasso


def data_processing(df: pandas.DataFrame,columns_to_drop=[]):
    """
    Prétraite un DataFrame pandas pour des tâches d'apprentissage automatique en nettoyant, supprimant les valeurs aberrantes, normalisant les caractéristiques et en divisant en ensembles d'entraînement, de validation et de test.
    Étapes réalisées :
    - Supprime les lignes avec des valeurs manquantes et les doublons.
    - Supprime certaines colonnes catégorielles ("type_batiment", "type_toit", "qualite_cuisine") si présentes.
    - Supprime les valeurs aberrantes de toutes les colonnes sauf "prix" en utilisant la méthode IQR.
    - Supprime les colonnes spécifiées par l'utilisateur et "prix" des caractéristiques.
    - Normalise les caractéristiques avec StandardScaler.
    - Divise les données en ensembles d'entraînement, de validation et de test.
    Arguments :
        df (pandas.DataFrame) : DataFrame d'entrée contenant les caractéristiques et la colonne cible "prix".
        columns_to_drop (list, optionnel) : Liste de colonnes supplémentaires à supprimer des caractéristiques. Par défaut [].
    Retourne :
        tuple : (X, Y, X_train, y_train, X_test, Y_test, X_val, Y_val)
            - X (pandas.DataFrame) : DataFrame des caractéristiques normalisées.
            - Y (pandas.Series) : Variable cible ("prix").
            - X_train (pandas.DataFrame) : Caractéristiques d'entraînement.
            - y_train (pandas.Series) : Cible d'entraînement.
            - X_test (pandas.DataFrame) : Caractéristiques de test.
            - Y_test (pandas.Series) : Cible de test.
            - X_val (pandas.DataFrame) : Caractéristiques de validation.
            - Y_val (pandas.Series) : Cible de validation.
    Exemple :
        >>> import pandas as pd
        >>> df = pd.read_csv("maisons.csv")
        >>> X, Y, X_train, y_train, X_test, Y_test, X_val, Y_val = data_processing(df, columns_to_drop=["surface_jardin"])
    """
    df.dropna(inplace=True)
    df.drop_duplicates(inplace=True)
    
    to_remove = ["type_batiment","type_toit","qualite_cuisine"]
    for col in to_remove:
        if col in df.columns:
            df.drop(columns=[col], inplace=True)

    outliers_columns_check = [col for col in df.columns if col != "prix"]

    ratio = 1.5

    for col in outliers_columns_check:
        if col in df.columns:
            q1 = df[col].quantile(0.25)
            q3 = df[col].quantile(0.75)
            iqr = q3 - q1
            lower_bound = q1 - ratio * iqr
            upper_bound = q3 + ratio * iqr
            df = df[(df[col] >= lower_bound) & (df[col] <= upper_bound)]
    
    to_drop = columns_to_drop + ["prix"]
    X = df.drop(columns=to_drop)
    Y = df["prix"]


    # Normalisation
    scaler = StandardScaler()
    X_normalized = scaler.fit_transform(X)

    X = pandas.DataFrame(X_normalized, columns=X.columns)

    X_train, X_test, y_train, Y_test = train_test_split(X, Y, test_size=0.20, random_state=20)

# split data into validation set
    X_train, X_val, y_train, Y_val = train_test_split(X_train, y_train, test_size=0.25, random_state=20)

    return X,Y,X_train, y_train,X_test, Y_test,X_val,Y_val

def model_fit(X:np.array,Y:np.array):
    """
    Ajuste un modèle de régression Lasso avec expansion des caractéristiques polynomiales sur les données d'entrée.

    Paramètres
    ----------
    X : np.array
        Matrice des caractéristiques d'entrée de forme (n_samples, n_features).
    Y : np.array
        Valeurs cibles de forme (n_samples,).

    Retourne
    --------
    model : sklearn.linear_model.Lasso
        Modèle de régression Lasso entraîné.
    poly : sklearn.preprocessing.PolynomialFeatures
        Transformateur de caractéristiques polynomiales ajusté.

    Exemple d'utilisation
    --------------------
    Supposons que vous disposez d'un jeu de données avec les caractéristiques `X` et les valeurs cibles `Y`, et que vous souhaitez ajuster un modèle de régression polynomiale avec régularisation Lasso pour éviter le surapprentissage. Vous pouvez utiliser cette fonction comme suit :
        >>> model, poly = model_fit(X, Y)
        >>> X_new_poly = poly.transform(X_new)
        >>> Y_pred = model.predict(X_new_poly)
    """
    
    p = 4  # Degré du polynôme
    poly = PolynomialFeatures(degree=p)
    X_poly = poly.fit_transform(X)  
    model = Lasso(alpha=700, max_iter=10000) 
    model.fit(X_poly, Y) 
    return model, poly



def model_predict(poly,model,X: np.ndarray):
    """
    Prédit les valeurs de sortie pour les données d'entrée X en utilisant un modèle de régression et une transformation polynomiale.

    Args:
        poly: Un objet de transformation polynomiale (par exemple, PolynomialFeatures) utilisé pour transformer les données d'entrée.
        model: Un modèle de régression entraîné (par exemple, LinearRegression) utilisé pour effectuer la prédiction.
        X (np.ndarray): Un tableau numpy contenant les données d'entrée à prédire.

    Returns:
        np.ndarray: Les valeurs prédites par le modèle pour les données transformées.

    Exemple d'utilisation
    --------------------
    Supposons que vous avez entraîné un modèle et un transformateur polynomial :
        >>> model, poly = model_fit(X_train, y_train)
        >>> Y_pred = model_predict(poly, model, X_test)
    """
    X_poly = poly.transform(X)
    return model.predict(X_poly)