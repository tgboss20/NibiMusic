from os import getenv

from dotenv import load_dotenv

load_dotenv()

admins = {}

SESSION_NAME = getenv("SESSION_NAME", "BQBvL-IAFkmQq8XMzLDbl_HpZ53JtVd67trMlNaW1IX8fWgXBkwnQKgL3qw6ipd2-bwdhRAZ1pgfPz_ij8aM0UlZIqsngfhklUWVapnq-eogdyr4zXIzO-6x6bmx8GwYLzV39a0TmqxMZ2ypPJkCoRJPMT85_Q7FXEBv6oE3s5snx69z7ka9y556_StkthbLAS8m_g6On2y8hciU2Ub4W-RsIcMHAY1sQEPItjnITkK-w7F5cO5YERhRpb1GNmucqaekWx6_US66bh8Q1p0PR1OUMPRxnUj2tohsHwWHtXgzTHFzI9lkFIO-9uyj4cEIUeYI5pdZEHZ-0DXX1dpw_4LX3T_5TAAAAABPQVpRAA")

BOT_TOKEN = getenv("BOT_TOKEN", "6249078353:AAFcJLc7BxoTNc53Q36xkpaXA5pYloTDKzI")
API_ID = int(getenv("API_ID", "7286754"))
API_HASH = getenv("API_HASH", "ea32d6cdb32f751aca22f05fdea1d3a8")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "PrinceVcSupport")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "")
OWNER_ID = list(map(int, getenv("OWNER_ID", "1262312971").split()))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1262312971").split()))
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "120"))

IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/31e9ecee16a46575267a4.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/d744707634106cf76627a.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/c3401a572375b569138c3.png")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/d8f8fc1de9110b93ca94c.jpg")
YOUTUBE_IMG_URL = getenv(
    "YOUTUBE_IMG_URL", "https://te.legra.ph/file/bc5556476395a0c8e109b.jpg"
)
