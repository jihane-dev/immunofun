from pathlib import Path
import json
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_extras.let_it_rain import rain

# === Directories and file paths ===
THIS_DIR = Path(__file__).parent
CSS_FILE = THIS_DIR / "style" / "style.css"
ASSETS = THIS_DIR / "assets"
LOTTIE_ANIMATION = ASSETS / "immuno.json"

# === Load Lottie animation ===
def load_lottie_animation(file_path):
    with open(file_path, "r") as f:
        return json.load(f)

# === immuno animation effect ===
def run_immuno_animation():
    rain(emoji="🔬", font_size=20, falling_speed=5, animation_length="infinite")

# === Get user name from URL ===
def get_person_name():
    query_params = st.experimental_get_query_params()
 # Updated to use `st.query_params`
    return query_params.get("name", ["Chers professeurs"])[0]

# === Page configuration ===
st.set_page_config(page_title="Immuno-Fun", page_icon="🧫")

# === Start immuno animation ===
run_immuno_animation()

# === Load and apply CSS ===
with open(CSS_FILE) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# === Personalized greeting ===
PERSON_NAME = get_person_name()
st.markdown(f"<h1 style='text-align: center;'>🧫 Immuno-fun : Innovation au service de l’enseignement  🦠</h1>", unsafe_allow_html=True)
st.markdown(f"<h3 style='text-align: center;'>👤 Bienvenus, {PERSON_NAME} !</h3>", unsafe_allow_html=True)

# === Lottie animation display ===
lottie_animation = load_lottie_animation(LOTTIE_ANIMATION)
st_lottie(lottie_animation, key="lottie-immuno", height=300)

# === Inspirational References Section ===
st.markdown("### 🔬 Pour s’inspirer")
st.markdown("""
    > 💬 * « La technologie ne remplacera jamais un grand enseignant, mais la technologie entre les mains d’un grand enseignant peut être transformante. »* — George Couros
    > 💬 *« La meilleure façon de prédire l’avenir, c’est de l’inventer. »* — Alan Kay 
    > 💬 * « Immuno-Fun n’est pas qu’une application, c’est un pont entre l’abstrait et la compréhension réelle. »* — Jihane Jait
""")

st.markdown("---")

st.markdown("### 📚 Références Bibliographiques :")

# Liste des références bibliographiques 
st.markdown("""
1-Basque, J. (2020). Une réflexion sur les fonctions attribuées aux TIC en enseignement universitaire. Revue internationale des technologies en pédagogie universitaire.
2-Centre National d’Éducation et de Formation. (2000). Levier stratégique n°10 : Intégration des technologies de l’information et de la communication dans l’enseignement. Royaume du Maroc.
3-Dehaene, S. (2018). Apprendre ! Les talents du cerveau, le défi des machines. Odile Jacob.
4-Dictionnaire Le Robert. (2000). Dictionnaire Le Robert. Le Robert.
5-Drissi, M. & Kabbaj, M & Taalibi, M.(2009). Programme GENIE au Maroc : TICE et développement professionnel.
6-Drot-Delange, B. (2011). Quiz et jeux sérieux dans l’enseignement. Revue STICEF.
7-Fondation Django Software. (2024). Django documentation.  
8-Gagneux, A. (2001). Évaluer autrement les élèves (brochure). PUF.
9-Jorro, A. & Meirieu, P. (2007). Favoriser l’engagement et la motivation des élèves. Chenelière.
10-Karsenti, T. & Van den Dool, K. (2007). TIC et pédagogie : Intégration des technologies dans les pratiques pédagogiques. De Boeck.
11-Lebrun, M. (2002). Intégrer les TIC : Quelle formation pour les enseignants ? De Boeck Supérieur.
12-Mathey, E. & Merillou, F. (2009). Travailler et faire travailler en équipe. L’enseignement par projet. Revue des sciences de l’éducation, 16, 111–128.
13-Ministère de l’Éducation Nationale. (2005). Programme GENIE (Généralisation des TIC dans l’enseignement). Maroc.
14-Ministère de l’Éducation Nationale. (2021). Cadre de référence des compétences TIC des enseignants. Maroc.
15-MDN Web Docs. (2024). HTML, CSS & JavaScript documentation. Mozilla Foundation. https://developer.mozilla.org/
16-Senteni, A. & Toutisson, A. (2003). L’essor des communautés virtuelles d’apprentissage.
17-Stratégie nationale pour la transformation numérique. (2024). Maroc digital 2030.
18-Sidir, M. & Benchenna, A. (2008). Du recours aux TICE en temps de crise ? Le cas des universités marocaines.
19-Tardif, J. (2006). L’évaluation des compétences : Documenter le parcours de développement. Chenelière Éducation.


 
    **Partagé par [Professeur stagiaire SVT - Jihane.J-  💙]**
    
  

    
    © all rights reserved 2025
    """,
    unsafe_allow_html=True
)
