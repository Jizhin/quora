from django.apps import AppConfig


class QuorappConfig(AppConfig):
    name = 'quorapp'

    def ready(self):
        import quorapp.signals
        pass