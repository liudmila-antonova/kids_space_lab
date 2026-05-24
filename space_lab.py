import streamlit as st
import pandas as pd
import plotly.express as px

# ------------------------
# Настройки страницы
# ------------------------

st.set_page_config(
    page_title="🌌 Космическая лаборатория",
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

    </style>
    """,
    unsafe_allow_html=True
)

# ------------------------
# Данные планет
# ------------------------

planets = pd.DataFrame({

    "planet": [
        "Меркурий",
        "Венера",
        "Земля",
        "Марс",
        "Юпитер",
        "Сатурн",
        "Уран",
        "Нептун"
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
    ],

    "day_length": [
        "58 земных дней",
        "243 земных дня",
        "24 часа",
        "24 часа 37 минут",
        "10 часов",
        "10.7 часа",
        "17 часов",
        "16 часов"
    ],

    "summer_length": [
        "22 земных дня",
        "56 земных дней",
        "93 дня",
        "6 месяцев",
        "3 земных года",
        "7 земных лет",
        "21 земной год",
        "40 земных лет"
    ]

})

# ------------------------
# Картинки планет
# ------------------------

planet_images = {

    "Меркурий":
    "https://upload.wikimedia.org/wikipedia/commons/4/4a/Mercury_in_true_color.jpg",

    "Венера":
    "https://upload.wikimedia.org/wikipedia/commons/e/e5/Venus-real_color.jpg",

    "Земля":
    "https://upload.wikimedia.org/wikipedia/commons/9/97/The_Earth_seen_from_Apollo_17.jpg",

    "Марс":
    "https://upload.wikimedia.org/wikipedia/commons/0/02/OSIRIS_Mars_true_color.jpg",

    "Юпитер":
    "https://upload.wikimedia.org/wikipedia/commons/e/e2/Jupiter.jpg",

    "Сатурн":
    "https://upload.wikimedia.org/wikipedia/commons/c/c7/Saturn_during_Equinox.jpg",

    "Уран":
    "https://upload.wikimedia.org/wikipedia/commons/3/3d/Uranus2.jpg",

    "Нептун":
    "https://upload.wikimedia.org/wikipedia/commons/5/56/Neptune_Full.jpg"
}

# ------------------------
# Цвета планет
# ------------------------

planet_colors = {

    "Меркурий": "#B7B7B7",
    "Венера": "#E6C229",
    "Земля": "#3FA9F5",
    "Марс": "#D1495B",
    "Юпитер": "#D9A066",
    "Сатурн": "#F4D58D",
    "Уран": "#72DDF7",
    "Нептун": "#4361EE"
}

# ------------------------
# Заголовок
# ------------------------

st.title("🌌 Космическая лаборатория")

st.write(
    "Исследуйте планеты Солнечной системы 🚀"
)

# ------------------------
# Данные ребёнка
# ------------------------

st.subheader("🧒 Расскажите о себе")

col_a, col_b = st.columns(2)

with col_a:

    child_age = st.slider(
        "🎂 Сколько вам лет на Земле?",
        1,
        100,
        9
    )

with col_b:

    child_weight = st.slider(
        "⚖️ Сколько вы весите на Земле?",
        10,
        150,
        30
    )

# ------------------------
# Выбор планеты
# ------------------------

planet_name = st.selectbox(
    "🪐 Выберите планету",
    planets["planet"]
)

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

st.subheader(f"🪐 {planet_name}")

col1, col2 = st.columns([1, 2])

# ------------------------
# Картинка
# ------------------------

with col1:

    st.image(
        planet_images[planet_name],
        width=280
    )

# ------------------------
# Метрики
# ------------------------

with col2:

    st.metric(
        "☀️ Расстояние до Солнца",
        f"{planet['distance']} млн км"
    )

    st.metric(
        "🌡 Средняя температура",
        f"{planet['temperature']} °C"
    )

    st.metric(
        "📅 Длина года",
        f"{planet['year_days']} земных дней"
    )

    st.metric(
        "🌍 Радиус",
        f"{planet['radius']} км"
    )

    st.metric(
        "🕐 Сутки длятся",
        planet["day_length"]
    )

    st.metric(
        "☀️ Лето длится",
        planet["summer_length"]
    )

# ------------------------
# Информация о ребёнке
# ------------------------

st.subheader("🤯 А что насчёт вас?")

col3, col4 = st.columns(2)

with col3:

    st.metric(
        "⚖️ Ваш вес на планете",
        f"{planet_weight:.1f} кг"
    )

with col4:

    st.metric(
        "🎂 Ваш возраст на планете",
        f"{planet_age:.1f} лет"
    )

# ------------------------
# Человечки
# ------------------------

st.subheader("🧍 Вы на разных планетах")

earth_size = 120

planet_size = earth_size * planet["gravity"]

planet_size = max(50, min(planet_size, 300))

human_col1, human_col2 = st.columns(2)

# ------------------------
# Земля
# ------------------------

with human_col1:

    st.markdown(
        "<h3 style='text-align:center;'>🌍 Земля</h3>",
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

    st.markdown(
        f"<h2 style='text-align:center;'>{child_weight} кг</h2>",
        unsafe_allow_html=True
    )

# ------------------------
# Планета
# ------------------------

with human_col2:

    st.markdown(
        f"<h3 style='text-align:center;'>🪐 {planet_name}</h3>",
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

    st.markdown(
        f"<h2 style='text-align:center;'>{planet_weight:.1f} кг</h2>",
        unsafe_allow_html=True
    )

# ------------------------
# Bubble chart
# ------------------------

st.subheader("🌌 Карта планет")

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

fig.update_traces(
    hovertemplate=
    "<b>%{text}</b><br><br>" +
    "☀️ Расстояние: %{x} млн км<br>" +
    "🌡 Температура: %{y} °C<br>" +
    "<extra></extra>"
)

fig.update_layout(

    paper_bgcolor="#050816",

    plot_bgcolor="#050816",

    font_color="white",

    xaxis_title="☀️ Расстояние до Солнца (млн км)",

    yaxis_title="🌡 Температура (°C)",

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
# Интересные факты
# ------------------------

st.subheader("🚀 Космический факт")

if planet_name == "Юпитер":

    st.info(
        "Юпитер настолько огромный, "
        "что внутри него поместилось бы "
        "больше 1300 Земель 😄"
    )

elif planet_name == "Марс":

    st.info(
        "На Марсе находится самый большой "
        "вулкан Солнечной системы 🌋"
    )

elif planet_name == "Сатурн":

    st.info(
        "Кольца Сатурна состоят "
        "изо льда и камней ✨"
    )

elif planet_name == "Нептун":

    st.info(
        "На Нептуне бывают ветра "
        "быстрее скорости самолёта 🌪"
    )

elif planet_name == "Венера":

    st.info(
        "Венера горячее Меркурия, "
        "потому что её атмосфера "
        "удерживает тепло 🔥"
    )

# ------------------------
# Объяснение графика
# ------------------------

with st.expander("🤔 Как читать космическую карту?"):

    st.write(
        """
🔵 Чем больше пузырь — тем больше планета.

☀️ Чем правее планета — тем дальше она от Солнца.

🌡 Чем выше планета — тем она горячее.

🎨 Цвет пузыря похож на цвет самой планеты.
"""
    )