from django.apps import AppConfig


class SyteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'syte'


    def ready(self):
        import syte.signals  
