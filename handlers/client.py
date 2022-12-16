from telethon import TelegramClient

api_id = 6031312
api_hash = "9098c9ccc1185098251c457ab85b655f"
bot_token = "5809313534:AAHO2Cni3WIK-BVvZicK6eqWa-slqAY1kn0"
client = TelegramClient('bbahodirov', api_id, api_hash)

botClient = TelegramClient('tg_magicbot', api_id, api_hash).start(bot_token=bot_token)