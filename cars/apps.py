from django.apps import AppConfig


class CarrosConfig(AppConfig):
    name = 'cars'

    def ready(self):
        import cars.signals 