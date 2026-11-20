from pathlib import Path

BASE_DIR = Path(__file__).parent
IMAGE_DIR = BASE_DIR / "Images"

#  Ссылки
SOCIAL_LINKS = {
    "discord": "https://discord.gg/DWUQeEQdrc",
    "tiktok": "https://tiktok.com/@falke_one_motorsport",
    "lfm": "https://lowfuelmotorsport.com/teams/detail/18394/members"
}

#  Пилоты
PILOTS = [
    {"nick": "FALKE1_1 #145", "name": "Семёнов Арсений", "role": "Team Principal / Lead Driver/𝗙𝟏𝗣𝗲𝗿𝗳𝗼𝗿𝗺𝗮𝗻𝗰𝗲 Senior Engineer ⚒︎"},
    {"nick": "IvAn #15", "name": "Николаев Иван", "role": "Race Driver AC"},
    {"nick": "taifunvozduh #17", "name": "Омеги Геннадий", "role": "Race Driver AC"},
    {"nick": "sKIF #16", "name": "Афанасьев Матвей", "role": "Race Driver AC/Deputy Director"},
]

#  Симуляторы
SIMULATORS = [
    {"title": "ASSETTO CORSA", "image": "ac_bg.png"},
    {"title": "ASSETTO CORSA COMPETIZIONE", "image": "acc_bg.png"},
    {"title": "AUTOMOBILISTA 2", "image": "ams2_bg.png"},
]

#  Сетапы
SETUPS = [
    {
        "car": "AUDI TT CUP",
        "description": "Универсальный. Более улучшенная управляемость для лучшего заныривания в повороты. Антикрыло дает баланс для быстрого развития скорости и стабильности задней оси. Передняя ось слегка приподнята для агрессивной атаки поребриков.",
        "author": "𝗙𝟏𝗣𝗲𝗿𝗳𝗼𝗿𝗺𝗮𝗻𝗰𝗲 Senior Engineer ⚒︎",
        "image": "audi_tt_setup.jpg",
        "cm_link": "https://acstuff.club/s/zcoX"
    }
]

#  Тексты
TEAM_CREATED = "Наша команда создана 06.09.2026 и развивается с каждым днём!"

ABOUT_TEXT = """**FALKE ONE MOTORSPORT** - это не просто команда симрейсеров. Это сообщество симрейсеров, которые создают и ценят честную физику, инженерный подход и взаимное уважение. 
Мы не просто "катаем с рулём", мы строим империю. Наша цель -  попасть в историю симрейсинга,  победы в серьезных киберспортивных сериях на платформе Low Fuel Motorsport."""

QUOTE_TEXT = "Мы не боремся с машиной. Мы адаптируем её под нас."