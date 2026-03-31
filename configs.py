# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "35682421"))
    API_HASH = getenv("API_HASH", "f5e97f7ebbd5bb4eb93814e8b85d5ffd")
    BOT_TOKEN = getenv("BOT_TOKEN", "")
    # Your Force Subscribe Channel Id Below 
    CHID = int(getenv("CHID", "-1003802403847")) # Make Bot Admin In This Channel
    # Admin Or Owner Id Below
    SUDO = list(map(int, getenv("SUDO", "1471357181 2128743963").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://shoorveerpf001_db_user:S0sijTRD32E1pw2s@cluster0.qgerchs.mongodb.net/?appName=Cluster0")
    
cfg = Config()

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
