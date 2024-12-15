import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

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

        # Vérifier la présence des colonnes nécessaires pour le graphique
        if 'species' in df.columns and 'petal_length' in df.columns:
            st.write("### Graphique des longueurs des pétales en fonction des espèces :")
            
            # Nettoyage des données
            df_cleaned = df[['species', 'petal_length']].dropna()

            # Vérification qu'il y a plusieurs espèces distinctes pour afficher le graphique
            if df_cleaned['species'].nunique() > 1:
                plt.figure(figsize=(10, 6))
                sns.boxplot(x='species', y='petal_length', data=df_cleaned)
                st.pyplot(plt)
                plt.close()  # Ferme la figure après son rendu
            else:
                st.warning("Il n'y a pas assez de catégories distinctes dans la colonne 'species' pour tracer un graphique.")
        else:
            st.warning("Les colonnes nécessaires ('species' et 'petal_length') sont absentes ou mal nommées.")
            
    except Exception as e:
        st.error(f"Erreur lors de la lecture du fichier : {e}")
else:
    st.info("Veuillez télécharger un fichier pour commencer.")
