import streamlit as st
import os

# --- 1. НАСТРОЙКИ СТРАНИЦЫ И БРЕНДИНГ ---
st.set_page_config(
    page_title="FALKE ONE MOTORSPORT",
    page_icon="miniem.png",
    layout="wide",
    initial_sidebar_state="collapsed"
)




# Стиль: Черный фон, золотые акценты, премиальный вид
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Rajdhani:wght@500;700&family=Montserrat:wght@400;600&display=swap');

    /* Общий фон, */
    .stApp { 
        background-color: #0a0a0a; 
        color: #ffffff; 

    }

    /* Дерзкие заголовки */
    h1, h2, h3 { 
        color: #ffd700 !important; 
        text-align: center; 
        font-family: 'Rajdhani', sans-serif !important;
        font-weight: 700 !important;
        text-transform: uppercase;
        letter-spacing: 2px;
    }

    /* Читабельный основной текст */
    p { 
        font-size: 1.1em; 
        line-height: 1.6; 
        font-family: 'Montserrat', sans-serif;
        color: #e0e0e0;
    }

    /* КАРТОЧКИ ПИЛОТОВ (Стеклянный эффект) */
    .pilot-card {
        background-color: rgba(30, 30, 30, 0.4); /* Полупрозрачный фон */
        border: 1px solid rgba(255, 215, 0, 0.3); /* Тонкая золотая рамка */
        border-radius: 20px; /* Сильное закругление */
        padding: 20px; 
        margin-bottom: 15px; 
        text-align: center;
        backdrop-filter: blur(10px); /* Размытие фона под карточкой */
        transition: transform 0.3s ease;
    }
    .pilot-card:hover {
        transform: translateY(-5px); /* Легкий подъем при наведении */
        border-color: #ffd700;
    }
    .pilot-nick { 
        color: #ffd700; 
        font-weight: bold; 
        font-size: 1.3em; 
        font-family: 'Rajdhani', sans-serif; 
        letter-spacing: 1px;
    }
    .pilot-name { color: #aaaaaa; font-size: 0.95em; margin-top: 5px; font-family: 'Montserrat', sans-serif; }

    /* КНОПКИ-ССЫЛКИ (Закругленные и прозрачные) */
    .link-btn {
        display: block; 
        width: 100%; 
        padding: 15px; 
        margin: 12px 0;
        background-color: rgba(255, 215, 0, 0.05); /* Почти прозрачный фон */
        color: #ffd700 !important; 
        text-align: center;
        text-decoration: none; 
        border-radius: 50px; /* Овальная форма */
        font-weight: bold;
        font-family: 'Rajdhani', sans-serif;
        font-size: 1.2em;
        letter-spacing: 1px;
        border: 2px solid #ffd700; /* Золотая рамка */
        transition: all 0.3s ease;
    }
    .link-btn:hover { 
        background-color: #ffd700; 
        color: #000000 !important; 
        box-shadow: 0 0 20px rgba(255, 215, 0, 0.6); /* Золотое свечение */
        transform: translateY(-2px);
    }

    /* КНОПКИ STREAMLIT (Тоже делаем красивыми) */
    .stButton>button {
        background-color: rgba(255, 215, 0, 0.1) !important;
        border: 2px solid #ffd700 !important;
        border-radius: 50px !important;
        color: #ffd700 !important;
        font-family: 'Rajdhani', sans-serif !important;
        font-weight: 700 !important;
        letter-spacing: 1px;
        transition: all 0.3s ease !important;
    }
    .stButton>button:hover { 
        background-color: #ffd700 !important; 
        color: #000000 !important;
        box-shadow: 0 0 15px rgba(255, 215, 0, 0.5) !important;
    }
    /* Ограничиваем ширину контента по центру */
.block-container {
    max-width: 1150px !important;
    margin: 0 auto !important;
}
    </style>
""", unsafe_allow_html=True)




# --- 2. ГЛАВНЫЙ ЭКРАН ---
st.markdown("<h1>FALKE ONE MOTORSPORT</h1>", unsafe_allow_html=True)

if os.path.exists("Images/emblem.png"):
    # Эмблема с фиксированной шириной (300 пикселей)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image("Images/emblem.png", width=1500)
else:
    st.info("📸 Положи файл emblem.png в папку с проектом, чтобы увидеть эмблему!")


# --- 3. О КОМАНДЕ ---
st.markdown("---")
st.markdown("<h2>О КОМАНДЕ</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #888; margin-top: -20px; margin-bottom: 20px;'>Наша команда создана 06.09.2026 и развивается с каждым днём! </p>", unsafe_allow_html=True)
st.markdown("""
**FALKE ONE MOTORSPORT** - это не просто команда симрейсеров. Это сообщество симрейсеров, которые создают и ценят честную физику, инженерный подход и взаимное уважение. 
Мы не просто "катаем с рулём", мы строим империю. Наша цель -  попасть в историю симрейсинга,  победы в серьезных киберспортивных сериях на платформе Low Fuel Motorsport.
""")


# --- 3.1. МУЛЬТИ-ПЛАТФОРМЕННОСТЬ ---
st.markdown("---")
st.markdown("<h2>НАШИ СИМУЛЯТОРЫ</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #888; margin-top: -20px; margin-bottom: 20px;'>Объединяет пилотов всех популярных платформ</p>", unsafe_allow_html=True)

# Верхний текст в стеклянной фигуре
st.markdown("""
<div style="
    background-color: rgba(30, 30, 30, 0.4); 
    border: 1px solid rgba(255, 215, 0, 0.3); 
    border-radius: 20px; 
    padding: 20px; 
    text-align: center;
    margin-bottom: 20px;
">
    <p style="font-size: 1.15em; color: #e0e0e0; margin: 0;">
        Мы не ограничиваем себя одной игрой. <b style="color: #ffd700;">FALKE ONE MOTORSPORT</b> - это сообщество пилотов, которые катают на всех топовых симуляторах:
    </p>
</div>
""", unsafe_allow_html=True)

# Создаем 3 колонки с карточками в стиле пилотов
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="pilot-card">
        <div class="pilot-nick">ASSETTO CORSA</div>
        <div class="pilot-name">AC</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div style="margin-top: 10px;">', unsafe_allow_html=True)
    if os.path.exists("Images/ac_bg.png"):
        st.image("Images/ac_bg.png", use_container_width=True)
    elif os.path.exists("ac_bg.jpg"):
        st.image("ac_bg.jpg", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="pilot-card">
        <div class="pilot-nick">ASSETTO CORSA COMPETIZIONE</div>
        <div class="pilot-name">ACC</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div style="margin-top: 10px;">', unsafe_allow_html=True)
    if os.path.exists("Images/acc_bg.png"):
        st.image("Images/acc_bg.png", use_container_width=True)
    elif os.path.exists("acc_bg.jpg"):
        st.image("acc_bg.jpg", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="pilot-card">
        <div class="pilot-nick">AUTOMOBILISTA 2</div>
        <div class="pilot-name">AMS2</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div style="margin-top: 10px;">', unsafe_allow_html=True)
    if os.path.exists("Images/ams2_bg.png"):
        st.image("Images/ams2_bg.png", use_container_width=True)
    elif os.path.exists("ams2_bg.jpg"):
        st.image("ams2_bg.jpg", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Нижний текст
st.markdown("""
<div style="
    background-color: rgba(30, 30, 30, 0.4); 
    border: 1px solid rgba(255, 215, 0, 0.3); 
    border-radius: 20px; 
    padding: 20px; 
    text-align: center;
    margin-top: 20px;
">
    <p style="font-size: 1.1em; color: #e0e0e0; margin: 0;">
        Каждый пилот выбирает свой симулятор, но все мы - одна команда. 
    </p>
</div>
""", unsafe_allow_html=True)


# --- 4.СОСТАВ (ПИЛОТЫ) ---
st.markdown("---")
st.markdown("<h2>Состав</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #888;'>Те, кто пишет историю команды</p>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="pilot-card">
        <div class="pilot-nick">FALKE1_1 #145</div>
        <div class="pilot-name">Семёнов Арсений</div>
        <div style="color: #ffd700; font-size: 0.8em; margin-top: 5px;">Team Principal / Lead Driver/𝗙𝟏𝗣𝗲𝗿𝗳𝗼𝗿𝗺𝗮𝗻𝗰𝗲 Senior Engineer ⚒︎ </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="pilot-card">
        <div class="pilot-nick">IvAn #15</div>
        <div class="pilot-name">Николаев Иван</div>
        <div style="color: #ffd700; font-size: 0.8em; margin-top: 5px;">Race Driver AC</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="pilot-card">
        <div class="pilot-nick">taifunvozduh #17</div>
        <div class="pilot-name">Омеги Геннадий </div>
        <div style="color: #ffd700; font-size: 0.8em; margin-top: 5px;">Race Driver AC</div>
    </div>
    """, unsafe_allow_html=True)

with col1:
    st.markdown("""
    <div class="pilot-card">
        <div class="pilot-nick">sKIF #16</div>
        <div class="pilot-name"> Афанасьев Матвей</div>
        <div style="color: #ffd700; font-size: 0.8em; margin-top: 5px;">Race Driver AC</div>
    </div>
    """, unsafe_allow_html=True)



# --- 5. НАША МАШИНА ---
st.markdown("---")
st.markdown("<h2>БОЛИДЫ </h2>", unsafe_allow_html=True)
if os.path.exists("Images/car.jpg"):
    st.image("Images/car.jpg", caption="BMW M4 2021 GT3 | FALKE ONE MOTORSPORT Livery", use_container_width=True)
else:
    st.info("📸 Положи файл car.jpg в папку с проектом, чтобы увидеть фото машины!")

# --- 5.1. F1PERFORMANCE (ИНЖЕНЕРНОЕ БЮРО) ---
st.markdown("---")
st.markdown("<h2>️ F1PERFORMANCE</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #888; margin-top: -20px; margin-bottom: 20px;'>Инженерное бюро и техническая аналитика FALKE ONE MOTORSPORT</p>", unsafe_allow_html=True)

# ЭМБЛЕМА F1PERFORMANCE
if os.path.exists("Images/f1performance.png"):
    st.image("Images/f1performance.png", width=1000)
else:
    st.info("📸 Положи файл f1performance.png в папку с проектом!")

# ТЕКСТОВОЕ ОПИСАНИЕ В "СТЕКЛЯННОЙ" ФИГУРЕ
st.markdown("""
<div style="
    background-color: rgba(30, 30, 30, 0.4); 
    border: 1px solid rgba(255, 215, 0, 0.3); 
    border-radius: 20px; 
    padding: 30px; 
    backdrop-filter: blur(10px);
    margin-bottom: 20px;
">
    <p style="font-size: 1.15em; line-height: 1.8; margin-bottom: 15px; color: #e0e0e0;">
        <b style="color: #ffd700;">F1Performance</b> - это техническое ядро/Суббренд  FALKE ONE MOTORSPORT. 
        Здесь мы не просто «настраиваем машины», мы деконструируем физику симулятора.
    </p>
    <p style="font-size: 1.15em; line-height: 1.8; margin-bottom: 15px; color: #e0e0e0;">
        Глубокий анализ телеметрии, поиск идеальных сетапов, работа с давлением в шинах, 
        аэродинамическим балансом, работа подвески, термодинамикой мотора. Мы превращаем сырые данные в секунды на круге.
    </p>
    <p style="font-size: 1.2em; line-height: 1.6; color: #ffd700; font-weight: bold; text-align: center; margin-top: 25px; font-family: 'Rajdhani', sans-serif; letter-spacing: 1px;">
        "Мы не боремся с машиной. Мы адаптируем её под  нас."
    </p>
</div>
""", unsafe_allow_html=True)


# --- БЛОК БЕСПЛАТНЫХ СЕТАПОВ ---
st.markdown("---")
st.markdown("<h2> SETUPS BY F1PERFORMANCE</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;color:#888;'>Эксклюзивные настройки для доминирования на трассе</p>", unsafe_allow_html=True)

# Заголовок машины
st.markdown("<h3 style='color:#ffd700;text-align:center;font-family:Rajdhani,sans-serif;font-size:2em;margin-top:30px;'>AUDI TT CUP</h3>", unsafe_allow_html=True)

# Карточка с характеристикой
st.markdown("""
<div class="pilot-card" style="padding:25px;border-color:rgba(255,215,0,0.5);margin:20px 0;">
    <h4 style="color:#ffd700;font-family:Rajdhani,sans-serif;font-size:1.3em;margin-bottom:15px;">Характеристика сетапа:</h4>
    <p style="color:#e0e0e0;line-height:1.8;font-family:Montserrat,sans-serif;">
        Универсальный. Более улучшенная управляемость для лучшего заныривания в повороты. 
        Антикрыло дает баланс для быстрого развития скорости и стабильности задней оси. 
        Передняя ось слегка приподнята для агрессивной атаки поребриков.
    </p>
    <p style="color:#ffd700;font-weight:bold;margin-top:20px;font-family:Rajdhani,sans-serif;font-size:1.2em;">
        Автор: 𝗙𝟏𝗣𝗲𝗿𝗳𝗼𝗿𝗺𝗮𝗻𝗰𝗲  Senior Engineer ⚒︎
    </p>
</div>
""", unsafe_allow_html=True)

# Фото машины из шоурума
st.markdown("<p style='text-align:center;color:#888;margin:20px 0;'>Showroom Preview</p>", unsafe_allow_html=True)
if os.path.exists("audi_tt_setup.jpg"):
    st.image("audi_tt_setup.jpg", use_container_width=True)
else:
    st.info(" Положи скриншот машины под именем audi_tt_setup.jpg в папку с сайтом!")

# Кнопка по центру
st.markdown("<br>", unsafe_allow_html=True)
cm_link = "https://acstuff.club/s/yak"
st.markdown(f"""
<div style="text-align:center;margin:30px 0;">
    <a href="{cm_link}" class="link-btn" target="_blank" style="display:inline-block;max-width:500px;width:100%;">
        Импортировать сетап через Content Manager
    </a>
</div>
""", unsafe_allow_html=True)





# --- 6. ССЫЛКИ И КОНТАКТЫ ---
st.markdown("---")
st.markdown("<h2>ПРИСОЕДИНЯЙСЯ к нам!</h2>", unsafe_allow_html=True)

# ЗАМЕНИ ЭТИ ССЫЛКИ НА ВАШИ РЕАЛЬНЫЕ
discord_link = "https://discord.gg/DWUQeEQdrc"
tiktok_link = "https://tiktok.com/@falke_one_motorsport"
lfm_link = "https://lowfuelmotorsport.com/teams/detail/18394/members"

st.markdown(f'<a href="{discord_link}" class="link-btn" target="_blank">💬 Вступить в Discord FALKE ONE MOTORSPORT</a>', unsafe_allow_html=True)
st.markdown(f'<a href="{tiktok_link}" class="link-btn" target="_blank">🎵 Мы в TikTok</a>', unsafe_allow_html=True)
st.markdown(f'<a href="{lfm_link}" class="link-btn" target="_blank">🏆 Мы  на Low Fuel Motorsport</a>', unsafe_allow_html=True)

# --- ФУТЕР ---
st.markdown("---")
st.markdown("<p style='text-align: center; color: #555555; font-size: 12px;'>© 2026 FALKE ONE MOTORSPORT. Built for Champions. </p>", unsafe_allow_html=True)
