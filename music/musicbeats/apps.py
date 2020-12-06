from django.apps import AppConfig


class MusicbeatsConfig(AppConfig):
    name = 'musicbeats'


    def ready(self):
        import musicbeats.signals