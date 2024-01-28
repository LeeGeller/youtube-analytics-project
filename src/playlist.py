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
        self.video_response = youtube.videos().list(part='contentDetails,statistics',
                                                    id=','.join(self.video_ids)
                                                    ).execute()

        self._total_duration = datetime.timedelta()

        for video in self.video_response['items']:
            # YouTube video duration is in ISO 8601 format
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            self._total_duration += duration

    @property
    def total_duration(self):
        return self._total_duration

    def show_best_video(self):
        youtube = self.get_service()

        video_response = youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                               id=','.join(self.video_ids)
                                               ).execute()
        max_likes = 0

        best_video_id = ''

        for info in video_response['items']:
            if int(info['statistics']['likeCount']) > max_likes:
                max_likes = int(info['statistics']['likeCount'])
                best_video_id = info['id']

        return f"https://www.youtube.com/watch?v={best_video_id}"
