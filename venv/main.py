import os

from googleapiclient.discovery import build
import json

from dotenv import load_dotenv


class Youtube:
    def __init__(self, channel_id):
        self.__channel_id = channel_id
        load_dotenv()
        api_key: str = os.environ.get('api_key')
        youtube = build('youtube', 'v3', developerKey=api_key)
        self.channel_info = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        self.title = self.channel_info['items'][0]['snippet']['title']
        self.description = self.channel_info['items'][0]['snippet']['description']
        self.url = 'https://www.youtube.com/' + self.__channel_id
        self.subscriber_count = self.channel_info['items'][0]['statistics']['subscriberCount']
        self.video_count = self.channel_info['items'][0]['statistics']['videoCount']
        self.view_count = self.channel_info['items'][0]['statistics']['viewCount']
        data = self.title = self.description + self.url + self.subscriber_count + self.video_count + self.view_count

    def print_info(self):
        print(json.dumps(self.channel_info, indent=2, ensure_ascii=False))

    def to_json(self):
        data = {
            "title": self.channel_info
        }
        with open('filename.json', "w", encoding="UTF-8") as file:
            json.dump(data, file, indent=2, ensure_ascii=False)

    @classmethod
    def get_service(self):
        service = build('youtube', 'v3', developerKey = os.environ.get('api_key'))
        return service
