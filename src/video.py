from src.channel import Channel


# https://www.youtube.com/@egoroffchannel/videos
# channel_id='UC-OVMPlMA3-YCIeg4z5z23A'

class Video(Channel):
    def __init__(self, id_video):
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.id_video = id_video
        self.make_attribute_info()

    def get_info(self) -> None:
        youtube = self.get_service()
        return youtube.videos().list(id=self.id_video, part="snippet,contentDetails,statistics").execute()

    def make_attribute_info(self):
        info = self.get_info()
        self.title = info['items'][0]['snippet']['title']
        self.url = info['items'][0]['snippet']['thumbnails']['default']['url']
        self.view_count = info['items'][0]['statistics']['viewCount']
        self.like_count = info['items'][0]['statistics']['likeCount']


video = Video('AWX4JnAnjBE')
print(video.get_info())
print(video.make_attribute_info())
print(video.title)
print(video.url)
print(video.view_count)
print(video.like_count)
