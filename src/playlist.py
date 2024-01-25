from src.channel import Channel


class PlayList(Channel):
    def __init__(self, id_playlist):
        self.id_playlist = id_playlist

    def get_info(self) -> None:
        youtube = self.get_service()
        return youtube.playlistItems().list(playlistId=self.id_playlist,
                                            part="snippet,contentDetails").execute()


pl = PlayList('PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw')
print(pl.get_info())
