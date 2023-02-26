import os

from googleapiclient.discovery import build
import json

from dotenv import load_dotenv


class Youtube:
    def __init__(self, channel_id):
        self.channel_id = channel_id
        load_dotenv()
        api_key: str = os.getenv('YOUTUBE_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)
        self.channel_info = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        self.tittle = self.channel_info['items'][0]['snippet']['tittle']
        self.description = self.channel_info['items'][0]['snippet']['description']
        self.url = 'https://www.youtube.com/' + self.channel_id
        self.subscriber_count = self.channel_info['items'][0]['statistics']['subscriberCount']
        self.video_count = self.channel_info['items'][0]['statistics']['videoCount']
        self.view_count = self.channel_info['items'][0]['statistics']['viewCount']
        data = self.tittle = self.description + self.url + self.subscriber_count + self.video_count + self.view_count

    def print_info(self):
        print(json.dumps(self.channel_info, indent=2, ensure_ascii=False))


y = Youtube('UCMCgOm8GZkHp8zJ6l7_hIuA')
y.print_info()
