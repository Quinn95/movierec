from importlib import import_module

from django.apps import AppConfig as BaseAppConfig


class AppConfig(BaseAppConfig):

    name = "what2watch"

    def ready(self):
        import_module("what2watch.receivers")
