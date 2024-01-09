from googleapiclient.discovery import build
class Channel:
    """Класс для ютуб-канала"""
    youtube = build()

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        pass

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        pass