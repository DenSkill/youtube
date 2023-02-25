import os

from googleapiclient.discovery import build
import json

api_key = 'AIzaSyB_zRuBrxjY-cBxVeGZPzn7JeEofSDpe5c'

youtube = build('youtube', 'v3', developerKey=api_key)
channel_id = 'UC1eFXmJNkjITxPFWTy6RsWg'
channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()


class Channel:
    def __init__(self, id):
        self.id = id
        self.channel_id = channel_id

    def print_info(self):
        text = json.dumps(self.channel_id, indent=2, ensure_ascii=False)
        print(json.loads(text))


vdud = Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')
vdud.print_info()
