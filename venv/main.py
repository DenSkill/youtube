from config import api_key
import os

from googleapiclient.discovery import build
import json

api_key: str = os.getenv('YT_API_KEY')
youtube = build('youtube', 'v3', developerKey=api_key)

channel = youtube.channels().list(id=channel_id, part='snippet,statistics,description,items,viewCount').execute()


class Channel:
    def __init__(self, id):
        self.id = id

    def print_info(self):
        text = json.dumps(self.channel, indent=2, ensure_ascii=False)
        return json.loads(text)


vdud = Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')
vdud.print_info()
