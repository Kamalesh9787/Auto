from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "25599491"))
    API_HASH = getenv("API_HASH", "c8e3c0561cf148a6504f27b111fc3698")
    BOT_TOKEN = getenv("BOT_TOKEN", "")
    FSUB = getenv("FSUB", "Tamil_Mini")
    CHID = int(getenv("CHID", "-1002053727982"))
    SUDO = list(map(int, getenv("SUDO", "5983189506").split()))
    MONGO_URI = getenv("MONGO_URI", "")
    
cfg = Config()
