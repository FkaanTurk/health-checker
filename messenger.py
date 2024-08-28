import requests
import config


class Messenger:
    def __init__(self,
                 *,
                 telegram_bot_token: str = config.TELEGRAM_BOT_TOKEN,
                 chat_id: str = config.CHAT_ID) -> None:
        self.telegram_bot_token = telegram_bot_token
        self.chat_id = chat_id

    def send_message(self, message: str):
        requests.post(
            url=f'https://api.telegram.org/bot{self.telegram_bot_token}/sendMessage',
            headers={
                'Content-Type': 'application/json',
            },
            json={
                "chat_id": self.chat_id,
                "text": message
            }
        )
