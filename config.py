import json
import os
from pathlib import Path


CHECK_INTERVAL = 60  # in seconds
URLS_TO_CHECK = json.loads(Path('domains.json').read_text())
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')
