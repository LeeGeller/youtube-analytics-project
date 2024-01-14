import os

from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        self.title = ''
        self.video_count = ''
        self.url = ''
        self.all_info = None

    def __repr__(self):
        return (f"{self.channel_id} id канала\n"
                f"{self.title} название канала\n"
                f"{self.video_count} количество видео\n"
                f"{self.url} url")

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        youtube = build('youtube', 'v3', developerKey="AIzaSyBh6pGPuYR5rbNQDIsLLqktyXtNTJWGHWA")
        self.all_info = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()

        for key, value in self.all_info.items():
            if key == 'items':
                for items in value:
                    self.title = items['snippet']['title']
                    self.video_count = items["statistics"]["videoCount"]
                    self.url = items["kind"]

        return self.all_info

    @classmethod
    def get_service(cls):
        return build('youtube', 'v3', developerKey="AIzaSyBh6pGPuYR5rbNQDIsLLqktyXtNTJWGHWA")


moscowpython = Channel('UC-OVMPlMA3-YCIeg4z5z23A')
print(moscowpython.print_info())
print(moscowpython.all_info)
print(moscowpython.title)
print(moscowpython.video_count)
