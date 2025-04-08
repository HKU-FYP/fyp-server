from enum import Enum
from datetime import datetime
import requests
from requests import HTTPError
import pytz

from src.config import load_config

cfg = load_config()

class DiscordClient:
    def __init__(
        self,
        channel_id: str,
        bot_token: str,
        base_url: str = "https://discord.com/api/v10",
    ):
        self.base_url = base_url
        self.url = base_url + f"/channels/{channel_id}/messages"
        self.headers = {"Authorization": f"Bot {bot_token}"}

    def report_news(
        self,
        stock_name: str,
        title: str,
        summary: str,
        published_date: datetime,
        sentiment: str
    ):
        utc_now = datetime.utcnow().strftime("%Y/%m/%d, %H:%M:%S")
        content = f"# News Alert for stock: {stock_name}\n* Published at: `{published_date}`\n* Sentiment: `{sentiment}`"
        embeds = [
            # {"title": f"Sentiment: {sentiment}"},
            {"title": title, "description": summary},
            # {"title": "Published date", "description": published_date},
            # {"title": "Summary", "description": summary},
        ]
        body = {"content": content, "tts": False, "embeds": embeds}
        requests.post(url=self.url, json=body, headers=self.headers)


discord_client = DiscordClient(
    channel_id=cfg.discord.channel_id,
    bot_token=cfg.discord.bot_token,
)