import streamlit as st
import pandas as pd
import plotly.express as px

# ------------------------
# Настройки страницы
# ------------------------

st.set_page_config(
    page_title="🌌 Space Lab",
    page_icon="🪐",
    layout="wide"
)

# ------------------------
# Dark theme
# ------------------------

st.markdown(
    """
    <style>

    .stApp {
        background-color: #050816;
        color: white;
    }

    h1, h2, h3 {
        color: white;
    }

    p {
        color: white;
    }

    /* КНОПКИ */

    .stButton > button {

        background-color: #1E2A78;

        color: white;

        border-radius: 10px;

        border: 1px solid white;

        font-weight: bold;
    }

    .stButton > button:hover {

        background-color: #3246b8;

        color: white;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ------------------------
# Language buttons
# ------------------------

col_lang1, col_lang2, col_lang3 = st.columns([8, 1, 1])

with col_lang2:

    if st.button("🇮🇹 IT"):
        st.session_state.lang = "it"

with col_lang3:

    if st.button("🇷🇺 RU"):
        st.session_state.lang = "ru"

# ------------------------
# Default language
# ------------------------

if "lang" not in st.session_state:
    st.session_state.lang = "it"

lang = st.session_state.lang

# ------------------------
# Переводы
# ------------------------

translations = {

    "ru": {

        "title":
        "🌌 Космическая лаборатория",

        "subtitle":
        "Исследуйте планеты Солнечной системы 🚀",

        "about_you":
        "🧒 Расскажите о себе",

        "your_age":
        "🎂 Сколько вам лет на Земле?",

        "your_weight":
        "⚖️ Сколько вы весите на Земле?",

        "choose_planet":
        "🪐 Выберите планету",

        "distance":
        "☀️ Расстояние до Солнца",

        "temperature":
        "🌡 Средняя температура",

        "year":
        "📅 Длина года",

        "radius":
        "🌍 Радиус",

        "day":
        "🕐 Сутки длятся",

        "summer":
        "☀️ Лето длится",

        "your_results":
        "🤯 А что насчёт вас?",

        "your_planet_weight":
        "⚖️ Ваш вес на планете",

        "your_planet_age":
        "🎂 Ваш возраст на планете",

        "earth":
        "🌍 Земля",

        "planet_map":
        "🌌 Карта планет",

        "fact":
        "🚀 Космический факт",

        "graph_help":
        "🤔 Как читать космическую карту?"
    },

    "it": {

        "title":
        "🌌 Laboratorio Spaziale",

        "subtitle":
        "Esplora i pianeti del Sistema Solare 🚀",

        "about_you":
        "🧒 Raccontaci di te",

        "your_age":
        "🎂 Quanti anni hai sulla Terra?",

        "your_weight":
        "⚖️ Quanto pesi sulla Terra?",

        "choose_planet":
        "🪐 Scegli un pianeta",

        "distance":
        "☀️ Distanza dal Sole",

        "temperature":
        "🌡 Temperatura media",

        "year":
        "📅 Durata dell'anno",

        "radius":
        "🌍 Raggio",

        "day":
        "🕐 Durata del giorno",

        "summer":
        "☀️ Durata dell'estate",

        "your_results":
        "🤯 E tu?",

        "your_planet_weight":
        "⚖️ Il tuo peso sul pianeta",

        "your_planet_age":
        "🎂 La tua età sul pianeta",

        "earth":
        "🌍 Terra",

        "planet_map":
        "🌌 Mappa dei pianeti",

        "fact":
        "🚀 Curiosità spaziale",

        "graph_help":
        "🤔 Come leggere la mappa?"
    }
}

t = translations[lang]

# ------------------------
# Названия планет
# ------------------------

planet_names = {

    "ru": {
        "Mercury": "Меркурий",
        "Venus": "Венера",
        "Earth": "Земля",
        "Mars": "Марс",
        "Jupiter": "Юпитер",
        "Saturn": "Сатурн",
        "Uranus": "Уран",
        "Neptune": "Нептун"
    },

    "it": {
        "Mercury": "Mercurio",
        "Venus": "Venere",
        "Earth": "Terra",
        "Mars": "Marte",
        "Jupiter": "Giove",
        "Saturn": "Saturno",
        "Uranus": "Urano",
        "Neptune": "Nettuno"
    }
}

# ------------------------
# Данные
# ------------------------

planets = pd.DataFrame({

    "planet": [
        "Mercury",
        "Venus",
        "Earth",
        "Mars",
        "Jupiter",
        "Saturn",
        "Uranus",
        "Neptune"
    ],

    "distance": [
        58,
        108,
        150,
        228,
        778,
        1430,
        2870,
        4500
    ],

    "radius": [
        2440,
        6052,
        6371,
        3390,
        69911,
        58232,
        25362,
        24622
    ],

    "temperature": [
        167,
        464,
        15,
        -65,
        -110,
        -140,
        -195,
        -200
    ],

    "year_days": [
        88,
        225,
        365,
        687,
        4333,
        10759,
        30687,
        60190
    ],

    "gravity": [
        0.38,
        0.91,
        1.0,
        0.38,
        2.34,
        1.06,
        0.92,
        1.19
    ]
})

# ------------------------
# Картинки
# ------------------------

planet_images = {

    "Mercury":
    "https://upload.wikimedia.org/wikipedia/commons/4/4a/Mercury_in_true_color.jpg",

    "Venus":
    "https://upload.wikimedia.org/wikipedia/commons/e/e5/Venus-real_color.jpg",

    "Earth":
    "https://upload.wikimedia.org/wikipedia/commons/9/97/The_Earth_seen_from_Apollo_17.jpg",

    "Mars":
    "https://upload.wikimedia.org/wikipedia/commons/0/02/OSIRIS_Mars_true_color.jpg",

    "Jupiter":
    "https://upload.wikimedia.org/wikipedia/commons/e/e2/Jupiter.jpg",

    "Saturn":
    "https://upload.wikimedia.org/wikipedia/commons/c/c7/Saturn_during_Equinox.jpg",

    "Uranus":
    "https://upload.wikimedia.org/wikipedia/commons/3/3d/Uranus2.jpg",

    "Neptune":
    "https://upload.wikimedia.org/wikipedia/commons/5/56/Neptune_Full.jpg"
}

# ------------------------
# Цвета планет
# ------------------------

planet_colors = {

    "Mercury": "#B7B7B7",
    "Venus": "#E6C229",
    "Earth": "#3FA9F5",
    "Mars": "#D1495B",
    "Jupiter": "#D9A066",
    "Saturn": "#F4D58D",
    "Uranus": "#72DDF7",
    "Neptune": "#4361EE"
}

# ------------------------
# Заголовок
# ------------------------

st.title(t["title"])

st.write(t["subtitle"])

# ------------------------
# Данные ребёнка
# ------------------------

st.subheader(t["about_you"])

col_a, col_b = st.columns(2)

with col_a:

    child_age = st.slider(
        t["your_age"],
        1,
        100,
        9
    )

with col_b:

    child_weight = st.slider(
        t["your_weight"],
        10,
        150,
        30
    )

# ------------------------
# Планета
# ------------------------

planet_options = [
    planet_names[lang][p]
    for p in planets["planet"]
]

selected_display = st.selectbox(
    t["choose_planet"],
    planet_options
)

reverse_mapping = {
    planet_names[lang][k]: k
    for k in planet_names[lang]
}

planet_name = reverse_mapping[selected_display]

planet = planets[
    planets["planet"] == planet_name
].iloc[0]

# ------------------------
# Расчёты
# ------------------------

planet_weight = child_weight * planet["gravity"]

planet_age = (
    child_age * 365 /
    planet["year_days"]
)

# ------------------------
# Карточка планеты
# ------------------------

st.subheader(f"🪐 {selected_display}")

col1, col2 = st.columns([1, 2])

with col1:

    st.image(
        planet_images[planet_name],
        width=280
    )

with col2:

    st.metric(
        t["distance"],
        f"{planet['distance']} mln km"
    )

    st.metric(
        t["temperature"],
        f"{planet['temperature']} °C"
    )

    st.metric(
        t["year"],
        f"{planet['year_days']} days"
    )

    st.metric(
        t["radius"],
        f"{planet['radius']} km"
    )

# ------------------------
# Ваши данные
# ------------------------

st.subheader(t["your_results"])

col3, col4 = st.columns(2)

with col3:

    st.metric(
        t["your_planet_weight"],
        f"{planet_weight:.1f} kg"
    )

with col4:

    st.metric(
        t["your_planet_age"],
        f"{planet_age:.1f}"
    )

# ------------------------
# Человечки
# ------------------------

st.subheader("🧍 Gravity Comparison")

earth_size = 120

planet_size = earth_size * planet["gravity"]

planet_size = max(50, min(planet_size, 300))

human_col1, human_col2 = st.columns(2)

with human_col1:

    st.markdown(
        f"<h3 style='text-align:center;'>{t['earth']}</h3>",
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div style='
            text-align:center;
            font-size:{earth_size}px;
        '>
        🧍
        </div>
        """,
        unsafe_allow_html=True
    )

with human_col2:

    st.markdown(
        f"<h3 style='text-align:center;'>🪐 {selected_display}</h3>",
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div style='
            text-align:center;
            font-size:{planet_size}px;
        '>
        🧍
        </div>
        """,
        unsafe_allow_html=True
    )

# ------------------------
# Bubble chart
# ------------------------

st.subheader(t["planet_map"])

fig = px.scatter(
    planets,
    x="distance",
    y="temperature",
    size="radius",
    text="planet",
    size_max=60
)

fig.update_traces(

    marker=dict(

        color=[
            planet_colors[p]
            for p in planets["planet"]
        ],

        line=dict(
            width=2,
            color="white"
        )

    ),

    textposition="top center",

    textfont=dict(
        color="white",
        size=14
    )
)

fig.update_layout(

    paper_bgcolor="#050816",

    plot_bgcolor="#050816",

    font_color="white",

    showlegend=False,

    xaxis=dict(
        showgrid=False
    ),

    yaxis=dict(
        showgrid=False
    )
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ------------------------
# Help
# ------------------------

with st.expander(t["graph_help"]):

    if lang == "ru":

        st.write(
            """
🔵 Чем больше пузырь — тем больше планета.

☀️ Чем правее планета — тем дальше она от Солнца.

🌡 Чем выше планета — тем она горячее.
"""
        )

    else:

        st.write(
            """
🔵 Più grande è il cerchio, più grande è il pianeta.

☀️ Più a destra è il pianeta, più è lontano dal Sole.

🌡 Più in alto è il pianeta, più è caldo.
"""
        )
