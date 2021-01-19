from django.apps import AppConfig


class NumberConfig(AppConfig):
    name = 'number'

    def ready(self):
        from number import number_generator
        number_generator.start()
