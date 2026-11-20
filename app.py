import streamlit as st
from data import BASE_DIR, IMAGE_DIR, PILOTS, SIMULATORS, SETUPS, SOCIAL_LINKS, TEAM_CREATED, ABOUT_TEXT

#  0. ФУНКЦИЯ ДЛЯ КАРТИНОК
@st.cache_data
def get_image_path(image_name: str) -> str:
    """Возвращает путь к картинке из папки Images, если она существует."""
    img_path = IMAGE_DIR / image_name
    if img_path.exists():
        return str(img_path)
    return None

# 1. НАСТРОЙКИ СТРАНИЦЫ
st.set_page_config(
    page_title="FALKE ONE MOTORSPORT",
    page_icon="miniem.png ",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Стиль
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Rajdhani:wght@500;700&family=Montserrat:wght@400;600&display=swap');

    .stApp { background-color: #0a0a0a; color: #ffffff; }
    h1, h2, h3 { 
        color: #ffd700 !important; text-align: center; font-family: 'Rajdhani', sans-serif !important;
        font-weight: 700 !important; text-transform: uppercase; letter-spacing: 2px;
    }
    p { font-size: 1.1em; line-height: 1.6; font-family: 'Montserrat', sans-serif; color: #e0e0e0; }

    .pilot-card {
        background-color: rgba(30, 30, 30, 0.4); border: 1px solid rgba(255, 215, 0, 0.3);
        border-radius: 20px; padding: 20px; margin-bottom: 15px; text-align: center;
        backdrop-filter: blur(10px); transition: transform 0.3s ease;
    }
    .pilot-card:hover { transform: translateY(-5px); border-color: #ffd700; }
    .pilot-nick { color: #ffd700; font-weight: bold; font-size: 1.3em; font-family: 'Rajdhani', sans-serif; letter-spacing: 1px; }
    .pilot-name { color: #aaaaaa; font-size: 0.95em; margin-top: 5px; font-family: 'Montserrat', sans-serif; }

    .link-btn {
        display: block; width: 100%; padding: 15px; margin: 12px 0;
        background-color: rgba(255, 215, 0, 0.05); color: #ffd700 !important; text-align: center;
        text-decoration: none; border-radius: 50px; font-weight: bold; font-family: 'Rajdhani', sans-serif;
        font-size: 1.2em; letter-spacing: 1px; border: 2px solid #ffd700; transition: all 0.3s ease;
    }
    .link-btn:hover { 
        background-color: #ffd700; color: #000000 !important; 
        box-shadow: 0 0 20px rgba(255, 215, 0, 0.6); transform: translateY(-2px);
    }
    .block-container { max-width: 1150px !important; margin: 0 auto !important; }
    </style>
""", unsafe_allow_html=True)

#  2. ГЛАВНЫЙ ЭКРАН
st.markdown("<h1>FALKE ONE MOTORSPORT</h1>", unsafe_allow_html=True)

emblem_path = get_image_path("emblem.png")
if emblem_path:
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image(emblem_path, use_container_width=True) # use_container_width надежнее чем width=1500
else:
    st.info("📸 Положи файл emblem.png в папку Images, чтобы увидеть эмблему!")

#  3. О КОМАНДЕ
st.markdown("---")
st.subheader("О КОМАНДЕ")
st.markdown(f"<p style='text-align: center; color: #888; margin-top: -10px; margin-bottom: 20px;'>{TEAM_CREATED}</p>", unsafe_allow_html=True)
st.markdown(ABOUT_TEXT)

#  4. НАШИ СИМУЛЯТОРЫ
st.markdown("---")
st.markdown("<h2>НАШИ СИМУЛЯТОРЫ</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #888; margin-top: -20px; margin-bottom: 20px;'>Объединяет пилотов всех популярных платформ</p>", unsafe_allow_html=True)

st.markdown("""
<div style="background-color: rgba(30, 30, 30, 0.4); border: 1px solid rgba(255, 215, 0, 0.3); border-radius: 20px; padding: 20px; text-align: center; margin-bottom: 20px;">
    <p style="font-size: 1.15em; color: #e0e0e0; margin: 0;">
        Мы не ограничиваем себя одной игрой. <b style="color: #ffd700;">FALKE ONE MOTORSPORT</b> - это сообщество пилотов, которые катают на всех топовых симуляторах:
    </p>
</div>
""", unsafe_allow_html=True)

#  Вывод симуляторов из data.py
cols_sim = st.columns(len(SIMULATORS))
for i, sim in enumerate(SIMULATORS):
    with cols_sim[i]:
        st.markdown(f"""
        <div class="pilot-card">
            <div class="pilot-nick">{sim['title']}</div>
        </div>
        """, unsafe_allow_html=True)
        img_path = get_image_path(sim["image"])
        if img_path:
            st.image(img_path, use_container_width=True)

st.markdown("""
<div style="background-color: rgba(30, 30, 30, 0.4); border: 1px solid rgba(255, 215, 0, 0.3); border-radius: 20px; padding: 20px; text-align: center; margin-top: 20px;">
    <p style="font-size: 1.1em; color: #e0e0e0; margin: 0;">Каждый пилот выбирает свой симулятор, но все мы - одна команда.</p>
</div>
""", unsafe_allow_html=True)

#  5. СОСТАВ (ПИЛОТЫ)
st.markdown("---")
st.markdown("<h2>Состав</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #888;'>Те, кто пишет историю команды</p>", unsafe_allow_html=True)

#  Вывод пилотов из data.py
cols = st.columns(2)
for i, pilot in enumerate(PILOTS):
    with cols[i % 2]: # Магически раскидывает: 0->col1, 1->col2, 2->col1, 3->col2
        st.markdown(f"""
        <div class="pilot-card">
            <div class="pilot-nick">{pilot['nick']}</div>
            <div class="pilot-name">{pilot['name']}</div>
            <div style="color: #ffd700; font-size: 0.8em; margin-top: 5px;">{pilot['role']}</div>
        </div>
        """, unsafe_allow_html=True)

#  6. НАША МАШИНА
st.markdown("---")
st.markdown("<h2>БОЛИДЫ</h2>", unsafe_allow_html=True)
car_path = get_image_path("car.jpg")
if car_path:
    st.image(car_path, caption="BMW M4 2021 GT3 | FALKE ONE MOTORSPORT Livery", use_container_width=True)
else:
    st.info("📸 Положи файл car.jpg в папку Images, чтобы увидеть фото машины!")

#  7. F1PERFORMANCE
st.markdown("---")
st.markdown("<h2>F1PERFORMANCE</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #888; margin-top: -20px; margin-bottom: 20px;'>Инженерное бюро и техническая аналитика FALKE ONE MOTORSPORT</p>", unsafe_allow_html=True)

f1_path = get_image_path("f1performance.png")
if f1_path:
    st.image(f1_path, use_container_width=True)
else:
    st.info("📸 Положи файл f1performance.png в папку Images!")

st.markdown("""
<div style="background-color: rgba(30, 30, 30, 0.4); border: 1px solid rgba(255, 215, 0, 0.3); border-radius: 20px; padding: 30px; backdrop-filter: blur(10px); margin-bottom: 20px;">
    <p style="font-size: 1.15em; line-height: 1.8; margin-bottom: 15px; color: #e0e0e0;">
        <b style="color: #ffd700;">F1Performance</b> - это техническое ядро/Суббренд FALKE ONE MOTORSPORT. 
        Здесь мы не просто «настраиваем машины», мы деконструируем физику симулятора.
    </p>
    <p style="font-size: 1.15em; line-height: 1.8; margin-bottom: 15px; color: #e0e0e0;">
        Глубокий анализ телеметрии, поиск идеальных сетапов, работа с давлением в шинах, 
        аэродинамическим балансом, работа подвески, термодинамикой мотора. Мы превращаем сырые данные в секунды на круге.
    </p>
    <p style="font-size: 1.2em; line-height: 1.6; color: #ffd700; font-weight: bold; text-align: center; margin-top: 25px; font-family: 'Rajdhani', sans-serif; letter-spacing: 1px;">
        "Мы не боремся с машиной. Мы адаптируем её под нас."
    </p>
</div>
""", unsafe_allow_html=True)

#  8. БЛОК БЕСПЛАТНЫХ СЕТАПОВ
st.markdown("---")
st.markdown("<h2>SETUPS BY F1PERFORMANCE</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;color:#888;'>Эксклюзивные настройки для доминирования на трассе</p>", unsafe_allow_html=True)

#  Вывод сетапов из data.py
for setup in SETUPS:
    st.markdown(f"<h3 style='color:#ffd700;text-align:center;font-family:Rajdhani,sans-serif;font-size:2em;margin-top:30px;'>{setup['car']}</h3>", unsafe_allow_html=True)

    st.markdown(f"""
    <div class="pilot-card" style="padding:25px;border-color:rgba(255,215,0,0.5);margin:20px 0;">
        <h4 style="color:#ffd700;font-family:Rajdhani,sans-serif;font-size:1.3em;margin-bottom:15px;">Характеристика сетапа:</h4>
        <p style="color:#e0e0e0;line-height:1.8;font-family:Montserrat,sans-serif;">{setup['description']}</p>
        <p style="color:#ffd700;font-weight:bold;margin-top:20px;font-family:Rajdhani,sans-serif;font-size:1.2em;">Автор: {setup['author']}</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<p style='text-align:center;color:#888;margin:20px 0;'>Showroom Preview</p>", unsafe_allow_html=True)
    setup_img_path = get_image_path(setup['image'])
    if setup_img_path:
        st.image(setup_img_path, use_container_width=True)
    else:
        st.info(f"📸 Положи скриншот машины под именем {setup['image']} в папку Images!")

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"""
    <div style="text-align:center;margin:30px 0;">
        <a href="{setup['cm_link']}" class="link-btn" target="_blank" style="display:inline-block;max-width:500px;width:100%;">
            Импортировать сетап через Content Manager
        </a>
    </div>
    """, unsafe_allow_html=True)

#  9. ССЫЛКИ И КОНТАКТЫ
st.markdown("---")
st.markdown("<h2>ПРИСОЕДИНЯЙСЯ к нам!</h2>", unsafe_allow_html=True)

#  Ссылки из data.py
st.markdown(f'<a href="{SOCIAL_LINKS["discord"]}" class="link-btn" target="_blank">💬 Вступить в Discord FALKE ONE MOTORSPORT</a>', unsafe_allow_html=True)
st.markdown(f'<a href="{SOCIAL_LINKS["tiktok"]}" class="link-btn" target="_blank">🎵 Мы в TikTok</a>', unsafe_allow_html=True)
st.markdown(f'<a href="{SOCIAL_LINKS["lfm"]}" class="link-btn" target="_blank">🏆 Мы на Low Fuel Motorsport</a>', unsafe_allow_html=True)

#  10. ФУТЕР
st.markdown("---")
st.markdown("<p style='text-align: center; color: #555555; font-size: 12px;'>© 2026 FALKE ONE MOTORSPORT. Built for Champions. </p>", unsafe_allow_html=True)