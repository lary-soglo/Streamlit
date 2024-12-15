import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


import streamlit as st
import pandas as pd

# Titre de l'application
st.title("Importation de vos données")

# Champ pour importer un fichier CSV
file = st.file_uploader("Importer vos données ici (format CSV uniquement)", type=["csv"])

# Vérification si un fichier a été téléchargé
if file is not None:
    try:
        # Lire le fichier téléchargé dans un DataFrame pandas
        df = pd.read_csv(file)

        # Afficher un message de succès
        st.success("Fichier chargé avec succès !")

        # Afficher les 5 premières lignes du fichier
        st.write("### Aperçu des données :")
        st.dataframe(df.head())  # Affiche un tableau interactif

        # Afficher des informations supplémentaires (facultatif)
        st.write("### Dimensions des données :")
        st.write(f"Nombre de lignes : {df.shape[0]}")
        st.write(f"Nombre de colonnes : {df.shape[1]}")
    except Exception as e:
        st.error(f"Erreur lors de la lecture du fichier : {e}")
else:
    st.info("Veuillez télécharger un fichier pour commencer.")
 
  # Charger le fichier CSV avec les bons noms de colonnes
try:
    iris_data = pd.read_csv('iris.csv', names=[
        'sepal_length', 'sepal_width', 'petal_length', 'petal_width', 
        'species_numeric', 'unused_col1', 'unused_col2', 'unused_col3', 'species'])
except FileNotFoundError:
    st.error("Le fichier 'iris.csv' est introuvable. Assurez-vous qu'il est dans le même dossier que ce script.")

# Vérifiez si les données ont été correctement chargées avant de continuer
if 'iris_data' in locals():
    # Afficher un aperçu des données
    st.write("### Aperçu des données :")
    st.dataframe(iris_data)
    
 
# Nettoyage des colonnes utilisées pour le graphique
    if 'species_numeric' in iris_data.columns and 'petal_length' in iris_data.columns:
        # Supprimer les lignes avec des valeurs manquantes ou incorrectes
        iris_data_cleaned = iris_data[['species_numeric', 'petal_length']].dropna()

        # Vérifier que chaque espèce a des données valides pour le graphique
        if iris_data_cleaned['species_numeric'].nunique() > 1:
            st.write("### Graphique des longueurs des pétales en fonction des espèces :")
            plt.figure(figsize=(10, 6))
            sns.boxplot(x='species_numeric', y='petal_length', data=iris_data_cleaned)
            st.pyplot(plt)
            plt.close()
        else:
            st.warning("Il n'y a pas assez de catégories distinctes dans la colonne 'species_numeric' pour tracer un graphique.")
    else:
        st.warning("Les colonnes nécessaires ('species_numeric' et 'petal_length') sont absentes ou mal nommées.")
else:
    st.warning("Le chargement des données a échoué. Vérifiez le fichier fourni.")
