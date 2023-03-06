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
        #self.playlist = youtube.playlists().list(id=playlist_id, part='snippet').execute()
        #self.playlist_name = self.playlist['items'][0]['snippet']['title']
        # data = self.title + self.description + self.url + self.subscriber_count + self.video_count + self.view_count

    def print_info(self):
        print(json.dumps(self.channel_info, indent=2, ensure_ascii=False))

    def to_json(self):
        data = {
            "title": self.channel_info
        }
        with open('venv/filename.json', "w", encoding="UTF-8") as file:
            json.dump(data, file, indent=2, ensure_ascii=False)

    @classmethod
    def get_service(self):
        service = build('youtube', 'v3', developerKey=os.environ.get('api_key'))
        return service

    def __str__(self) -> str:
        return f'{self.title}'

    def __lt__(self, other):
        if not isinstance(other, (Youtube)):
            raise TypeError('оперант справа должен принадлежать классу Youtube')

        x = other if isinstance(other, int) else other.subscriber_count
        return self.subscriber_count < x

    def __add__(self, other):
        return int(self.subscriber_count) + int(other.subscriber_count)


class Video:
    __API_KEY: str = os.getenv('api_key')

    def __init__(self, video_id):
        self.__video_id = video_id
        self._init_from_api()

    def _init_from_api(self):
        video_response = self.get_service().videos().list(part='snippet,statistics',
                                                          id=self.__video_id
                                                          ).execute()

        self.title = video_response['items'][0]['snippet']['title']
        self.url = f'https://youtu.be/{self.__video_id}'
        self.view_count = video_response['items'][0]['statistics']['viewCount']
        self.like_count = video_response['items'][0]['statistics']['likeCount']

    @classmethod
    def get_service(cls):
        service = build('youtube', 'v3', developerKey=cls.__API_KEY)
        return service

    def __str__(self) -> str:
        return self.title


class PLVideo(Video):
    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.playlist = self.get_service().playlists().list(id=playlist_id, part='snippet').execute()
        self.playlist_name = self.playlist['items'][0]['snippet']['title']

    def get_video_in_playlist(cls, video_id: str, playlist_id: str) -> dict:
        """Получает данные о видео в плейлисте"""
        video_in_playlist = cls.get_service().playlistItems().list(videoId=video_id,
                                                                   playlistId=playlist_id,
                                                                   part='snippet').execute()
        return video_in_playlist

video1 = Video('9lO06Zxhu88')
video2 = PLVideo('BBotskuyw_M', 'PL7Ntiz7eTKwrqmApjln9u4ItzhDLRtPuD')
print(video1)
#Как устроена IT-столица мира / Russian Silicon Valley (English subs)
print(video2)
#Пушкин: наше все? (Литература)