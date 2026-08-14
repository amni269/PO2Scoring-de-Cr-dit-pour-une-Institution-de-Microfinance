import streamlit as st
import pandas as pd
import joblib



model = joblib.load("credit_model.pkl")

st.set_page_config(
    page_title="Scoring de Crédit - Microfinance Madina",
    page_icon="💰",
    layout="centered"
)

st.title("💰 Scoring de Crédit - Microfinance Madina")
st.write(
    "Cette application estime le risque de défaut de paiement d'un commerçant "
    "du marché de Madina à partir des informations saisies."
)


st.header("Informations du commerçant")

age = st.number_input(
    "Âge",
    min_value=18,
    max_value=80,
    value=35
)

genre = st.selectbox(
    "Genre",
    ["Homme", "Femme"]
)

situation = st.selectbox(
    "Situation matrimoniale",
    ["Célibataire", "Marié(e)", "Divorcé(e)", "Veuf/Veuve"]
)

nb_charge = st.number_input(
    "Nombre de personnes à charge",
    min_value=0,
    max_value=10,
    value=2
)

secteur = st.selectbox(
    "Secteur d'activité",
    [
        "Alimentation",
        "Tissus & Pagnes",
        "Quincaillerie",
        "Électronique/Téléphonie",
        "Cosmétiques",
        "Restauration",
        "Transport",
        "Autre"
    ]
)

anciennete = st.number_input(
    "Ancienneté de l'activité (années)",
    min_value=0,
    max_value=40,
    value=6
)

revenu = st.number_input(
    "Revenu mensuel (GNF)",
    min_value=500000,
    max_value=50000000,
    value=4500000,
    step=100000
)

membre_tontine = st.selectbox(
    "Membre d'une tontine ?",
    ["Oui", "Non"]
)

mobile_money = st.selectbox(
    "Possède un compte Mobile Money ?",
    ["Oui", "Non"]
)

association = st.selectbox(
    "Membre d'une association de marchands ?",
    ["Oui", "Non"]
)

nb_credits = st.number_input(
    "Nombre de crédits antérieurs",
    min_value=0,
    max_value=20,
    value=1
)

retard = st.selectbox(
    "A déjà eu un retard de paiement ?",
    ["Non", "Oui"]
)

jours_retard = st.number_input(
    "Nombre maximal de jours de retard antérieur",
    min_value=0,
    max_value=365,
    value=0
)

garant = st.selectbox(
    "Garant disponible ?",
    ["Oui", "Non"]
)

score_credit = st.number_input(
    "Score bureau de crédit",
    min_value=300,
    max_value=900,
    value=650
)

montant = st.number_input(
    "Montant du prêt demandé (GNF)",
    min_value=100000,
    max_value=50000000,
    value=1500000,
    step=100000
)

duree = st.number_input(
    "Durée du prêt (mois)",
    min_value=1,
    max_value=60,
    value=12
)

# Ratio prêt / revenu
ratio = montant / revenu if revenu > 0 else 0

st.header("Politique de risque")

threshold = st.selectbox(
    "Seuil de décision",
    [0.30, 0.50],
    index=0
)


if st.button("Prédire"):

    client = pd.DataFrame({
        "id_client": [1],
        "age": [age],
        "genre": [genre],
        "situation_matrimoniale": [situation],
        "nb_personnes_charge": [nb_charge],
        "secteur_activite": [secteur],
        "anciennete_activite_annees": [anciennete],
        "revenu_mensuel_gnf": [revenu],
        "membre_tontine": [membre_tontine],
        "possede_mobile_money": [mobile_money],
        "membre_association_marchands": [association],
        "nb_credits_anterieurs": [nb_credits],
        "a_deja_eu_retard": [retard],
        "jours_retard_max_anterieur": [jours_retard],
        "garant_disponible": [garant],
        "score_bureau_credit": [score_credit],
        "montant_pret_demande_gnf": [montant],
        "duree_pret_mois": [duree],
        "ratio_pret_revenu": [ratio]
    })

    # Probabilité de défaut
    proba = model.predict_proba(client)[0][1]

    # Décision selon le seuil choisi
    prediction = int(proba >= threshold)

    st.subheader("Résultat de l'analyse")

    st.metric("Probabilité de défaut", f"{proba:.1%}")
    st.metric("Seuil utilisé", f"{threshold:.2f}")

    if prediction == 1:
        st.error("❌ Crédit refusé – Risque élevé")
        st.write(
            "Le modèle estime que le risque de défaut est supérieur au seuil choisi. "
            "Le dossier devrait être examiné plus attentivement avant toute décision d'octroi."
        )
    else:
        st.success("✅ Crédit accordé – Bon risque")
        st.write(
            "Le risque estimé est inférieur au seuil choisi. "
            "Le profil est considéré comme relativement solvable par le modèle."
        )

    st.write("---")
    st.write("### Exemple de démonstration")
    st.write(
        "Pour la soutenance, vous pouvez utiliser un commerçant de **35 ans**, "
        "exerçant depuis **6 ans**, avec un revenu mensuel de **4 500 000 GNF**, "
        "qui demande un prêt de **1 500 000 GNF** sur **12 mois**."
    )
