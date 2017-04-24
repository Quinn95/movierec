from importlib import import_module

from django.apps import AppConfig as BaseAppConfig


class AppConfig(BaseAppConfig):

    name = "v3_whattowatch"

    def ready(self):
        import_module("v3_whattowatch.receivers")
