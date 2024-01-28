import datetime

import isodate

from src.channel import Channel


class PlayList(Channel):
    def __init__(self, id_playlist):
        self.id_playlist = id_playlist
        self._total_duration = None
        self.make_attribute_info()

    def get_info(self) -> None:
        youtube = self.get_service()
        return youtube.playlistItems().list(playlistId=self.id_playlist,
                                            part="snippet,contentDetails").execute()

    def make_attribute_info(self):
        info = self.get_info()
        self.title = info['items'][0]['snippet']['title']
        self.url = f"https://www.youtube.com/playlist?list={self.id_playlist}"
        self.video_ids: list[str] = [video['contentDetails']['videoId'] for video in info['items']]

    def get_duration_videos(self):
        youtube = self.get_service()
        video_response = youtube.videos().list(part='contentDetails,statistics',
                                               id=','.join(self.video_ids)
                                               ).execute()

        self._total_duration = datetime.timedelta()

        for video in video_response['items']:
            # YouTube video duration is in ISO 8601 format
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            self._total_duration += duration

    @property
    def total_duration(self):
        return self._total_duration


pl = PlayList('PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw')
print(pl.get_info())
print(pl.title)
print(pl.url)
print(pl.video_ids)
print(pl.get_duration_videos())
print(pl.total_duration)

